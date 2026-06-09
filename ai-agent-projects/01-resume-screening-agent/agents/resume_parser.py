import json                                           # Standard library for parsing and generating JSON data (handles LLM responses)
from models.candidate_schema import CandidateProfile  # Pydantic model defining the structure of extracted candidate data
from services.llm_service import LLMService           # Wrapper class for OpenAI API calls (handles prompt sending and response parsing)
from utils.text_cleaner import clean_text             # Function to normalize resume text (removes extra whitespace, special characters)


class ResumeParserAgent:
    """
    PURPOSE:
    Main agent that converts raw CV text → structured candidate profile.

    WHY THIS IS AN AGENT:
    - Encapsulates reasoning + LLM + validation
    - Acts as reusable component in multi-agent system later
    """

    def __init__(self, llm_service: LLMService | None = None):
        """
        Initialize LLM service.

        WHY:
        - Keeps LLM logic centralized
        - Makes agent clean and reusable
        """
        print("[INFO] Initializing ResumeParserAgent...")

        # Use provided service OR create default instance
        self.llm_service = llm_service if llm_service is not None else LLMService() # Instantiates a LLMService (reads API key from env)

    def _build_prompt(self, resume_text: str) -> str:
        """
        PURPOSE:
        Create strict instruction prompt for LLM to extract structured data from the resume text.

        The prompt includes instructions for the LLM to return data in a specific JSON format
        that matches the CandidateProfile schema.

        WHY THIS PROMPT DESIGN:
        - Forces JSON-only output (reduces parsing errors)
        - Defines schema explicitly (reduces hallucination)
        - Helps downstream parsing reliability
        """

        print("[DEBUG] Building LLM prompt...")

        # Multi-line f-string containing the full system instruction and user prompt
        # The placeholder {resume_text} will be replaced with the cleaned resume content
        prompt = f"""
You are an expert resume parsing system.

IMPORTANT RULES:
- Return ONLY valid JSON
- Do NOT include explanations
- Use null if data is missing
- Ensure output strictly follows schema

OUTPUT FORMAT:
{{
  "full_name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "experience": [
    {{
      "company": "",
      "role": "",
      "duration": "",
      "responsibilities": []
    }}
  ],
  "education": [
    {{
      "institution": "",
      "degree": "",
      "year": ""
    }}
  ],
  "summary": ""
}}

RESUME:
{resume_text}
"""

        print("[INFO] Prompt built successfully")
        return prompt

    def parse(self, resume_text: str) -> CandidateProfile:
        """
        PURPOSE:
        Main method to parse raw resume text into a CandidateProfile object.

        STEPS:
        1. Input validation - Validate and preprocess the input resume text
        2. Clean Text       - Clean the resume text for better LLM understanding
        3. Build Prompt     - Build the prompt with instructions and cleaned resume
        4. Call LLM         - Call the LLM service to get the response
        5. Parse JSON       - Parse the JSON response into a CandidateProfile object
        6. Validate Schema  - Validate the parsed data against the CandidateProfile schema

        WHY THIS APPROACH:
        - Cleaning improves LLM accuracy
        - Structured prompt reduces hallucination
        - Using Pydantic model ensures data integrity
        """

        print("[INFO] ===== RESUME PARSING STARTED =====")

        try:
            # -----------------------------
            # STEP 1: Input Validation
            # -----------------------------
            # Guard clause: reject empty or non‑string inputs early
            if not resume_text or not isinstance(resume_text, str):
                print("[ERROR] Empty resume input received")
                raise ValueError("Invalid Input: Resume text must be a non-empty string")
            
            print("[DEBUG] Raw resume input received")

            # -----------------------------
            # STEP 2: Clean Text
            # -----------------------------
            # Remove noise (extra spaces, newlines, non‑ASCII if configured)
            cleaned_text = clean_text(resume_text)
            print("[DEBUG] Cleaned resume preview:", cleaned_text[:150])  # Log only first 150 chars for brevity

            # -----------------------------
            # STEP 3: Build Prompt
            # -----------------------------
            # Inject the cleaned text into the instruction template
            prompt = self._build_prompt(cleaned_text)
            print("[DEBUG] Built prompt")

            # -----------------------------
            # STEP 4: Call LLM
            # -----------------------------
            # Call LLM service with the built prompt; returns JSON string from GPT
            llm_response = self.llm_service.extract_structured_data(prompt)

            print("[DEBUG] LLM raw response received")

            # -----------------------------
            # STEP 5: Parse JSON Safely
            # -----------------------------
            # Convert LLM response string to Python dict; catch malformed JSON
            try:
                response_data = json.loads(llm_response)
                print("[DEBUG] LLM response parsed as JSON")
            except json.JSONDecodeError as e:
                print("[ERROR] Failed to parse LLM response as JSON:", e)
                print("[DEBUG] Raw response:", llm_response)
                raise ValueError("Invalid JSON returned by LLM")

            # -----------------------------
            # STEP 6: Validate Schema
            # -----------------------------
            # Pydantic will validate types and required fields; raises exception if invalid
            candidate_profile = CandidateProfile(**response_data)
            print("[INFO] Resume parsing completed successfully")

            print("[INFO] ===== RESUME PARSING END =====")

            return candidate_profile
        except Exception as e:
            print(f"[ERROR] Resume parsing failed: {str(e)}")

            # SAFE FALLBACK OBJECT
            # Return an empty CandidateProfile (all fields None or empty) to prevent pipeline crash
            # Downstream agents can treat this as a candidate with zero score
            return CandidateProfile()
