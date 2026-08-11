# AI Coding Workflows: From Cloud to Local

This repository contains the companion files for the DeepLearning.AI AI Coding Workflows course. It includes the project specifications, Python dependencies, and custom implementer-agent configuration you'll use to build a simple Python web app throughout the course.

## Other DeepLearning.AI Resources
> :mortar_board: **Keep learning** → [Explore all DeepLearning.AI courses](https://www.deeplearning.ai/courses/) — taught by the people building the future of AI. Find your next one.
>
> :computer: **Explore more course artifacts** → [Browse the DeepLearning.AI course artifacts repo](https://github.com/https-deeplearning-ai/deeplearning-ai) to find notebooks, projects, and notes from other courses across the DeepLearning.AI library.

## How to use this repo

The simplest way to take this course is to follow the videos in order, using the same project throughout. During setup in Lesson 2, you'll create your own project and copy in the starting files from `Lessons_02-08`. From there, the course itself walks you through every change that appears in the later folders, so you won't need to copy anything else.

The repo is organized into three folders. Each holds the project files as they should look during that stretch of the course:

| Folder | Contents |
|---|---|
| `Lessons_02-08` | The starting files: project specs and Python dependencies |
| `Lessons_09` | Adds the implementer subagent configuration created in Lesson 9 |
| `Lessons_11-12` | The three-phase roadmap and the local-model implementer from Lesson 11 |

The later folders are there so you can jump into the course partway through, or check your own files against a known-good state.

A few notes:

- The `Lessons_09` folder already contains the implementer file that Lesson 9 teaches you to create. If you're working from that folder while following Lesson 9 itself, delete `.opencode/agents/implementer.md` first and let the lesson's prompt create it. If you're jumping in after Lesson 9, keep it as is.
- Likewise, the roadmap in `Lessons_11-12` already has the Phase 3 split that Lesson 11 has you make, so skip the roadmap-split prompt if you start from that folder.
- The course was recorded on a Mac, so the local-model references in the implementer configuration and prompts use Mac values: MLX model builds and the `.venv/bin/python` test command. On Windows or Linux, substitute your GGUF model ID from LM Studio and `.venv\Scripts\python`.

All prompts used in the course are collected in [prompts.md](prompts.md), so you can copy them rather than typing them from the videos.

## Project files

| Path | Purpose |
|---|---|
| `prompts.md` | Every prompt used in the course, with notes on when and how to run each one. Keep this file open while you follow along |
| `specs/mission.md` (in each folder) | Describes the app, its purpose, and the experience it should provide |
| `specs/tech-stack.md` (in each folder) | Records the required technologies and implementation constraints |
| `specs/roadmap.md` (in each folder) | Breaks the app into phases that coding agents can plan and implement |
| `.opencode/agents/implementer.md` | Defines the custom implementer subagent (in `Lessons_09` and `Lessons_11-12` only) |
| `requirements.txt` (in each folder) | Lists the Python packages required by the project |
| `.gitignore` | Excludes virtual environments, Python cache files, local configuration, and editor files from Git |

## Prerequisites

- [Python 3.11 or later](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)
- An IDE or editor: the course uses [PyCharm](https://www.jetbrains.com/pycharm/download/)
- [Claude Code](https://code.claude.com/docs/en/getting-started)
- [OpenCode](https://opencode.ai/docs/)
- An [OpenRouter](https://openrouter.ai/docs/quickstart) account
- [LM Studio](https://lmstudio.ai/download)
