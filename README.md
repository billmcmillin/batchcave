# Batchcave
## A Web Interface for the Classic Batch Records Processing Program

## Setup
All environmental variables are defined in file .env. Copy this file into project root.

All other settings are defined in Dockerfile and docker-compose.yml.

* Currently only the dev environment is configured. 

# Testing
start server with ```sudo docker-compose up```

###Unit tests
run with 
```python3 manage.py test converter```
* make sure DATABASE_HOST env variable is not set
* file upload tests will only pass when run from inside container due to permissions

###Functional Tests
* use selenium, so these will not run inside the container
* run with ```python3 manage.py test functional_tests```
* in batchcaves/functional_tests/tests.py

## Migrations
```python3 batchcave/manage.py makemigrations```

## Running
From project root:
```docker-compose up```

## SSH into container
* docker attach won't work b/c start_app.sh is running the server. Instead, use
```sudo docker exec -it batchcave_app_1 bash```

## Flush Database Contents
in run_app.sh, prepend this:
```cat <(echo "yes") - | python3 manage.py flush
## Sources
* [https://docs.docker.com/compose/django/](https://docs.docker.com/compose/django/)
