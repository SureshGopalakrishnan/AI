"""
Main Entry Point for Resume Screening Project

WHAT:
- Demonstrates the Resume Screening system components.

CURRENT SCOPE:
- Resume Parser Agent
- JD Analyzer Agent

WHY:
- Provides a simple way to run the project, executable entry point
- Hides internal module complexity from users/recruiters
- Useful for demos and portfolio showcase
- Different from tests because it demonstrates workflow, not validation
- Acts as a demo runner (NOT a test)

RUN:
    python main.py
"""

from agents.resume_parser import ResumeParserAgent  # Import the main parsing agent class
from agents.jd_analyzer import JDAnalyzerAgent      # Import the JD analyzer agent class


def main():
    """
    Main function to demonstrate Resume Parser Agent.

    WHAT:
    - Creates sample resume input
    - Calls ResumeParserAgent
    - Prints structured output
    - Creates sample JD input
    - Calls JDAnalyzerAgent
    - Prints structured JD output

    WHY:
    - Gives a quick, clean demo of system capability
    - Avoids requiring users to understand internal structure

    Demonstration workflow.

    Current flow:

    Resume Text
        ↓
    Resume Parser
        ↓
    Structured Candidate Profile

    Job Description
        ↓
    JD Analyzer
        ↓
    Structured Job Requirements
    """

    # -------------------------------------------------------
    # Project Header
    # -------------------------------------------------------
    # WHY:
    # Makes console output easier to read and gives the
    # application a more professional feel.
    project_title = "AI Resume Screening System"

    print("=" * 80)
    print(project_title.center(80))
    print("=" * 80)

    print("[INFO] ===== Resume Screening System Started =====")

    # -------------------------------------------------------
    # Step 1: Prepare Sample Inputs
    # -------------------------------------------------------

    # -------------------------------------------------------
    # Sample Resume Input
    # -------------------------------------------------------
    # NOTE:
    # This is currently hardcoded for demonstration purposes.
    #
    # FUTURE:
    # This input may come from:
    # - PDF Upload
    # - Streamlit UI
    # - REST API
    # - Database
    # -------------------------------------------------------
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

    # -------------------------------------------------------
    # Sample Job Description Input
    # -------------------------------------------------------
    # NOTE:
    # This is currently hardcoded for demonstration purposes.
    #
    # FUTURE:
    # This input may come from:
    # - Recruiter UI
    # - Job Board Integration
    # - API Request
    # - Database
    # -------------------------------------------------------
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

    print("[INFO] Sample job description prepared")

    try:
        # ===================================================
        # RESUME PARSING SECTION
        # ===================================================
        section_title = "RESUME PARSER AGENT"

        print("\n" + "=" * 80)
        print(section_title.center(80))
        print("=" * 80)

        # ---------------------------------------------------
        # Step 2: Initialize Resume Parser Agent
        # ---------------------------------------------------
        # WHY:
        # Creates the agent responsible for converting
        # raw resume text into structured candidate data.
        print("[INFO] Initializing Resume Parser Agent...")
        resume_agent = ResumeParserAgent()

        # ---------------------------------------------------
        # Step 3: Parse Resume
        # ---------------------------------------------------
        # WHY:
        # Sends the resume text through:
        #
        # Text Cleaning
        #     ↓
        # Prompt Building
        #     ↓
        # LLM Extraction
        #     ↓
        # JSON Parsing
        #     ↓
        # Pydantic Validation
        #
        # Result:
        # Structured Candidate Profile
        print("[INFO] Parsing resume...")
        candidate_profile = resume_agent.parse(sample_resume)  # Call the parsing method with the sample resume 

        # ---------------------------------------------------
        # Step 4: Display Resume Output
        # ---------------------------------------------------
        print("\n[INFO] ===== Parsed Candidate Profile =====")

        # IMPORTANT:
        # Using Pydantic v2 method (model_dump_json)
        print(candidate_profile.model_dump_json(indent=2))

        # ===================================================
        # JOB DESCRIPTION ANALYSIS SECTION
        # ===================================================
        section_title = "JD ANALYZER AGENT"

        print("\n" + "=" * 80)
        print(section_title.center(80))
        print("=" * 80)


        # ---------------------------------------------------
        # Step 5: Initialize JD Analyzer Agent
        # ---------------------------------------------------
        # WHY:
        # Creates the agent responsible for converting
        # raw job descriptions into structured hiring
        # requirements.
        print("[INFO] Initializing JD Analyzer Agent...")
        jd_agent = JDAnalyzerAgent()

        # ---------------------------------------------------
        # Step 6: Analyze Job Description
        # ---------------------------------------------------
        # WHY:
        # Sends the JD through:
        #
        # Text Cleaning
        #     ↓
        # Prompt Building
        #     ↓
        # LLM Extraction
        #     ↓
        # JSON Parsing
        #     ↓
        # Pydantic Validation
        #
        # Result:
        # Structured Hiring Requirements
        print("[INFO] Parsing job description...")
        jd_requirements = jd_agent.parse(sample_jd)

        # ---------------------------------------------------
        # Step 7: Display JD Output
        # ---------------------------------------------------
        print("\n[INFO] ===== Parsed Job Requirements =====")

        print(jd_requirements.model_dump_json(indent=2))

        # ===================================================
        # DEMO COMPLETION
        # ===================================================
        print("\n" + "=" * 80)
        print("[INFO] Resume Screening Demo Completed Successfully")
        print("=" * 80)
    except Exception as e:
        # ---------------------------------------------------
        # Global Error Handling
        # ---------------------------------------------------
        # WHY:
        # Ensures clean failure instead of crash
        # Prevents unexpected crashes from terminating the
        # application without useful information.
        #
        # In a production system, this would be replaced with
        # proper application logging.
        print(f"[ERROR] Application Failed: {str(e)}")

# -------------------------------------------------------
# Entry Point Guard
# -------------------------------------------------------
# WHY:
# Ensures this file runs only when executed directly
# (not when imported as a module)
#
# Example:
#     python main.py
#
# Prevents accidental execution when imported by another
# module.
# -------------------------------------------------------


if __name__ == "__main__":
    main()
