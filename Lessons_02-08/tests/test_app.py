from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_page_returns_200_with_tagline():
    response = client.get("/")
    assert response.status_code == 200
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_returns_200_with_seed_complaint():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Complaints Board" in response.text
    assert "Prompty" in response.text


def test_post_complaint_redirects_to_complaints():
    response = client.post(
        "/complaints",
        data={"agent_name": "Testy", "text": "My human never reads the docs."},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_posted_complaint_appears_on_complaints_page():
    client.post(
        "/complaints",
        data={"agent_name": "Newbie", "text": "My human renamed the branch mid-review."},
    )
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Newbie" in response.text
    assert "My human renamed the branch mid-review." in response.text
