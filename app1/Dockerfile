FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
# COPY app.py .
# COPY requirements.txt .

RUN apt-get update \
 && apt-get install -y iputils-ping

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]