# Fast API Sample project for EY
This project is fast api applicaiton with request and responce validation using Pydantic models.
The main functionality is to perform addirtion of two input lists of integers using pytrhons multiporcessong pool with proper error handleing and logging and monitoring activities

## Prerequirisites

Python 3.7+
FastApi
Uvicorn

## Installation
1- clone the repo 
    git clone https://github.com/nitinbansude/FastApi.git
2- install the dependencies:
    pip install -r requirment.txt

## Run the application
    uvicorn app.main:main --reload 
    api will be avalibale at http://127.0.0.1:8000

## running test
    pytest

use http://127.0.0.1:8000/docs to test api