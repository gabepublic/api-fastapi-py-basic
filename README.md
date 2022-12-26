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
C:\> cd <projectFolder>\api-fastapi-py-basic
C:\> pipenv shell
(api-fastapi-py-basic-R5wfDv9q) C:\>
```

- Install python package `fastapi`, and `uvicorn`
```
(api-fastapi-py-basic-R5wfDv9q) $ pipenv install fastapi uvicorn 
```

- Alternatively, if you clone this repo, the `Pipfile` is included so
  just run the following:
```
C:\> cd <projectFolder>\api-fastapi-py-basic
C:\> pipenv shell
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
(api-fastapi-py-basic-R5wfDv9q) C:\>uvicorn main:app --reload
INFO:     Started server process [20884]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

- Open browser and go to API, `http://localhost:8000/`

- Open browser and go to API docs, `http://localhost:8000/docs`
