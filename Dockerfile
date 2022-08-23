
FROM python:3.9
WORKDIR /src
COPY . /src
RUN pip install --no-cache-dir --upgrade -r /v/requirements.txt
COPY ./requirements.txt /code/requirements.txt
ENV   POSTGRES_USER='postgres'
ENV POSTGRES_PASSWORD='postgres'
ENV POSTGRES_DB='postgres'
ENV DATABASE_HOST='localhost'
ENV DATABASE_PORT=5432
EXPOSE 3000
CMD pipenv run python main.py