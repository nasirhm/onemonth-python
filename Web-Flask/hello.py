from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hwllo World!"

@app.route("/")
def index():
    return "Index"