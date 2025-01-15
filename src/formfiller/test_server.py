import requests
import json
import base64
from time import sleep

if __name__ == "__main__":
    pdf_path = '/Volumes/Drive D/vizafi/python/formfiller_api/assets/raw_pdfs/i-90.pdf'
    with open(pdf_path, "rb") as pdf_file:
        pdf_binary = pdf_file.read()
    user_response_path = '/Volumes/Drive D/vizafi/python/formfiller_api/assets/jsons/result.json'
    with open(user_response_path, "r") as file:
        user_response = json.load(file)
    inputs = {
        "pdf_form_schema": base64.b64encode(pdf_binary).decode('utf-8'),
        "user_response": user_response,
    }

    # Make the kickoff request
    response = requests.post('http://localhost:8000/kickoff', json=inputs)
    kickoff_response = response.json()
    print("Kickoff response:", kickoff_response)

    # Extract the job_id from the kickoff response
    job_id = kickoff_response.get("job_id")
    if job_id:
        # Make the status request using the job_id
        while True:
            status_response = requests.get(f'http://localhost:8000/status/{job_id}')
            print("Status response:", status_response.json())
            status = status_response.json().get("status")
            if status == "finished":
                break
            sleep(5)
    else:
        print("No job_id returned from kickoff")