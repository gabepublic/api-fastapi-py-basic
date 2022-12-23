# api-fastapi-py-basic
API example using python fastapi 

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

## CODE

- See `main.py`

- Run
```
(api-fastapi-py-basic-R5wfDv9q) C:\>uvicorn main:app
INFO:     Started server process [20884]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

- Open browser and go to API, `http://localhost:8000/`

- Open browser and go to API docs, `http://localhost:8000/docs`
