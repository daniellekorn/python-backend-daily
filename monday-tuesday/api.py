from flask import Flask

app = Flask(__name__)

users = {}
instruments = {}


@app.route("/")
def hello():
    return "Hello user!"


if __name__ == "__main__":
    app.run()
