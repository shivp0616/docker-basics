from flask import Flask, Response

import logging

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        filename='./logs/out.log',
        filemode='a'
        )

app = Flask(__name__)

@app.route("/")
def hello():
    return Response("{'message':'Hello from app1'}", status=200, mimetype="application/json")

@app.route("/health")
def health():
    return Response("{'message':'Healthy'}", status=200, mimetype="application/json")

@app.route("/test-error")
def test():
    return Response("{'message':'error'}", status=500, mimetype="application/json")

if __name__ == "__main__":
    port = 5001
    app.run(port=port)
