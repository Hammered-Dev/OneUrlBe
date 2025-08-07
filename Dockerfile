FROM python:3.13.5-alpine3.22

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m", "src/oneurl/main.py" ]