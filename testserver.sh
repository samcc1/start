#!/bin/bash

python manage.py syncdb && echo yes | python manage.py collectstatic && python manage.py runserver
