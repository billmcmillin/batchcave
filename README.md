# Batchcave
## A Web Interface for the Classic Batch Records Processing Program

## Setup
All environmental variables are defined in file .env. Copy this file into project root.

All other settings are defined in Dockerfile and docker-compose.yml.

* Currently only the dev environment is configured. 

## Testing
Functional tests in functional_tests.py 
start server with ```sudo docker-compose up```
run with ```python3 functional_tests.py```

## Migrations
```python3 batchcave/manage.py makemigrations```

## Running
From project root:
```docker-compose up```

## SSH into container
* docker attach won't work b/c start_app.sh is running the server. Instead, use
```sudo docker exec -it batchcave_app_1 bash```

## Sources
* [https://docs.docker.com/compose/django/](https://docs.docker.com/compose/django/)
