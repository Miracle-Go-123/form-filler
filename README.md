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

## Usage

1. Configure your form settings in the `config.json` file.
2. Run the application:
   ```bash
   npm start
   ```
3. Follow the prompts to fill out and submit forms.

## API Endpoints

If using the API mode, the following endpoints are available:

- **POST /api/fillForm**: Submit form data.

  - **Request Body**:
    ```json
    {
      "formId": "string",
      "fields": {
        "fieldName": "value"
      }
    }
    ```
  - **Response**:
    ```json
    {
      "status": "success",
      "message": "Form submitted successfully."
    }
    ```

- **GET /api/forms**: Retrieve a list of available forms.
  - **Response**:
    ```json
    [
      {
        "formId": "string",
        "formName": "string"
      }
    ]
    ```

## Configuration

The `config.json` file allows you to customize the behavior of FormFiller. Below is an example configuration:

```json
{
  "apiMode": true,
  "defaultFormId": "12345",
  "retryAttempts": 3,
  "timeout": 5000
}
```

- **apiMode**: Enable or disable API mode.
- **defaultFormId**: Specify a default form ID to use.
- **retryAttempts**: Number of retry attempts for failed submissions.
- **timeout**: Timeout duration (in milliseconds) for API requests.

## Dependencies

FormFiller relies on the following dependencies:

- **Node.js**: Runtime environment for executing JavaScript code.
- **Express**: Web framework for building API endpoints.
- **Axios**: HTTP client for making API requests.
- **Joi**: Schema validation for form inputs.

Install all dependencies using:

```bash
npm install
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or support, please contact [MiracleGo123](mailto:support@miraclego123.com).
