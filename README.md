# CNAB Parser

An application focused on reading plain text files that contains standardized statements in each line of the document. It features a simple layout for selecting your file, and a padronized display of all the inputted information, which was saved and retrieved from a database.

## Tech Stacks

- Base Python
- Django framework
- Sqlite3 (for local development)
- PostgresQL
- Docker

## Installation guide

- Create a virtual environment, with:

`python -m venv venv`

- Activate your virtual environment, either with:

Windows - `./venv/Scripts/activate`

Linux - `source venv/bin/activate`

- Install all required dependencies from requirements.txt, with:

`pip install -r requirements.txt`

- Install all migrations, with:

`python manage.py migrate`

- Create a `.env` file, following the format in `.env.example`

  - Make sure all variables have values. May not be able to execute runserver command even if `TEST` variable has no value.

- Execute the server, with

`python manage.py runserver`

### If you'd like to run it on Docker, run:

`docker-compose up`

OBSERVATION: Application may not work in `http://0.0.0.0:8000` through Docker, simply change it to either `http://127.0.0.1:8000`, or `http://localhost:8000`.
