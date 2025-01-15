#!/usr/bin/env python

from crew import Formfiller
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Union, Optional, Dict
from uuid import uuid4
from enum import StrEnum


class UserResponseItem(BaseModel):
    question: str
    answer: Union[str, int, bool]

class InputData(BaseModel):
    pdf_form_schema: str
    user_response: List[UserResponseItem]

class Status(StrEnum):
    RUNNING='running'
    FINISHED='finished'
    FAILED='failed'

class CrewItem(BaseModel):
    status: Status
    output: Optional[str] = None
    error: Optional[str] = None

store: Dict[str, CrewItem] = {}
app = FastAPI()

def run_kickoff(input_data: InputData, job_id: str):
    try:
        formfiller = Formfiller()
        output = formfiller.crew().kickoff(input_data.dict())
        store[job_id] = CrewItem(status=Status.FINISHED, output=output)
    except Exception as e:
        store[job_id] = CrewItem(status=Status.FAILED, error=str(e))

@app.post("/kickoff")
async def kickoff(input_data: InputData, background_tasks: BackgroundTasks):
    try:
        job_id = str(uuid4())
        background_tasks.add_task(run_kickoff, input_data, job_id)
        store[job_id] = CrewItem(status=Status.RUNNING)
        return {"job_id": job_id, "message": "Job started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    try:
        if job_id not in store:
            raise HTTPException(status_code=404, detail=f"Job {job_id} not found")
        else:
            return store[job_id]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
