import google.generativeai as genai
import os
from fastapi import FastAPI
app = FastAPI()

os.environ["API_KEY"] = 'AIzaSyAZfdkmW0ywcJddyFdKX6AbytOkyN2hKOQ'
genai.configure(api_key=os.environ["API_KEY"])

@app.get("/prompt")
def gen_response(guess):
    model = genai.GenerativeModel('gemini-1.5-flash-latest')   
    response = model.generate_content(guess)
    return response.text

guess = "You are a Wolf. Generate a text for a video with 5 minutes about narcissism."
print(gen_response(guess))
