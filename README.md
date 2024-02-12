# FastAPI SQLite Example

This is a simple FastAPI application that demonstrates the use of SQLite database with background tasks using `fastapi_utils`.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-sqlite-example.git
    cd fastapi-sqlite-example
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI application on `http://127.0.0.1:8000`.

2. Access the Swagger documentation:

    Open your web browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API using the Swagger UI.

## Application Structure

- `main.py`: Main FastAPI application file containing the application setup, background tasks, and endpoints.
- `requirements.txt`: List of dependencies for the project.

## Background Tasks

The application demonstrates the use of background tasks using `fastapi_utils.tasks.repeat_every` decorator. Two background tasks, `remove_expired_tokens_task` and `remove_expired_tokens_task1`, are defined in the `main.py` file. The tasks are scheduled to run every 3 seconds (you can adjust this as needed).

## SQLite Database

The application uses SQLite as the database backend. The `FastAPISessionMaker` class from `fastapi_utils.session` is used to manage the database sessions.

## Important Note

In the provided example, `remove_expired_tokens_task1` intentionally raises an exception (`x = 0/0`) to demonstrate error handling in background tasks. You can uncomment the lines to use the actual background task logic (`remove_expired_tokens(db=db)`).

Feel free to modify the code and adapt it to your specific use case.

