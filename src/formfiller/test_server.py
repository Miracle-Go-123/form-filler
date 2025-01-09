import requests
import json
import base64


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
    response = requests.post('http://localhost:8000/kickoff', json=inputs)
    print(response.json())