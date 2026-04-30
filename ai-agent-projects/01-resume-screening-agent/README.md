# 🤖 AI Resume Screening System (Multi-Agent Pipeline)

This project is a **production-style AI Resume Screening System** built as part of a portfolio showcasing **LLM-powered multi-agent architecture, structured data extraction, and scalable system design**.

---

## 🎯 Project Overview

The system simulates a real-world recruitment screening pipeline where:

- Job Descriptions are analyzed into structured requirements
- Resumes are parsed into structured candidate profiles
- Candidates are evaluated and ranked (coming next)
- Final results are displayed via a UI layer (coming next)

---

## 🧠 Current Stage (Stage 1 Completed)

### ✅ Resume Parser Agent

This is the first implemented agent in the pipeline.

It is responsible for:

- Accepting raw resume text input
- Cleaning and normalizing the text
- Using an LLM to extract structured candidate information
- Validating output using Pydantic models
- Returning structured JSON profiles

---

## 🧱 System Architecture (Current State)

```plaintext
Resume Text
     ↓
Resume Parser Agent
     ↓
LLM-based Extraction Layer
     ↓
Pydantic Validation Layer
     ↓
Structured Candidate Profile (JSON)
````

---

## ✨ Features Implemented (Stage 1)

✔ Resume text ingestion  
✔ Text cleaning and preprocessing  
✔ LLM-based structured extraction  
✔ Strong schema validation using Pydantic  
✔ Debug logging at every step  
✔ Error handling with safe fallbacks  
✔ Test-driven execution support  
✔ Standalone execution via `main.py`  

---

## 🧠 Resume Parser Agent (Deep Dive)

### Responsibilities:

* Extracts:

  * Full name
  * Email
  * Phone number
  * Skills
  * Work experience
  * Education details
  * Summary (if available)

### Output Format:

Structured JSON output ensuring consistency across candidates.

---

## ⚙️ Tech Stack

| Component                   | Purpose                         |
| --------------------------- | ------------------------------- |
| Python                      | Core application logic          |
| OpenAI API                  | LLM-based extraction            |
| Pydantic                    | Structured schema validation    |
| dotenv                      | Environment variable management |
| Logging (custom print logs) | Debugging and traceability      |

---

## 📁 Project Structure

```plaintext
01-resume-screening-agent/
│
├── agents/
│   └── resume_parser.py        # Core Resume Parser Agent
│
├── models/
│   └── candidate_schema.py     # Pydantic schema definitions
│
├── services/
│   └── llm_service.py          # LLM abstraction layer
│
├── utils/
│   └── text_cleaner.py         # Text preprocessing utilities
│
├── tests/
│   └── test_resume_parser.py   # Test execution script
│
├── main.py                     # Entry point for demo execution
├── requirements.txt
├── .env                        # API keys (not committed)
└── README.md
```

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/SureshGopalakrishnan/AI
cd ai-agent-projects/01-resume-screening-agent
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

```bash
# Windows
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ How to Run

### Run main demo

```bash
python main.py
```

---

### Run tests

```bash
python -m tests.test_resume_parser
```

---

## 🧪 Example Input

```text
Suresh Gopalakrishnan
suresh.gopalakrishnan@email.com | +44 7123456789

Experience:
Software Engineer at Google (2020-2023)
- Built scalable backend systems
- Worked on distributed systems

Education:
BSc Computer Science, University of Oxford

Skills:
Python, Machine Learning, Distributed Systems
```

---

## 📤 Example Output

```json
{
  "full_name": "Suresh Gopalakrishnan",
  "email": "suresh.gopalakrishnan@email.com",
  "phone": "+44 7123456789",
  "skills": [
    "Python",
    "Machine Learning",
    "Distributed Systems"
  ],
  "experience": [
    {
      "company": "Google",
      "role": "Software Engineer",
      "duration": "2020-2023",
      "responsibilities": [
        "Built scalable backend systems",
        "Worked on distributed systems"
      ]
    }
  ],
  "education": [
    {
      "institution": "University of Oxford",
      "degree": "BSc Computer Science",
      "year": "2020"
    }
  ]
}
```

---

## 🧠 Design Highlights

* Modular agent-based architecture
* Clear separation of concerns (parser, service, utils, models)
* LLM abstraction layer for scalability
* Strong schema validation for reliability
* Debug-first development approach

---

## 🔜 Roadmap (Upcoming Agents)

### Stage 2: JD Analyzer Agent

* Extract structured requirements from job descriptions

### Stage 3: Matching / Scoring Agent

* Compare candidates vs JD requirements

### Stage 4: Ranking Engine

* Rank multiple candidates based on fit score

### Stage 5: Streamlit UI

* Interactive recruiter dashboard

---

## 📌 Notes

* `.env` file is required for API access
* Project follows monorepo structure
* Each agent is independently testable
* Designed for extensibility and production-style thinking

---

## ⭐ Purpose of this Project

This project demonstrates:

* LLM application design
* Multi-agent system architecture
* Structured data extraction
* Real-world AI engineering practices
* Portfolio-ready system design thinking

---
