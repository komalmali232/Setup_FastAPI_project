# Setup_FastAPI_project
# FastAPI Addition Endpoint

## Overview
This project sets up a FastAPI application to perform addition on input lists of integers using Python's multiprocessing pool. The project follows the MVC (Model-View-Controller) structure.

## Setup
1. Install FastAPI and Uvicorn:
Step 2: Implement FastAPI Endpoint
In main.py, crea#te a FastAPI application and define the endpoint for addition.
Import the necessary modules such as Pydantic models and the addition controller.
Implement request validation using Pydantic models.
Implement the logic to perform addition using multiprocessing pool in the controller.
Define appropriate error handling and logging.
2. Step 3: Unit Testing
Write unit tests for all edge cases and scenarios in test_addition_controller.py.
Test the validation of request and response formats.
Test the addition logic with different inputs and edge cases.


## Usage
1. Run the FastAPI application:
2. Send POST requests to `http://localhost:8000/addition/` with the following JSON payload:

{
"batchid": "id0101",
"payload": [[1, 2], [3, 4]]
}


## Project Structure
- `main.py`: Entry point of the FastAPI application.
- `controllers/`: Contains the controller logic for processing addition.
- `models/`: Defines Pydantic models for request and response validation.
- `views/`: Defines the FastAPI endpoints.
- `tests/`: Contains unit tests for the controller logic.
- `README.md`: Overview and usage instructions for the project.
