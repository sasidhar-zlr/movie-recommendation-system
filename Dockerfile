FROM python:3.8-slim

WORKDIR /movie-recommendation-system

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]