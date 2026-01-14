from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

assert os.getenv("HUGGINGFACE_ACCESS_TOKEN"), "Token not loaded"

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=50,
)

print(llm.invoke("What is the capital of India?"))
