from pathlib import Path

import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models import Complaint, complaints

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="AgentClinic")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/complaints")
def list_complaints(request: Request):
    return templates.TemplateResponse(
        request, "complaints.html", {"complaints": complaints}
    )


@app.post("/complaints")
def add_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaints.append(Complaint(agent_name=agent_name, text=text))
    return RedirectResponse("/complaints", status_code=303)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, reload_dirs=[str(BASE_DIR)])
