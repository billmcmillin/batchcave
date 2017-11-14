#!/bin/bash

python3 batchcave/manage.py makemigrations && python3 batchcave/manage.py migrate && python3 batchcave/manage.py runserver 0.0.0.0:8000
