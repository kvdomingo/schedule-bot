FROM python:3.8.9-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -U pip && pip install -r requirements.txt

COPY . .

EXPOSE 8080:80

CMD ["python", "main.py", "runbot"]
