FROM python:3.9

#
WORKDIR /code
ENV FASTAPI_APP main.py
#
COPY requirements.txt requirements.txt

#
RUN pip3 install -r requirements.txt
#
COPY . .

#
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "9000"]