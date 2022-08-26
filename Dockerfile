
FROM python:3.9
WORKDIR /src
COPY . /src
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 3000
CMD pipenv run python main.py
