<h1 align="left">Curricul.AI Prototype</h1>

###

<h3 align="left">AI-Powered Resume Builder & Optimization</h3>

Curricul.AI is an AI-powered platform designed to help users create optimized resumes tailored to specific job descriptions.  
It uses OpenAI's GPT-4o-mini to enhance and personalize resumes while ensuring keyword alignment with Applicant Tracking Systems (ATS).

---

## 🚀 Features

- **AI Resume Optimization:** Automatically improves your resume with personalized suggestions.
- **Job Description Matching:** Tailors your resume to match specific job requirements.
- **Bullet Point Enhancer:** Sharp, impactful bullet point suggestions.
- **Keyword Optimization:** Ensures compatibility with ATS systems.
- **Gradio UI:** Simple interface for prototyping and testing.
- **PDF Export:** Generates clean, professional resumes via WeasyPrint.
- **(Coming soon)** Cover letter generation.

---

## ⚙️ Tech Stack

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="40" alt="fastapi logo"  />
</div>

**Backend:**  
- FastAPI  
- OpenAI API  

**Frontend (Prototype UI):**  
- Gradio  

**PDF + Formatting:**  
- WeasyPrint  
- Markdown  

---

## 📦 Install Dependencies

Install all necessary packages using:

```
pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```
markdown
weasyprint
gradio
openai
fastapi
uvicorn
python-dotenv
```

---

## ▶️ How to Use

### 1. Create a `.env` File

In the root directory of the project, create a `.env` file and add your own OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

### 2. Start the Backend API

Use the following command to run the FastAPI server:

```
uvicorn main:app --reload
```

Once running, the backend API will be available at:

```
http://127.0.0.1:8000
```

---

### 3. Launch the Gradio Interface (Prototype UI)

Run the following command:

```
python gradio_ui.py
```

This will open a browser interface where you can:

- Upload your resume  
- Paste a job description  
- Receive AI-powered suggestions and enhancements  
- Download your optimized PDF resume

---

## ⚠️ Notes

- `WeasyPrint` may require additional system dependencies depending on your OS.
- On **Windows**, the `markdown` library may not work properly unless [MSYS2](https://www.msys2.org/) is installed.
- This is a **prototype**, and features such as cover letter generation, language support, and job-specific templates are actively being developed.
- Projects improvements being built on private development repository.

---

## 📬 Contact
This is an early prototype — pull requests, ideas, and testing help are welcome!

**Pietro Brandalise De Andrade**  
📱 (11) 99473-1578  
📧 [ppietrobrandalise@icloud.com](mailto:ppietrobrandalise@icloud.com)  
🔗 [linkedin.com/in/pietroaandrade](https://www.linkedin.com/in/pietroaandrade)



