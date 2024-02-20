# LAB - Class 31

## Project: Django REST Framework & Docker

### Author: [Caleb Hemphill](https://github.com/kaylubh)

A small project to demonstrate how to used Django and Django REST Framework to set up a web API.

### Setup

#### Requirements

1. Install [Python](https://www.python.org/) if not already

1. Create and activate a virtual environment

    `python3 -m venv .venv`

    `source .venv/bin/activate` (Linux/Mac)

    `source .venv/Scripts/activate` (Windows)

1. Install packages

    `pip install -r requirements.txt`

#### Run

1. Run `python manage.py runserver` from root of project directory in order to interact with the API

1. In a browser navigate to: `http://localhost:8000/api/v1/penguins/`

    Adjust `localhost` as necessary to match your runtime configuration

1. In order to view resources individually, append the "id" to the path

    Example: `http://localhost:8000/api/v1/penguins/1`

#### Tests

From root of project directory run `python manage.py test`
