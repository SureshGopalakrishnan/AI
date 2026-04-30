import os                       # Provides functions to interact with the operating system, like reading environment variables
from openai import OpenAI       # Official OpenAI client library for v1.x+ API
from dotenv import load_dotenv  # Loads environment variables from a .env file into os.environ

# Load environment variables from .env file
load_dotenv()


class LLMService:
    """
    PURPOSE:
    Centralized LLM communication layer.

    WHY THIS DESIGN:
    - Keeps agent logic clean
    - Makes LLM interchangeable (OpenAI → Azure → Claude later)
    - Central place for debugging API issues
    """
    def __init__(self):
        # Initialize OpenAI client with API key from environment variable
        print("[INFO] Initializing LLM Service...")
        
        # Retrieve the API key string from environment variables (set by load_dotenv or system)
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        # Guard clause: warn if key is missing but don't crash immediately (graceful degradation)
        if not self.api_key:
            print("[WARNING] OPENAI_API_KEY not found in environment variables. LLM calls will fail.")
        else:
            print("[INFO] OPENAI_API_KEY loaded successfully.")
        
        # Create the OpenAI client instance using the API key (client will be used for all API calls)
        self.client = OpenAI(api_key = self.api_key)
        
    def extract_structured_data(self, prompt: str) -> str:
        """
        PURPOSE:
        Send prompt to LLM and get structured response.
        
        WHY THIS METHOD:
        - Abstracts away API call details
        - Can be extended for retries, error handling, or different LLMs in the future
        
        WHY TEMPERATURE = 0:
        - We want deterministic JSON output
        - Reduces randomness in structured extraction
        """
        print("[INFO] Sending request to LLM...")
        print("[DEBUG] Prompt length:", len(prompt))
        
        # If no API key was loaded, fail early without attempting the API call
        if not self.api_key:
            print("[ERROR] Cannot call LLM without API key")
            return ""
        
        try:
            # Make the chat completion request using the OpenAI client
            response = self.client.chat.completions.create(
                                                            model    = "gpt-4o-mini", # Fast, cost‑efficient model suitable for extraction
                                                            messages = [ 
                                                                         {
                                                                           "role"    : "system",
                                                                           "content" : ( 
                                                                                         "You are a strict resume parsing engine. "
                                                                                         "Return ONLY valid JSON. No explanations."
                                                                                       )
                                                                         }, # System prompt enforces JSON‑only output
                                                                         { 
                                                                           "role"    : "user",
                                                                           "content" : prompt  # The cleaned resume text or extraction prompt
                                                                         }
                                                                       ],
                                                            temperature = 0   # Deterministic output – same input → same output
                                                           )
            
            # Extract the textual content from the first choice (there is only one)
            result = response.choices[0].message.content
            
            print("[INFO] LLM response received successfully")
            print("[DEBUG] Raw LLM response preview:", result[:200])  # Print only first 200 chars to avoid clutter
            
            return result
        except Exception as e:
            print(f"[ERROR] LLM API call failed: {str(e)}")

            # SAFE FALLBACK
            # Return empty JSON prevents downstream/full pipeline crashes and allows for graceful degradation
            # (e.g., candidate gets 0 score instead of system failure)
            return "{}"
