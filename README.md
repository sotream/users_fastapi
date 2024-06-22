# FastAPI User Management Service

This is a simple FastAPI CRUD API service that manages users, using PostgreSQL as the database.

## Setup and Run

### Prerequisites

- Python 3.8+
- PostgreSQL

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/my_fastapi_project.git
    cd my_fastapi_project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your PostgreSQL database and update the configuration in `app/core/config.py`.

5. Run the database migrations:
    ```bash
    alembic upgrade head
    ```

6. Start the FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

7. Open your browser and go to `http://127.0.0.1:8000/docs` to see the API documentation.

## Project Structure

- `app/main.py`: Entry point of the application.
- `app/api/`: Contains the API routes and dependencies.
- `app/core/`: Contains the core configuration of the application.
- `app/db/`: Contains database models, schemas, and setup.
- `app/services/`: Contains business logic and services.

## Used Packages

- **fastapi**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **uvicorn**: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.
- **sqlalchemy**: The Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- **alembic**: A lightweight database migration tool for use with SQLAlchemy.
- **asyncpg**: An efficient, clean implementation of a PostgreSQL client library for Python's asyncio framework.
- **pydantic**: Data validation and settings management using Python type annotations.

### Note on Using Python 3

To ensure the correct version of Python is used, specify `python3` when creating the virtual environment:

```bash
python3 -m venv venv
```
