# 🧠 Resume Screening Agent — Architecture Overview

---

## 1. Overview

The **Resume Screening Agent** is an AI-powered system designed to automate and standardize the evaluation of job candidates.

It enables recruiters to:
- Upload a **Job Description (JD)** and multiple **CVs**
- Extract structured candidate information (skills, experience, education)
- Compute **match scores** based on job requirements
- Rank candidates automatically
- View **clear, explainable insights** for decision-making

### 👤 Users
- Recruiters and Talent Acquisition teams  
- Hiring Managers  
- Recruitment Agencies  

### 🚀 Key Capabilities
- Automated resume parsing (PDF/Text)
- LLM-based structured data extraction
- Hybrid scoring (rule-based + semantic)
- Candidate ranking and comparison
- Explainable AI-driven insights
- Interactive UI via Streamlit

---

## 2. Problem Statement

### ❗ Real-World Hiring Challenges
- High volume of applications (100–500+ per role)
- Manual screening is time-consuming and inconsistent
- Keyword-based ATS systems lack semantic understanding
- Difficulty in maintaining fair and explainable evaluation

### 💡 Why This Solution Matters
This system introduces:
- **Automation** → reduces manual effort significantly  
- **Consistency** → standardized scoring across candidates  
- **Intelligence** → semantic understanding of skills and experience  
- **Transparency** → clear explanations for rankings  

### 💼 Business Value
- Reduces recruiter workload and time-to-hire  
- Improves quality of shortlisted candidates  
- Enables scalable hiring processes  
- Provides auditability and fairness in screening  

---

## 3. System Architecture

The system follows a **modular, service-oriented architecture** combining LLM intelligence with deterministic scoring.

### 🖥️ Streamlit UI
- User-facing interface for recruiters  
- Accepts JD input and CV uploads  
- Displays ranked candidates, scores, and explanations  

### ⚡ Backend (FastAPI / Internal Services)
- Handles request processing and orchestration  
- Connects UI with processing modules  
- Enables scalability and API-based integrations  

### 📄 Resume Parser
- Extracts raw text from CVs (PDF/Text)  
- Cleans and normalizes content for downstream processing  

### 🧠 LLM Extraction Layer
- Converts unstructured text → structured JSON  
- Extracts:
  - Skills  
  - Experience  
  - Education  
  - Role relevance  
- Enforced using schema validation (e.g., Pydantic)  

### 📊 Scoring Engine
- Computes candidate-job match scores using:
  - Rule-based logic (skills, experience, keywords)  
  - Optional semantic similarity (embeddings)  
- Produces transparent, explainable scoring  

### 🗂️ Optional Storage Layer
- **Vector DB (FAISS/Chroma)** for semantic search and similarity  
- **In-memory storage** for lightweight/local execution  

---

## 4. Architecture Diagram (Text-Based)

```text
                ┌──────────────────────────┐
                │       Streamlit UI       │
                │  (JD Input + CV Upload)  │
                └───────────┬──────────────┘
                            │
                            ▼
                ┌──────────────────────────┐
                │     Backend Layer        │
                │   (FastAPI / Services)   │
                └───────────┬──────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌────────────────┐
│ JD Analyzer  │   │ Resume Parser│   │ Resume Loader  │
│ (LLM Agent)  │   │ (PDF/Text)   │   │ (File Handling)│
└──────┬───────┘   └──────┬───────┘   └────────┬───────┘
       ▼                  ▼                    ▼
┌────────────────────────────────────────────────────┐
│         LLM Extraction Layer (Structured Data)     │
│  - Skills Extraction                               │
│  - Experience Parsing                              │
│  - Role Understanding                              │
└──────────────┬─────────────────────────────────────┘
               ▼
      ┌────────────────────────┐
      │   Feature Builder      │
      │ (Standardized Profiles)│
      └──────────┬─────────────┘
                 ▼
      ┌────────────────────────┐
      │    Scoring Engine      │
      │ - Rule-based scoring   │
      │ - Semantic similarity  │
      └──────────┬─────────────┘
                 ▼
      ┌────────────────────────┐
      │    Ranking Engine      │
      └──────────┬─────────────┘
                 ▼
      ┌─────────────────────────────┐
      │  Explanation Generator (LLM)│
      └──────────┬──────────────────┘
                 ▼
        ┌────────────────────────┐
        │   Results to UI        │
        │ (Rankings + Insights)  │
        └────────────────────────┘
```
