# Django on Docker

This repository contains an example of the base Docker image with Django and Postgres.

## Instructions

To get started, follow the below steps:

- Clone the repository.
- Execute `docker-compose up -d --build`. This will build the image and start the container.
- Test the Django environment for any errors using this command: `docker-compose run --rm web sh -c "python manage.py test && flake8"`
- On the browser, open http://localhost:8000/admin for the Django UI.
- For creating the **admin** credentials, run the following command: `docker-compose exec web python manage.py createsuperuser`

After the Superuser gets created successfully, utilize the Django (on Docker image) for building apps.

## Getting started with Django

**Django** is a powerful web framework for building web applications with Python. Here's a step-by-step guide to getting started with Django:

- **Install Python**: Before you can use Django, you'll need to have Python installed on your computer. You can download Python from the official website at https://www.python.org/downloads/

- **Install Django**: Once you have Python installed, you can use pip to install Django. Open a command prompt and enter the command `pip install Django` to install the latest version of Django.

- **Create a Django project**: To create a new Django project, navigate to the directory where you want to create the project and enter the command `django-admin startproject projectname`. This will create a new directory with the name of your project and the necessary files for a new Django project.

- **Create a Django app**: A Django app is a component of a Django project that serves a specific function. To create a new app, navigate to the directory of your Django project and enter the command `python manage.py startapp appname`.

- **Define models**: In Django, models define the structure of your data. Define the models for your app by creating a new file in the app directory called `models.py` and defining your models using Django's built-in model classes.

- **Define views**: Views are Python functions that handle requests and return responses. Define the views for your app by creating a new file in the app directory called `views.py` and defining your views as functions.

- **Define URLs**: URLs map requests to views. Define the URLs for your app by creating a new file in the app directory called `urls.py` and defining your URLs using Django's built-in URL patterns.

- **Run the server**: To test your app, navigate to the directory of your Django project and enter the command "python manage.py runserver". This will start the development server, and you can access your app by navigating to http://127.0.0.1:8000/ in your web browser.

## Migration Workflow

**Important**: Make sure your app is in `INSTALLED_APPS` inside `settings.py`

- Step 1: Change model code
- Step 2: Generate migration script (check it!)
  `docker-compose exec web python manage.py makemigrations`
- Optional Step: Show migrations
  `docker-compose exec web python manage.py showmigrations`
- Step 3: Run migrations
  `docker-compose exec web python manage.py migrate`

## Some other useful Django commands

- `docker-compose exec web django-admin startproject <project-name> .`
- `docker-compose exec web python manage.py startapp <app-name>`
- `docker-compose exec web python manage.py sqlmigrate <app-name> <migration-name/number>`
- `docker-compose run --rm web sh -c "python manage.py runserver"`
- `docker-compose run --rm web sh -c "python manage.py runserver 0.0.0.0:8000"`
- `docker-compose logs -f`
