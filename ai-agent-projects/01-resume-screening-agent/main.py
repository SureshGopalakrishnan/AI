"""
Main entry point for Resume Screening Agent (Resume Parser only for now)

WHY THIS FILE EXISTS:
- Provides a simple way to run the project
- Hides internal module complexity from users/recruiters
- Acts as a demo runner (NOT a test)

HOW TO RUN:
    python main.py
"""

from agents.resume_parser import ResumeParserAgent  # Import the main parsing agent class


def main():
    """
    Main function to demonstrate Resume Parser Agent.

    WHAT:
    - Creates sample resume input
    - Calls ResumeParserAgent
    - Prints structured output

    WHY:
    - Gives a quick, clean demo of system capability
    - Avoids requiring users to understand internal structure
    """

    print("[INFO] ===== Resume Screening System Started =====")

    # -------------------------------
    # Step 1: Sample Resume Input
    # -------------------------------
    # NOTE:
    # In real usage, this would come from:
    # - file upload (PDF)
    # - API request
    # - database
    sample_resume = """
    Suresh Gopalakrishnan
    suresh.gopalakrishnan@email.com | +44 7123456789

    Experience:
    Software Engineer at Google (2020-2023)
    - Built scalable backend systems
    - Worked on distributed systems

    Education:
    BSc Computer Science, University of Oxford, 2020

    Skills:
    Python, Machine Learning, Distributed Systems
    """

    print("[INFO] Sample resume prepared")

    try:
        # -------------------------------
        # Step 2: Initialize Agent
        # -------------------------------
        print("[INFO] Initializing Resume Parser Agent...")
        agent = ResumeParserAgent()

        # -------------------------------
        # Step 3: Parse Resume
        # -------------------------------
        print("[INFO] Parsing resume...")
        result = agent.parse(sample_resume)

        # -------------------------------
        # Step 4: Output Result
        # -------------------------------
        print("\n[INFO] ===== Parsed Candidate Profile =====")

        # IMPORTANT:
        # Using Pydantic v2 method (model_dump_json)
        print(result.model_dump_json(indent=2))
    except Exception as e:
        # -------------------------------
        # Error Handling
        # -------------------------------
        # WHY:
        # Ensures clean failure instead of crash
        print(f"[ERROR] Failed to run Resume Parser: {str(e)}")


# -------------------------------
# Entry Point Guard
# -------------------------------
# WHY:
# Ensures this file runs only when executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()
