from pydantic import BaseModel, Field  # BaseModel is used to define data models; Field allows extra validation/config
from typing import List, Optional      # List for arrays/lists, Optional for nullable (can be None) fields


class Experience(BaseModel):
    """
    WHY: We separate experience into a structured object so we can later
    score candidates based on company, role, and responsibilities.
    """
    company: Optional[str] =  None                             # Can be missing/None; default None avoids empty string
    role: Optional[str] = None
    duration: Optional[str] = None
    responsibilities: List[str] = Field(default_factory=list)  # Pydantic creates a new list per instance (safe, unlike plain Python)


class Education(BaseModel):
    """
    WHY: Education is separated so we can evaluate academic relevance later
    (useful for filtering candidates in scoring agent).
    """
    institution: Optional[str] = None
    degree: Optional[str] = None
    year: Optional[str] = None  # Kept as string (e.g., "2020" or "2020-2024")


class CandidateProfile(BaseModel):
    """
    CORE OUTPUT SCHEMA

    WHY THIS EXISTS:
    - Converts unstructured CV → structured data
    - Enables ranking/scoring in downstream agents
    - Ensures consistency across all resumes
    """
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    
    skills: List[str] = Field(default_factory=list)             # List of technical skills as strings
    experience: List[Experience] = Field(default_factory=list)  # Currently raw text strings, not Experience objects (design choice)
    education: List[Education] = Field(default_factory=list)    # Currently raw strings, not Education objects (simpler extraction)

    summary: Optional[str] = None  # Free-text summary extracted from CV
