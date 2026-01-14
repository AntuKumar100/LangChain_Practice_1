import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create embedding
result = genai.embed_content(
    model="models/text-embedding-004",
    content="Dhaka is the capital of Bangladesh."
)

# Print embedding vector
print(result["embedding"])