FROM python:3.9

#
WORKDIR /code
ENV FASTAPI_APP main.py
#
COPY requirements.txt /code/requirements.txt

#
RUN pip3 install -r requirements.txt
#
COPY . ./code

#
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9000"]