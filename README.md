# Free Games Parser

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
