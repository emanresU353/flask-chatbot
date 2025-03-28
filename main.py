import google.generativeai as genai 
import os 
from flask import Flask, render_template, request 
from dotenv import load_dotenv 

load_dotenv() 

app = Flask(__name__) 

# Set up Gemini API 
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) 

@app.route("/") 
def index(): 
  return render_template("index.html") 
  
@app.route("/ask", methods=["POST"]) 
def ask(): 
  user_message = request.form["message"] 
  
  try: # Replace "gemini-pro" with the correct model name from Step 2 
    model = genai.GenerativeModel("gemini-2.0-flash") 
    response = model.generate_content(user_message) 
    return response.text # Return AI response 
  except Exception as e: 
    return f"❌ Error: {str(e)}" 
    
if __name__ == "__main__": 
  app.run(host="0.0.0.0", port=8080, debug=True)