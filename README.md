# Form Filler

Form Filler is a Python-based application designed to automate the process of filling PDF forms using user-provided data in JSON format. It leverages FastAPI for the backend, PyPDFForm for PDF manipulation, and CrewAI for task orchestration.

## Features

- Upload PDF templates and JSON data to fill forms dynamically.
- Supports text fields, checkboxes, dropdowns, and other PDF form widgets.
- Provides a web-based frontend for user interaction.
- Uses Azure OpenAI for intelligent field mapping and validation.
- Includes middleware for API key authentication.
- Generates filled PDF forms as downloadable files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MiracleGo123/form-filler.git
   ```
2. Navigate to the project directory:
   ```bash
   cd form-filler
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up environment variables
   - Create a .env file in the root directory (already included in the project:env-sample).
   - Update the values for AZURE_API_KEY, AZURE_API_BASE, and NEXT_API_KEY as needed.

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your browser and navigate to:

   ```bash
    http://127.0.0.1:8000/
   ```

3. Upload a PDF template and provide JSON data to fill the form.
4. Check the status of the job and download the filled PDF.

## API Endpoints

### `GET /`

Serves the frontend HTML page.

### `POST /upload`

Uploads a PDF file and JSON data to start the form-filling process.

#### Request Parameters:

- `pdf_file`: The PDF template file.
- `json_data`: JSON string containing user responses.

#### Response:

- `job_id`: Unique identifier for the form-filling job.

### `GET /status/{job_id}`

Checks the status of a form-filling job.

#### Response:

- `status`: Job status (`running`, `finished`, or `failed`).
- `output`: Base64-encoded filled PDF (if finished).
- `error`: Error message (if failed).

## Environment Variables

- `AZURE_API_KEY`: API key for Azure OpenAI.
- `AZURE_API_BASE`: Base URL for Azure OpenAI.
- `AZURE_API_VERSION`: API version for Azure OpenAI.
- `NEXT_API_KEY`: API key for authentication.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [PyPDF](https://pypdf.readthedocs.io/)
- [CrewAI](https://docs.crewai.com/)
- [Pillow](https://python-pillow.org/)
- [ReportLab](https://www.reportlab.com/)
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)
