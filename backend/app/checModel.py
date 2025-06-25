# check_models.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables (GOOGLE_API_KEY)
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

print("Available models that support 'generateContent':")

for m in genai.list_models():
  # We check if 'generateContent' is a supported method for the model
  if 'generateContent' in m.supported_generation_methods:
    print(f" - {m.name}")