"""
JD Schema Definition

WHAT:
Defines structured output format for Job Description parsing.

WHY:
- Ensures consistent structure from LLM output
- Enables validation using Pydantic
- Acts as contract between JD Analyzer and downstream agents (scoring, ranking)

IMPORTANT DESIGN CHOICES:
- Use Optional fields to tolerate incomplete JD data
- Use Field(default_factory=list) to avoid mutable default issues
- Keep schema simple and extensible (avoid over-engineering)
"""

from pydantic import BaseModel, Field  # BaseModel is used to define data models; Field allows extra validation/config
from typing import List, Optional      # List for arrays/lists, Optional for nullable (can be None) fields


class JDRequirements(BaseModel):
    """
    Represents structured job description requirements.

    This is the final output of the JD Analyzer Agent.
    """
    # -------------------------------
    # Basic Job Info
    # -------------------------------
    # WHY Optional:
    # Not all JDs explicitly mention job title in clean format
    job_title: Optional[str] = None  # e.g., "Software Engineer", "Data Scientist"

    # -------------------------------
    # Skills
    # -------------------------------
    # WHY separate required vs nice-to-have:
    # This is critical for scoring logic later
    required_skills: List[str] = Field(default_factory=list)      # e.g., ["Python", "Machine Learning"]
    nice_to_have_skills: List[str] = Field(default_factory=list)  # e.g., ["Docker", "Kubernetes"]

    # -------------------------------
    # Experience
    # -------------------------------
    # WHY Optional[int]:
    # Some JDs say "3+ years", some say "senior-level"
    # We will try to extract numeric value where possible
    min_experience_years: Optional[int] = None  # Minimum years of experience required (e.g., 3, 5, 0 for entry-level)

    # -------------------------------
    # Education
    # -------------------------------
    education_requirements: Optional[str] = None  # e.g., "Bachelor's degree in Computer Science"

    # -------------------------------
    # Responsibilities
    # -------------------------------
    # WHY list:
    # Useful for explainability and matching later
    responsibilities: List[str] = Field(default_factory=list)  # Key job duties extracted from JD (e.g., "Develop software", "Collaborate with team")

    # -------------------------------
    # Summary (optional enhancement)
    # -------------------------------
    # WHY:
    # Helpful for UI display later
    role_summary: Optional[str] = None  # e.g., "We are looking for a Software Engineer to join our team and work on cutting-edge AI projects."
