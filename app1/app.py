# flask_app1.py
from flask import Flask, Response
import requests
import os

app = Flask(__name__)

# vars
# APP_2_URL = 'http://app2:5001'

# env_vars
APP_2_URL = os.environ.get('APP_2_URL')

@app.route("/")
def hello():
    return Response("{'message':'Hello from app1'}", status=200, mimetype="application/json")

@app.route("/health")
def health():
    return Response("{'message':'Healthy'}", status=200, mimetype="application/json")

@app.route("/get-env")
def get_env():
    return Response(str(dict(os.environ)), status=200, mimetype="application/json")

@app.route("/get-app2")
def app2():
    response = requests.get(APP_2_URL)
    return Response(response.content, status=response.status_code, mimetype="application/json")

@app.route("/test-error")
def test():
    return Response("{'message':'error'}", status=500, mimetype="application/json")

if __name__ == "__main__":
    port = 5000
    app.run(port=port)