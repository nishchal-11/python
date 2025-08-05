import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

google_api_key=os.getenv("google_api_key")
# pip install google-generativeai
# Configure the Gemini API
genai.configure(api_key=google_api_key)

# Create the model
model = genai.GenerativeModel('gemini-2.0-flash')

# Create the prompt combining system and user messages
prompt = """You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud.

User: what is coding"""

# Generate response
response = model.generate_content(prompt)

print(response.text)