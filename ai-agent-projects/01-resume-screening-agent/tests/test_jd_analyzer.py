"""
Test Script for JD Analyzer Agent

WHAT:
- Provides isolated testing for JD Analyzer Agent

WHY:
- Helps validate extraction logic independently
- Makes debugging easier
- Ensures agent works before integrating into pipeline

HOW TO RUN:

From project root:

python -m tests.test_jd_analyzer
"""

from agents.jd_analyzer import JDAnalyzerAgent  # Import the main parsing agent class


def run_test():
    """
    Runs a simple JD parsing test.

    WHY:
    - Allows quick validation during development
    - Simulates real-world JD input
    """

    print("[INFO] Starting JD Analyzer Test...")

    # ----------------------------------------
    # Sample Job Description Input
    # ----------------------------------------
    # This sample intentionally contains:
    # - required skills
    # - nice-to-have skills
    # - experience
    # - education
    #
    # WHY:
    # Helps validate structured extraction behavior
    sample_jd = """
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
    """
    # ----------------------------------------

    try:
        # ----------------------------------------
        # Initialize Agent
        # ----------------------------------------
        print("[INFO] Initializing JDAnalyzerAgent...")
        agent = JDAnalyzerAgent()  # Creates a new instance (loads LLM service internally)

        # ----------------------------------------
        # Parse JD
        # ----------------------------------------
        print("[INFO] Parsing sample JD...")
        result = agent.parse(sample_jd)  # Executes the full extraction pipeline → returns JDRequirements object

        # ----------------------------------------
        # Print Structured Output
        # ----------------------------------------
        print("[INFO] Parsed JD Output:")

        # model_dump_json() is the recommended
        # Pydantic v2 method for serializing models to JSON
        # indent=2 makes output human-readable with 2-space indentation
        print(result.model_dump_json(indent=2))

        print("[INFO] JD Analyzer Test Completed Successfully")
    except Exception as e:
        # ----------------------------------------
        # Catch unexpected test-level failures
        # ----------------------------------------
        # Logs any error that occurs during test execution (e.g., missing API key, network issues)
        print(f"[ERROR] JD Analyzer Test Failed: {str(e)}")


# --------------------------------------------------
# Standard Python Entry Point
# --------------------------------------------------
# WHY:
# Allows file to be run directly (python test_jd_analyzer.py) or
# via module mode (python -m tests.test_jd_analyzer)
if __name__ == "__main__":
    run_test()  # Execute the test function only when this script is run directly
