# ✍️ Multi-Agent Social Media Content Generator
## Multi-lingual Support

This project provides a robust, agent-based solution for generating high-quality, platform-specific social media content. By leveraging a high-speed LLM (Groq) orchestrated via LangChain, it tailors posts for Twitter/X, Instagram, Facebook, and LinkedIn, ensuring adherence to strict platform rules, desired tone, and **multi-lingual support**.

## ✨ Core Features

* **Multilingual Output:** Generate content in various languages (English, Spanish, French, German, Japanese, etc.) via a simple dropdown selection in the UI.
* **Platform-Specific Agents:** Dedicated agents enforce unique length, format, and style constraints for each social media platform.
* **Dynamic Tone Control:** A user input field allows setting a custom style (e.g., "Candid and Humble," "Inspiring and Visionary").
* **Professional Validation:** Automatically validates the topic's relevance for LinkedIn using a Pydantic-based classifier, skipping content generation if the topic is deemed non-business/tech related.
* **Unified Hashtag Generation:** Generates exactly three relevant, highly specific hashtags.

---

## ⚙️ Technology Stack

| Technology | Role in Project |
| :--- | :--- |
| **Gradio** | Provides the interactive web interface (UI) for the generator. |
| **LangChain** | Manages the orchestration of LLM calls, prompt templating, and output parsing. |
| **Groq API** | The underlying high-speed LLM service (`llama-3.1-8b-instant`) used for generation and classification. |
| **Pydantic** | Used for structured output to reliably classify topics (e.g., for LinkedIn relevance). |
| **Python OOP** | Implemented dedicated agent classes for modular and maintainable code. |

---

## 🚀 Setup and Installation

### 1. Prerequisites

You must have a **Groq API key** to run this application.

### 2. Install Dependencies

The project dependencies are listed in `requirements.txt`. Run the following command to install them all:

```bash
pip install -r requirements.txt
````

### 3. Configure API Key

The script requires the `GROQ_API_KEY` to be set as an environment variable or loaded via a secrets manager (like Google Colab's `userdata`).

**If running locally,** set the environment variable:

```bash
export GROQ_API_KEY="YOUR_API_KEY_HERE"
```

### 4. Run the Application

You can launch the Content Generator using either a standard terminal (if saved as a `.py` file) or within a notebook environment (`.ipynb`).

#### Option A: Running as a Python Script (`.py`)

If you have downloaded the code as `social_media_content_generator.py`, execute it directly from your terminal:

```bash
python social_media_content_generator.py
```

#### Option B: Running in a Notebook (`.ipynb`)

If you are using Google Colab or Jupyter, simply open the notebook file (`social_media_content_generator.ipynb`) and run all cells sequentially. The interactive Gradio UI will appear embedded in the output.

The application will start and provide a local URL (e.g., `https://localhost:7860/`) to access the content generator in your browser.

-----

## 🛠️ Agent Constraints and Rules

Each agent is programmed with strict rules to maximize platform effectiveness:

| Platform Agent | Specific Rule Enforced |
| :--- | :--- |
| **Twitter/X Agent** | A single, highly engaging hook (under 280 characters). |
| **Instagram Agent** | A fun, two-paragraph caption, separated by a double line break. |
| **Facebook Agent** | A friendly, conversational post (2-3 sentences). |
| **LinkedIn Agent** | A professional, insightful summary (3-4 sentences), subject to topic relevance check. |
| **Hashtag Agent** | Exactly 3 relevant, highly specific hashtags, separated by spaces. |
