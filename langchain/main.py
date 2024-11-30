import google.generativeai as genai
genai.configure(api_key='AIzaSyAZfdkmW0ywcJddyFdKX6AbytOkyN2hKOQ')

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("What is LangChain?")
print(response.text)