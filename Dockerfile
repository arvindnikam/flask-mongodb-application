FROM python:3.11-slim-bullseye

EXPOSE 5004 5054

ENV FLASK_ENV=development

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
RUN mkdir -p log
RUN chmod +x config/development/start.sh

CMD config/development/start.sh
