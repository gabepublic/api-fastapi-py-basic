# api-fastapi-py-basic
API example using python fastapi 

Source: 
- Python for Software Engineering Bootcamp by Maximilian Schallwig;
  Published by Packt Publishing; O'Reilly

## TODO - wip
- Revisit & capture the Response model chpt

## Prerequisite

- Python environment (Python, pip, pipenv)
  See [Setup > Dev Environment > Python](https://digitalcompanion.gitbook.io/home/)

## SETUP
- Activate the virtual environment
```
C:\>cd <projectFolder>\api-fastapi-py-basic
C:\>pipenv shell
(api-fastapi-py-basic-R5wfDv9q) C:\>
```
- Install python package `fastapi`, and `uvicorn`
```
(api-fastapi-py-basic-R5wfDv9q) $ pipenv install fastapi uvicorn 
```
  - [Uvicorn](https://www.uvicorn.org/) is an ASGI web server 
    implementation for Python, a minimal low-level server/application
    interface for async frameworks.

- Install [pydantic](https://docs.pydantic.dev/), the data validation 
  and settings management using Python type annotations. `pydantic` 
  enforces type hints at runtime, and provides user friendly errors 
  when data is invalid. Define how data should be in pure, canonical 
  Python; validate it with pydantic.
```
(api-fastapi-py-basic-R5wfDv9q) C:\>pipenv install pydantic
```

- Install development packages:
  - `mypy` - a static type checker for Python
  - `pytes` - framework that makes it easy to write small, readable 
    tests, and can scale to support complex functional testing for
    applications and libraries.
```
(api-fastapi-py-basic-R5wfDv9q) C:\>pipenv install --dev mypy pytest
(api-fastapi-py-basic-R5wfDv9q) C:\>pytest --version
pytest 7.2.0
(api-fastapi-py-basic-R5wfDv9q) C:\>
```

- Alternatively, if you clone this repo, the `Pipfile` is included so
  just run the following:
```
C:\>cd <projectFolder>\api-fastapi-py-basic
C:\>pipenv shell
(api-fastapi-py-basic-R5wfDv9q) C:\>pipenv install
```

- The demo below was developed in visual studio code.
  - Since we are creating a virtual environment for this demo, the
    vscode python interpreter needs to be configured pointing to the
    python interpreter in virtual environment, as follow.
  - To select the Python interpreter; from within VS Code, open the 
    Command Palette (Ctrl+Shift+P), start typing the Python: Select 
    Interpreter command to search, then select the command.   

## CODE

- See `main.py`

- Run
```
(api-fastapi-py-basic-R5wfDv9q) C:\>uvicorn app.main:app --reload
INFO:     Started server process [20884]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

- Open browser and go to API, `http://localhost:8000/`

- Open browser and go to API docs, `http://localhost:8000/docs`

## TEST

### Prerequisite

- `pytest` has been installed
- all the test files are stored in the `tests` folder
- NOTE: the test file need to be prepended wijt `test_`, otherwise
  the file will not be included.

### Smoke

- Run the smoke test; add verbosity using (`-v`, `-vv`, etc.)
```
(api-fastapi-py-basic-R5wfDv9q) C:\>cd <projectFolder>\api-fastapi-py-basic
(api-fastapi-py-basic-R5wfDv9q) C:\>pytest -v tests\test_smoke.py
```