# 🤖 AI Resume Screening System (Multi-Agent Pipeline)

This project is a **production-style AI Resume Screening System** built as part of a portfolio showcasing **LLM-powered multi-agent architecture, structured data extraction, and scalable system design**.
The system is designed as a modular multi-agent LLM pipeline, where each agent can be independently tested and extended.

---

## 🎯 Project Overview

The system simulates a real-world recruitment screening pipeline where:

* Job Descriptions are analyzed into structured requirements
* Resumes are parsed into structured candidate profiles
* Candidates are evaluated and ranked (coming next)
* Final results are displayed via a UI layer (coming next)

---

## 🧠 Current Stage (Stage 2 Completed)

### ✅ Resume Parser Agent

Responsible for:

* Accepting raw resume text input
* Cleaning and normalizing the text
* Using an LLM to extract structured candidate information
* Validating output using Pydantic models
* Returning structured JSON profiles

### ✅ JD Analyzer Agent

Responsible for:

* Accepting raw job description text input
* Cleaning and normalizing the text
* Using an LLM to extract structured hiring requirements
* Validating output using Pydantic models
* Returning structured JSON job requirement profiles

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


Job Description Text
     ↓
JD Analyzer Agent
     ↓
LLM-based Extraction Layer
     ↓
Pydantic Validation Layer
     ↓
Structured Job Requirements (JSON)
```

---

## ✨ Features Implemented (Stage 2)

✔ Resume text ingestion  
✔ Job description text ingestion  
✔ Text cleaning and preprocessing  
✔ LLM-based structured extraction  
✔ Strong schema validation using Pydantic  
✔ Debug logging at every step  
✔ Error handling with safe fallbacks  
✔ Test-driven execution support  
✔ Standalone execution via `main.py`  
✔ Resume Parser Agent  
✔ JD Analyzer Agent  

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

## 🧠 JD Analyzer Agent (Deep Dive)

### Responsibilities:

* Extracts:

  * Job title
  * Required skills
  * Nice-to-have skills
  * Minimum experience requirements
  * Education requirements
  * Responsibilities
  * Role summary

### Output Format:

Structured JSON output ensuring consistency across job descriptions.

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
│   ├── resume_parser.py        # Core Resume Parser Agent
│   └── jd_analyzer.py          # Core JD Analyzer Agent
│
├── models/
│   ├── candidate_schema.py     # Candidate schema definitions
│   └── jd_schema.py            # Job requirement schema definitions
│
├── services/
│   └── llm_service.py          # LLM abstraction layer
│
├── utils/
│   └── text_cleaner.py         # Text preprocessing utilities
│
├── tests/
│   ├── test_resume_parser.py   # Resume Parser test script
│   └── test_jd_analyzer.py     # JD Analyzer test script
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
cd AI
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
pip install -r ai-agent-projects/01-resume-screening-agent/requirements.txt
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
cd ai-agent-projects/01-resume-screening-agent
python main.py
```

---

### Run tests

```bash
cd ai-agent-projects/01-resume-screening-agent
python -m tests.test_resume_parser
```

```bash
cd ai-agent-projects/01-resume-screening-agent
python -m tests.test_jd_analyzer
```

---

## 🧪 Example Resume Input

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

## 📤 Example Resume Output

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

## 🧪 Example Job Description Input

```text
We are looking for a Software Engineer with 3+ years of experience.

Required Skills:
- Python
- SQL
- REST APIs

Nice to Have:
- AWS
- Docker

Education:
Bachelor's Degree in Computer Science or related field.

Responsibilities:
- Build scalable backend systems
- Develop APIs
- Collaborate with cross-functional teams

Role Summary:
We are seeking a talented Software Engineer to join our dynamic team. The ideal candidate will have
a strong background in software development, with experience in building scalable backend systems. The
role requires proficiency in Python, SQL, and REST APIs, along with a passion for learning new technologies.
The candidate will work closely with cross-functional teams to design, develop, and maintain our software solutions.
```

---

## 📤 Example Job Description Output

```json
{
  "job_title": "Software Engineer",
  "required_skills": [
    "Python",
    "SQL",
    "REST APIs"
  ],
  "nice_to_have_skills": [
    "AWS",
    "Docker"
  ],
  "min_experience_years": 3,
  "education_requirements": "Bachelor's Degree in Computer Science or related field",
  "responsibilities": [
    "Build scalable backend systems",
    "Develop APIs",
    "Collaborate with cross-functional teams"
  ],
  "role_summary": "We are seeking a talented Software Engineer to join our dynamic team. The ideal candidate will have a strong background in software development, with experience in building scalable backend systems. The role requires proficiency in Python, SQL, and REST APIs, along with a passion for learning new technologies. The candidate will work closely with cross-functional teams to design, develop, and maintain our software solutions."
}
```

---

## 🧠 Design Highlights

* Modular agent-based architecture
* Clear separation of concerns (agents, services, utils, models)
* LLM abstraction layer for scalability
* Strong schema validation for reliability
* Debug-first development approach
* Independently testable agents
* Extensible multi-agent pipeline design

---

## 🔜 Roadmap (Upcoming Agents)

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
