# Free Games Parser
![Tests](https://github.com/altWulff/Free-Games-Parser/actions/workflows/python-tests.yml/badge.svg)
![Pylint](https://github.com/altWulff/Free-Games-Parser/actions/workflows/pylint.yml/badge.svg)

The project parses available free games
in the Epic Game Store, produces json output,
and displays on the page.

## Dependencies
- `Python 3.10+`
- `FastAPI`
- `Jinja2`


## Setup
`$ git clone git@github.com:altWulff/Free-Games-Parser.git && cd Free-Games-Parser`

`$ virtualenv venv && source venv/bin/activate`

`$ pip install -r requirements.txt`

`$ uvicorn app.main:app --reload`

Index page `http://127.0.0.1:8000`

Docs `http://127.0.0.1:8000/docs`


### Setting up with Docker
`$ docker build -t free_games_parser:latest .`

`$ docker run -d --name free_games_parser -p 80:80 free_games_parser:latest`


Index page `http://127.0.0.1`

Docs `http://127.0.0.1/docs`
