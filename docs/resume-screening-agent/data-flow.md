# 🧠 Resume Screening Agent — Data Flow Design

---

## 1. Overview of Data Flow

- User provides:
  - Job Description (JD)
  - Multiple CVs
- System processes data through sequential pipeline:
  - Ingestion → Preprocessing → LLM Extraction → Transformation → Scoring → Ranking → Output
- Output:
  - Ranked candidate list
  - Explainable scoring breakdown

---

## 2. Job Description (JD) Input Flow

- User input via Streamlit UI
- Validation steps:
  - non-empty check
  - minimum character length check
- Preprocessing:
  - lowercase conversion
  - whitespace normalization
  - special character removal
- Output passed to LLM extraction layer

---

## 3. CV Ingestion Flow

- User uploads CV files (PDF/DOC/TXT)
- For each file:
  - assign candidate_id
  - store temporarily in session storage
- Parsing initiation:
  - PDF → text extraction
  - DOC → text extraction
  - TXT → direct read
- Output:
  - raw extracted text per candidate

---

## 4. Preprocessing Layer

- PDF/Text extraction:
  - PyPDF2 / pdfminer extraction
  - OCR fallback (if scanned PDF)
- Cleaning steps:
  - remove headers/footers
  - remove special characters
  - normalize whitespace
- Normalization:
  - encoding fixes
  - section alignment (Skills, Experience, Education)
- Error handling:
  - corrupted file detection
  - empty text rejection

---

## 5. LLM Extraction Flow

### 🧾 JD Extraction
- Input: cleaned JD text
- Output: structured job requirements

### 📄 CV Extraction
- Input: cleaned CV text
- Output: structured candidate profile

### 🧩 Structured Output Format
```json
{
  "skills": [],
  "experience_years": 0,
  "education": [],
  "roles": []
}
```

---

## 6. Data Transformation Layer

* Convert JD + CV outputs into comparable schema
* Feature engineering:

  * skill normalization (synonyms → canonical form)
  * skill overlap computation
  * experience normalization (float years)
* Standardization:

  * unify JD and CV feature formats
* Output features:

  * match-ready structured vectors

---

## 7. Scoring Flow

* Matching logic:

  * skill overlap scoring
  * experience alignment scoring
  * keyword relevance scoring
* Score computation:

  * weighted aggregation model
* Weighting:

  * skills → highest weight
  * experience → medium weight
  * keywords/context → lower weight
* Final output:

  * total candidate score

---

## 8. Output Generation Flow

* Ranking:

  * sort candidates by total score (descending)
* Explanation generation:

  * LLM generates reasoning per candidate
* Output structuring:

  * rank
  * score breakdown
  * explanation text
* UI-ready formatting for Streamlit

---

## 9. Component Interaction Sequence

* Streamlit UI collects JD + CVs
* Backend receives request
* JD → LLM extraction module
* CVs → preprocessing → LLM extraction module
* Structured outputs → transformation layer
* Features → scoring engine
* Scores → ranking engine
* Ranking → explanation generator
* Final response → UI renderer

---

## 10. Data Flow Diagram (Text-Based)

```
User Input (JD + CVs)
        ↓
Input Validation Layer
        ↓
Preprocessing Layer
        ↓
LLM Extraction Layer
   ├── JD Extraction
   └── CV Extraction
        ↓
Structured Data Output
        ↓
Data Transformation Layer
        ↓
Feature Engineering Layer
        ↓
Scoring Engine
        ↓
Ranking Engine
        ↓
Explanation Generator (LLM)
        ↓
Streamlit UI Output (Ranked Candidates + Insights)
```
