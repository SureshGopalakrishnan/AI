# 🧠 AI & Generative Solutions Portfolio
### Collection of AI Projects / Demos

This repository serves as a collection of self-contained projects demonstrating proficiency in developing applications powered by Artificial Intelligence (AI) models, focusing on the integration of large language models (LLMs) and generative services.

All projects are designed for clarity, utilizing **minimal Python dependencies** to showcase clean, efficient implementation, and direct API interaction.

---

## 📂 Project Index

| Folder | Title & Description | Core Technologies | Status |
| :--- | :--- | :--- | :--- |
| **`content-generator`** | **Multi-Agent Social Media Content Generator:** A Gradio web app using an agent-based architecture to produce platform-optimized, multilingual content (Twitter/X, LinkedIn, etc.) based on a single topic, tone and language input. Includes Pydantic-driven professional validation. | Python, Gradio, LangChain, Groq API, Pydantic (Structured Output) | Proof of Concept |

---

## ⚙️ Technical Approach & Environment

Each project is designed to be fully self-contained in its subdirectory.

### Key Principles

* **Isolated Environments:** Each project folder contains its own specific dependencies (if any) and a dedicated **`requirements.txt`** file.
* **Production Focus:** Demonstrations prioritize clean API integration, secure key handling (as variables/placeholders), and robust error messaging.
* **Minimalism:** Front-end projects are built using single-file HTML/JS/CSS (Tailwind) to ensure the core focus remains on the AI logic.

### Running a Project Locally

1.  Navigate to the specific project directory:
    ```bash
    cd [folder-name]
    ```
2.  Install dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```
3.  Set up your API Key:
    * **Crucially, do not commit your API key.** Set your API key as an environment variable (ex. `GROQ_API_KEY`).
4.  Execute the project following its internal `README.md`.
