FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install flask_cors

COPY ./app /app
WORKDIR /app/

COPY ./app/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 80