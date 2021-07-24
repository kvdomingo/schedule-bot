FROM python:3.8.9-slim

COPY requirements.txt .

RUN python -m pip install -U pip && pip install -r requirements.txt

COPY . .

EXPOSE 8080:8080

CMD python main.py runbot