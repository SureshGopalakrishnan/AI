import re  # regular expression operations for pattern matching and text cleaning


def clean_resume_text(text: str) -> str:
    """
    PURPOSE:
    Cleans and normalizes resume text for better parsing before sending to LLM.

    WHY IMPORTANT:
    - PDFs may introduce noise (extra spaces, line breaks)
    - Resumes can have inconsistent formatting, extra whitespace, and special characters.
    - Cleaning helps improve the accuracy of information extraction and reduces hallucination risk in downstream agents.

    STEPS:
    1. Remove multiple new lines and tabs, replace with single space.
    2. Normalize whitespace (convert multiple spaces/newlines to single space).
    2. Remove non-ASCII characters (optional, depends on use case).
    3. Standardize common delimiters (e.g., replace tabs with spaces).
    4. Trim leading/trailing whitespace.
    """
    print("[DEBUG] Starting resume text cleaning...")

    try:
        # Guard clause: Reject empty or non‑string inputs early
        if not text or not isinstance(text, str):
            print("[ERROR] Invalid input type for resume text")
            return ""
        
        # Replace multiple consecutive newlines with a single newline
        text = re.sub(r'\n+', '\n', text)

        # Replace tabs with spaces (tabs often cause alignment issues)
        text = re.sub(r'\t+', ' ', text)

        # Collapse any whitespace sequence (spaces, newlines, tabs) into a single space
        cleaned_text = re.sub(r'\s+', ' ', text)
        
        # Remove non-ASCII characters (optional)
        # cleaned_text = re.sub(r'[^\x00-\x7F]+', '', cleaned_text)
        
        # Explicitly replace any remaining tabs with spaces (redundant but safe)
        cleaned_text = cleaned_text.replace('\t', ' ')
        
        # Remove leading and trailing whitespace
        cleaned_text = cleaned_text.strip()
        
        print("[INFO] Resume text cleaned successfully")
        print(f"[DEBUG] Cleaned text length: {len(cleaned_text)} characters")

        return cleaned_text
    except Exception as e:
        # If any unexpected error occurs, log it and return original text as fallback
        print(f"[ERROR] Failed while cleaning resume text: {str(e)}")
        return text  # Fallback to original text for safety
