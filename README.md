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
```