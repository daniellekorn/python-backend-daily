# Question for Yaakov:
# I originally just printed each check_status() func with the relevant url input rather than making routes.
# However, I saw in the assignment description that it was including Flask. Why do we want to do
# something like this with Flask?

from flask import Flask
import requests

app = Flask(__name__)


def check_status(url):
    request = requests.get(url)
    if request.status_code == 200:
        return "Success: status code 200"
    else:
        return "Something went wrong: status code {}".format(request.status_code)


@app.route("/stack")
def get_stack():
    return check_status('https://stackoverflow.com/')


@app.route("/will")
def get_will():
    return check_status('https://frontendmasters.com/teachers/will-sentance/')


@app.route("/umich")
def get_umich():
    return check_status('https://umich.edu/')


if __name__ == "__main__":
    app.run()
