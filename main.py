from utils import get_resume_response, create_prompt
from utils.openai_utils import api_key

from fastapi import FastAPI,  HTTPException





app = FastAPI()

@app.post("/process-resume")
async def process_resume(resume, job_desc):
    try:

        with open(resume, "r", encoding="utf-8") as file:
            resume = file.read()
        prompt = create_prompt(resume, job_desc)

        response_string = get_resume_response(prompt, api_key)
        response_list = response_string.split("## Additional Suggestions")

        new_resume = response_list[0]
        suggestions = "## Additional Suggestions  \n\n" + response_list[1]

        return  new_resume, new_resume, suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


