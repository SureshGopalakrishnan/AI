# 🧠 AI Engineering Portfolio Monorepo

## Production-Grade AI, Agentic AI & Multi-Agent Systems Portfolio

This repository is a **production-grade monorepo** showcasing practical **AI Engineering, Agentic AI, and Multi-Agent Systems projects** aligned to real-world enterprise use cases and the **UK AI job market**.

The portfolio is designed to demonstrate:

* **AI agent design and orchestration**
* **LangGraph / workflow-based agent systems**
* **LLM application engineering**
* **FastAPI + Streamlit deployment patterns**
* **multi-agent collaboration architectures**
* **shared tooling and reusable components**
* **production-ready project scaffolding**
* **clean monorepo engineering standards**

The repository combines:

* legacy foundational AI demos
* recruiter-ready flagship portfolio projects
* reusable shared utilities
* deployment-ready application templates

---

# 📁 Monorepo Structure

```text
AI/
├── shared/                       # Reusable prompts, tools, utilities, agents
├── foundations/                  # Legacy proof-of-concept projects
├── ai-agent-projects/            # Single-agent enterprise AI systems
├── agentic-ai-workflows/         # Workflow-driven autonomous AI systems
├── multi-agent-systems/          # Multi-agent orchestration projects
├── architecture-diagrams/        # HLD, LLD, workflow diagrams
├── docs/                         # Setup, scripts, design notes
├── streamlit-apps/               # Shared UI prototypes and dashboards
├── deployment/                   # Docker, cloud, CI/CD configs
├── requirements-dev.txt          # Shared development dependencies
└── pyproject.toml                # Repo engineering standards
```

---

# 🚀 Current Portfolio Projects

These are the **currently implemented or actively in-progress projects** in this monorepo.

## 🚧 Active Flagship Project

| Folder                                        | Description                                                               | Core Technologies                                     | Status      |
| :-------------------------------------------- | :------------------------------------------------------------------------ | :---------------------------------------------------- | :---------- |
| `ai-agent-projects/01-resume-screening-agent` | Intelligent CV parser, JD matcher, recruiter scorecard and ranking engine | Python, LangGraph, OpenAI, Streamlit, FastAPI, Pandas | In Progress |

---

# 🗓️ 90-Day Portfolio Roadmap

The following flagship projects are part of the planned delivery roadmap and will be moved into the active section as they are implemented.

## 🤖 AI Agent Projects

* `ai-agent-projects/02-ticket-agent`
* `ai-agent-projects/03-sql-data-analyst-agent`

## ⚡ Agentic AI Workflow Projects

* `agentic-ai-workflows/04-research-summarizer`
* `agentic-ai-workflows/05-meeting-minutes-agent`
* `agentic-ai-workflows/06-finance-goal-planner`

## 🤝 Multi-Agent AI Systems

* `multi-agent-systems/07-customer-support-system`
* `multi-agent-systems/08-research-report-generator`
* `multi-agent-systems/09-data-pipeline-insight-system`

---

# 🏗️ Foundations (Legacy Projects)

These are your earlier proof-of-concept projects, now preserved under `foundations/`.

| Folder                                                                 | Title                                      | Core Technologies                     | Status           |
| :--------------------------------------------------------------------- | :----------------------------------------- | :------------------------------------ | :--------------- |
| **[`foundations/content-generator`](./foundations/content-generator)** | Multi-Agent Social Media Content Generator | Gradio, LangChain, Groq API, Pydantic | Proof of Concept |
| **[`foundations/temple-chatbot`](./foundations/temple-chatbot)**       | Sri Lalithambigai Temple ChatBot           | Python, Gemini API, Search Grounding  | Proof of Concept |

These projects represent the **foundation of your AI engineering journey**.

---

# ⚙️ Engineering Standards

## 🧪 Environment Strategy

This monorepo uses a **hybrid dependency model**:

### Shared development environment

* root `.venv`
* `requirements-dev.txt`
* shared linting/testing packages

### Project-level runtime isolation

Each flagship project contains its own:

* `requirements.txt`
* `Dockerfile`
* `.env.example`
* `README.md`

This gives the best balance of:

* development speed
* reproducibility
* recruiter usability
* deployment portability

---

# ▶️ Running a Project Locally

## 1) Clone repository

```bash
git clone https://github.com/SureshGopalakrishnan/AI.git
cd AI
```

## 2) Create shared development environment

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## 3) Run any specific project

```bash
cd ai-agent-projects/01-resume-screening-agent
pip install -r requirements.txt
streamlit run app/ui.py
```

---

# ☁️ Deployment Strategy

Each flagship project is designed for:

* **Streamlit Community Cloud** → fast UI demos
* **Render / Railway** → FastAPI services
* **Docker Desktop** → local reproducibility
* **Azure / AWS** → enterprise-ready deployment path

---

# 💼 Portfolio Positioning for UK AI Market

This monorepo is intentionally aligned with roles such as:

* AI Engineer
* Agentic AI Engineer
* Applied LLM Engineer
* GenAI Solution Architect
* ML Platform Engineer
* AI Product Engineer
* Data + AI Solutions Consultant

The emphasis is on **practical business use cases**, not toy notebooks.

---
