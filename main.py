from fastapi import FastAPI
from pydantic import BaseModel
import requests
import google.generativeai as genai
from googletrans import Translator  

app = FastAPI()
translator = Translator()

@app.get("/")
def read_root():
    return {"welcome": "Welcome to the Translation System API!"}

#Gemini API
API_KEY = "AIzaSyBHO7GVuWHSKSbOlOtW1Lzy4r2atRj4W2g"  
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")  

#request model
class RequestData(BaseModel):
    text: str
    source_lang: str
    target_lang: str='en'

#call the LLM API
def query_llm(input_text: str) -> str:
    try:
        llm_prompt = f"Provide a brief yet informative response (2-3 sentences) to the following:\n\n{input_text}"
        response = model.generate_content(llm_prompt)
        return response.text.strip() if response.text else "I'm sorry, I couldn't process your request."
    
    except Exception as e:
        print("LLM API Error:", str(e))
        return "An error occurred while processing your request."
#Translation & LLM Processing
@app.post("/translate_process/")
def process_text(data: RequestData):
    try:
        #Translate Local Language → English
        english_text = translator.translate(data.text, src=data.source_lang, dest="en").text
        print("Translated to English:", english_text)

        #Send to LLM API
        llm_response = query_llm(english_text)
        print("LLM Response:", llm_response)

        #Translate LLM Response → Local Language
        final_response = translator.translate(llm_response, src="en", dest=data.source_lang).text
        print("Final Translated Response:", final_response)

        return {"response": final_response}

    except Exception as e:
        return {"error": str(e)}