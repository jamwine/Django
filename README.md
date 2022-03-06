# Django on Docker
This repository contains an example of the base Docker image with Django and Postgres.

## Instructions
To get started, follow the below steps:
* Clone the repository.
* Execute `docker-compose up -d --build`. This will build the image and start the container.
* Test the Django environment for any errors using this command: `docker-compose run --rm web sh -c "python manage.py test && flake8"`
* On the browser, open http://localhost:8000/admin for the Django UI.
* For creating the **Admin** credentials, run the following command: `docker-compose exec web python manage.py createsuperuser`

After the Superuser gets created successfully, utilize the Django (on Docker image) for building apps.

## Some other useful Django commands

* `docker-compose exec web django-admin startproject <project-name> .`
* `docker-compose exec web python manage.py startapp <app-name>`
* `docker-compose exec web python manage.py makemigrations`
* `docker-compose exec web python manage.py migrate`
* `docker-compose run --rm web sh -c "python manage.py runserver 0.0.0.0:8000"`
* `docker-compose logs -f`
