# 🧠 Resume Screening Agent — Agent Workflow Design

---

## 1. Overview of Agent Workflow

* System uses multiple specialised AI agents to break down resume screening into structured reasoning steps
* Each agent handles a single responsibility (modular reasoning)
* Workflow enables:

  * multi-step reasoning instead of single LLM call
  * improved accuracy and interpretability
  * easier debugging and traceability

---

## 2. Agent Architecture Style

* Uses **LangGraph-style stateful orchestration**
* Core principles:

  * Shared global state passed between agents
  * Node-based execution model
  * Directed edges define workflow transitions
* Execution model:

  * sequential pipeline for dependency-heavy steps
  * conditional branching for failure handling
  * optional parallel execution for CV processing

---

## 3. Agent List and Responsibilities

### 📄 JD Analyzer Agent

* Extracts structured job requirements
* Outputs:

  * required_skills
  * preferred_skills
  * experience level
  * role/domain

---

### 📑 Resume Parser Agent

* Extracts structured candidate profile from CV
* Outputs:

  * skills
  * experience
  * education
  * roles

---

### 🔗 Skill Matching Agent

* Compares JD vs CV skills
* Computes:

  * skill overlap
  * missing skills
  * skill relevance score

---

### 📊 Scoring Agent

* Computes final candidate score
* Uses weighted scoring:

  * skills
  * experience
  * optional semantic similarity

---

### 💡 Explanation Agent

* Generates human-readable reasoning
* Outputs:

  * strengths
  * gaps
  * justification of score

---

### 🏆 Ranking Agent

* Sorts candidates based on final score
* Assigns rank order

---

## 4. State Definition (VERY IMPORTANT)

```json id="st9kq1"
{
  "jd": {},
  "cvs": [],
  "extracted_jd": {},
  "extracted_cvs": [],
  "scores": [],
  "ranked_candidates": []
}
```

### 🧾 Field Explanation

* `jd`: raw job description input
* `cvs`: uploaded CV files
* `extracted_jd`: structured JD output from JD Analyzer Agent
* `extracted_cvs`: structured candidate profiles from Resume Parser Agent
* `scores`: computed scoring results per candidate
* `ranked_candidates`: final ordered list after ranking

### 🔄 State Evolution

* Each agent reads state → updates specific fields → passes to next agent

---

## 5. Agent Execution Flow (Step-by-Step)

* Step 1: JD input → JD Analyzer Agent
* Step 2: CV upload → Resume Parser Agent
* Step 3: Skill Matching Agent processes extracted outputs
* Step 4: Scoring Agent computes candidate scores
* Step 5: Explanation Agent generates reasoning per candidate
* Step 6: Ranking Agent produces final ordered list

---

## 6. Conditional Logic & Decision Points

* If JD is incomplete:

  * trigger re-processing in JD Analyzer Agent
  * fallback to rule-based extraction

* If CV parsing fails:

  * retry parsing once
  * if failure persists → mark candidate as invalid

* If extracted data is noisy:

  * apply normalization layer before scoring

* Retry Strategy:

  * max 2 retries per agent
  * fallback to heuristic extraction if LLM fails

---

## 7. Agent Interaction Diagram (Text-Based)

```text id="ag9xk1"
JD Input → JD Analyzer Agent
              ↓
        Structured JD
              ↓
CV Input → Resume Parser Agent
              ↓
     Structured CVs
              ↓
     Skill Matching Agent
              ↓
       Scoring Agent
              ↓
     Explanation Agent
              ↓
      Ranking Agent
              ↓
     Final Output (UI)
```

---

## 8. Why Agentic Design is Used

* Avoids single large LLM dependency
* Improves modularity and maintainability
* Enables step-by-step debugging of decisions
* Increases explainability for HR use cases
* Allows independent scaling of components
* Supports future extension (feedback loops, learning systems)

---

## 9. Failure Handling Strategy

* Agent-level retries (max 2 attempts)
* Graceful degradation:

  * fallback to rule-based extraction if LLM fails
* Partial execution support:

  * process valid CVs even if some fail
* Error logging per agent in shared state
* Isolation of failures (one CV failure does not break pipeline)
