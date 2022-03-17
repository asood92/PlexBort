FROM python:3.8-alpine
RUN mkdir /plexbot
ADD . /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]