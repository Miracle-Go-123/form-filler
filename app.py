from fastapi import FastAPI, HTTPException, BackgroundTasks, Form, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Union, Optional, Dict
from enum import StrEnum
from uuid import uuid4
import base64
import json
from pathlib import Path
from crew import Formfiller


# Models
class UserResponseItem(BaseModel):
    question: str
    answer: Union[str, int, bool]

class InputData(BaseModel):
    pdf_form_schema: str
    user_response: List[UserResponseItem]

class Status(StrEnum):
    RUNNING = 'running'
    FINISHED = 'finished'
    FAILED = 'failed'

class CrewItem(BaseModel):
    status: Status
    output: Optional[Union[str, dict]] = None  # Allow dict or string for output
    error: Optional[str] = None

store: Dict[str, CrewItem] = {}

# FastAPI app
app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def run_kickoff(input_data: InputData, job_id: str):
    try:
        formfiller = Formfiller()
        output = formfiller.crew().kickoff(input_data.dict())
        store[job_id] = CrewItem(status=Status.FINISHED, output=output)
    except Exception as e:
        store[job_id] = CrewItem(status=Status.FAILED, error=str(e))


@app.get("/", response_class=HTMLResponse)
async def get_frontend():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/upload")
async def upload_files(
    pdf_file: UploadFile, json_file: UploadFile, background_tasks: BackgroundTasks
):
    try:
        # Read PDF and JSON
        pdf_binary = await pdf_file.read()
        user_response = json.loads(await json_file.read())
        pdf_base64 = base64.b64encode(pdf_binary).decode("utf-8")
        
        # Prepare input data
        input_data = InputData(
            pdf_form_schema=pdf_base64,
            user_response=user_response,
        )
        
        # Create job
        job_id = str(uuid4())
        background_tasks.add_task(run_kickoff, input_data, job_id)
        store[job_id] = CrewItem(status=Status.RUNNING)
        return {"job_id": job_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    try:
        if job_id not in store:
            raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
        return store[job_id]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
