## App Basic RestAPI with FastAPI-MySQL-Python

![Logo](https://user-images.githubusercontent.com/68432004/141463176-4d597652-0d1e-422b-9322-986d79251e0c.jpg)

## Resources
    https://fastapi.tiangolo.com/
    https://www.sqlalchemy.org/
    https://pypi.org/project/cryptography/
    https://www.uvicorn.org/

###  Create and activate Virtual Enviroment with dependencies
    install Python3
    install virtualenv
### vscode python -> select interpreter path -> python-exe
    pip3 install virtualenv  
    python3 -m venv .env
    .env/Scripts/activate.bat

## Install prerequisite libraries
    pip install -r requirements.txt

## Initialize server
    uvicorn app:app
## Initialize server (Reload)
    uvicorn app:app --reload

## Working MySQL in VSCODE (optional)
    https://marketplace.visualstudio.com/items?itemName=formulahendry.vscode-mysql
