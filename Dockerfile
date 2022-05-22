FROM python:latest

RUN useradd free_games_parser
WORKDIR /home/free_games_parser

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN pip install -r requirements.txt
RUN pip install uvicorn

COPY app app

RUN chown -R free_games_parser:free_games_parser ./
USER free_games_parser

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]