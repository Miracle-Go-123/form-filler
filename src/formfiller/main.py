#!/usr/bin/env python
import sys
from formfiller.crew import Formfiller
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

class InputData(BaseModel):
    pdf_form_schema: str
    user_response: Dict[str, Any]

@app.post("/kickoff")
async def kickoff(input_data: InputData):
    try:
        formfiller = Formfiller()
        modified_inputs = formfiller.parse_pdf(input_data.dict())
        output = formfiller.crew().kickoff(modified_inputs)
        result = formfiller.fill_pdf(output)
        return {"message": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)