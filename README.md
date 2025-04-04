# Translation & LLM Processing API

## Overview
This FastAPI-based API integrates **Google's Gemini LLM** and **Google Translate** to provide seamless text translation and processing.  
- Supports **multi-language translation**.
- Uses **Google Gemini AI** for **context-aware text processing**.
- Provides **bidirectional translation** before and after LLM processing.

## Features
✅ Translate text from **any language** to **English**  
✅ Process text using **Google Gemini AI**  
✅ Translate processed text back to the **original language**  
✅ Built with **FastAPI** for speed and efficiency  

---

## Project Structure
```
├── main.py             # FastAPI application
├── requirements.txt    # Project dependencies
├── README.md           # Documentation
```

---

## Installation & Setup

### **1️⃣ Prerequisites**
Ensure you have:
- **Python 3.8+**
- **Google API Key** (for Gemini API)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/Kunal-AI-git/LLM_API
cd your-repo
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run FastAPI Server**
```sh
python -m uvicorn main:app --reload
```

---

## API Endpoints

### **1️⃣ Home Route**
**GET /**  
🔹 Response:
```json
{
  "welcome": "Welcome to the Translation System API!"
}
```

---

### **2️⃣ Translate & Process Text**
**POST /translate_process/**  
🔹 **Request Body:**
```json
{
  "text": "Hola, ¿cómo estás?",
  "source_lang": "es",
  "target_lang": "en"
}
```

🔹 **Response:**
```json
{
  "response": "Hello! I'm doing great. How about you?"
}
```

---

## Environment Variables
Set up your **Google API Key** in the `main.py` file:
```python
API_KEY = "your-google-api-key"
```

---

## Contributing
Feel free to contribute! Open an issue or submit a pull request. 🚀

---

## License
MIT License

