"""
JD Analyzer Agent

WHAT:
- Parses raw Job Description text
- Extracts structured hiring requirements using LLM

WHY:
- Converts unstructured JD into machine-readable format
- Enables scoring & ranking in later stages

DESIGN PRINCIPLES:
- Reuse existing LLM service
- Strong logging for debugging
- Graceful failure handling
"""

import json
from typing import Any
from urllib import response

from models.jd_schema import JDRequirements  # Import the structured schema for JD requirements
from services.llm_service import LLMService  # Import the LLM service for parsing JDs
from utils.text_cleaner import clean_text    # Utility to clean raw JD text


class JDAnalyzerAgent:
    """
    Agent responsible for analyzing Job Descriptions.
    """

    def __init__(self, llm_service: LLMService | None = None):
        """
        Initialize LLM service.

        WHY:
        - Keeps LLM logic centralized
        - Makes agent clean and reusable
        """
        print("[INFO] Initializing JDAnalyzerAgent...")

        # Use provided service OR create default instance
        self.llm_service = llm_service if llm_service is not None else LLMService()  # Instantiates a LLMService (reads API key from env)

    def parse(self, jd_text: str) -> JDRequirements:
        """
        Main method to parse JD text.

        STEPS:
        1. Input validation - Validate and preprocess the input JD text
        2. Clean Text       - Clean the JD text for better LLM understanding
        3. Build Prompt     - Build the prompt with instructions and cleaned JD
        4. Call LLM         - Call the LLM service to get the response
        5. Parse JSON       - Parse the JSON response into a JDRequirements object
        6. Validate Schema  - Validate the parsed data against the JDRequirements schema
        RETURNS:
        - JDRequirements object
        """
        
        print("[INFO] JD ANALYSIS STARTED")

        try:
            # -------------------------------
            # Step 1: Input validation
            # -------------------------------
            # Guard clause: reject empty or non‑string inputs early
            if not jd_text or not isinstance(jd_text, str):
                raise ValueError("Invalid JD input: must be non-empty string")
            
            print("[DEBUG] Raw JD input received")

            # -------------------------------
            # Step 2: Clean text
            # -------------------------------
            # Remove noise (extra spaces, newlines, non‑ASCII if configured)
            cleaned_text = clean_text(jd_text)

            print(f"[DEBUG] Cleaned JD length: {len(cleaned_text)}")
            print(f"[DEBUG] JD preview: {cleaned_text[:150]}")

            # -------------------------------
            # Step 3: Build prompt
            # -------------------------------
            # Inject the cleaned text into the instruction template
            prompt = self._build_prompt(cleaned_text)

            print("[INFO] Prompt built successfully")
            print(f"[DEBUG] Prompt length: {len(prompt)}")
            
            # -------------------------------
            # Step 4: Call LLM
            # -------------------------------
            # Call LLM service with the built prompt; returns JSON string from GPT
            print("[INFO] Sending request to LLM...")
            
            llm_response = self.llm_service.extract_structured_data(prompt)

            print("[DEBUG] LLM raw response received")
            print(f"[DEBUG] Raw response preview: {llm_response[:200]}")

            # -------------------------------
            # Step 5: Parse JSON
            # -------------------------------
            # Convert LLM response string to Python dict; catch malformed JSON
            try:
                response_data = json.loads(llm_response)
                print("[DEBUG] LLM response parsed as JSON")
            except json.JSONDecodeError as e:
                print("[ERROR] Failed to parse LLM response as JSON:", e)
                print("[DEBUG] Raw response:", llm_response)
                raise ValueError("Invalid JSON returned by LLM")
            
            # -------------------------------
            # Step 6: Validate schema
            # -------------------------------
            # Pydantic will validate types and required fields; raises exception if invalid
            try:
                jd_obj = JDRequirements(**response_data)
                print("[INFO] JD successfully validated")
                return jd_obj
            except Exception as e:
                print(f"[ERROR] Schema validation failed: {str(e)}")
                return JDRequirements()
        except Exception as e:
            print(f"[ERROR] JD analysis failed: {str(e)}")

            # SAFE FALLBACK OBJECT
            # Return an empty JDRequirements (all fields None or empty) to prevent pipeline crash
            # Downstream agents can treat this as a JD with zero match score
            return JDRequirements()

    def _build_prompt(self, jd_text: str) -> str:
        """
        Builds prompt for LLM extraction.

        WHY structured prompt:
        - Forces consistent JSON output
        - Reduces hallucination
        - Improves parsing reliability
        """

        return f"""
You are an expert HR system.

Extract structured information from the following Job Description.

Return ONLY valid JSON. No explanation.

Required JSON format:

{{
  "job_title": "string",
  "required_skills": ["string"],
  "nice_to_have_skills": ["string"],
  "min_experience_years": number,
  "education_requirements": "string",
  "responsibilities": ["string"],
  "role_summary": "string"
}}

RULES:
- Extract skills into required vs nice-to-have if possible
- Convert experience into integer (e.g., "3+ years" → 3)
- If not found, return null or empty list
- Do NOT include extra fields
- Output must be valid JSON

Job Description:
\"\"\"
{jd_text}
\"\"\"
"""
