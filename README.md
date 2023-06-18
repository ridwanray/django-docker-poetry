# Dockerised Django project with Poetry
Your software applications need monitoring. <br>
This codebase showcase how to use poetry in a dockerise Django project

This article has complete guide:  [check here](https://ridwanray.medium.com/how-to-monitor-a-django-application-with-sentry-de3ec31fa1f2?source=friends_link&sk=66d9d5312e78ae5048d85910c833151d)

# Setup & running locally

Create a .env file by copying the .env.sample provided and run:
```
docker compose build && docker compose up
```
to start the container. As an alternative, run:
```
docker compose -f docker-compose.dev.yml up --build
```
to build and run the container using the dev yaml file.
Make sure to externalize the db instance to be used. It can be in another container.

## Run tests
Run descriptive tests in the container using:
```
docker exec -it -w /app <container_name> pytest -rP -vv
```

Access the docs on:

```
http://localhost:10060/api/v1/doc
```


## Running In a Virtual Env

Create a virtual environment using:
```
mkvirtualenv <env_name>
```

Ensure you have installed `virtualenv` on your system and install dev dependencies using
```
pip install -r requirements/dev.txt
```

Run migrations using:
```
python manage.py makemigrations

python manage.py migrate
```

Run the server using:
```
python manage.py runserver
```

