# Weather App
This is a simple weather app that uses wtrr.in API to get the weather of a city. It is built using Python, FastAPI, and Docker.

## Prerequisites
- Docker
- Docker Compose
- Python 3.12
- Pip

## Install and run
1. Clone the repository
```bash 
git clone
```
2. Change directory to the project folder
```bash
cd weather-app
```
3. Build the Docker image
```bash
cp .env.example .env
```
4. Build the Docker image
```bash
docker-compose build
```
5. Run the Docker container
```bash
docker-compose up
```

## Development and contribution

1. Install [dev] dependencies
```bash
pip install -e .[dev]
```

2. Install pre-commit hooks
```bash
pre-commit install
```


## Run tests
1. Install test dependencies
```bash
pip install -e .[test]
```

2. Run tests
```bash
pytest
```


### Description

This is a simple weather app that uses wtrr.in 
API to get the weather of a city. It is built using Python, 
FastAPI, and Docker.

- I used FastAPI because it is a modern, fast (high-performance),
- Also I've used dependency injector framework because it perfectly matches to FastAPI and it is a powerful tool for managing and injecting dependencies in Python.
- Considering that the app is small so i've used monorepo structure to keep the code organized.
- I've used Docker to containerize the app and make it easy to run and deploy.
- Also most of things are simplified and abstracted because of test assignment nature.
  - Config may be injected with DI framework default tools but i've used singleton pattern to keep it simple.
  - Exception handling is simplified and not coverage all cases.
  - Logging is simplified and not cover all cases.
  - Tests covers only happy paths and not cover all cases.