from agents.resume_parser import ResumeParserAgent  # Import the main parsing agent class


def run_test():
    """
    PURPOSE:
    Simple end-to-end test to verify pipeline execution.

    WHY SIMPLE TEST:
    - Focus is on flow correctness, not LLM accuracy
    - In real systems, LLM would be mocked in unit tests
    """

    print("[INFO] Starting Resume Parser Test...")

    # Sample resume text (could be more complex in real tests)
    # Contains typical sections: name, contact, experience, education, skills
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

    # Instantiate the parser (reads API key from env internally)
    agent = ResumeParserAgent()

    # Run the full extraction pipeline → returns CandidateProfile object
    result = agent.parse(sample_resume)

    # Serialize the Pydantic model to formatted JSON string for readable output
    print("[INFO] Parsed Candidate Profile:")
    print(result.model_dump_json(indent = 2))


if __name__ == "__main__":
    # Execute test only when script is run directly (not imported as module)
    run_test()
