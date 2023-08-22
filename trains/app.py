# Flask app to fetch train data from a server and get train data

from flask import Flask
import requests
import json

app = Flask(__name__)

headers = {"Content-Type": "application/json"}


def get_auth_token():
    url = "http://20.244.56.144/train/auth"
    data = {
        "companyName": "Train Central",
        "clientID": "b46118f0-fbde-4b16-a4bl-6ae6ad718b27",
        "ownerName": "Rahul",
        "ownertmail": "rahul@abc.edu",
        "rollNo": "1",
        "clientSecret": "XOyolORPasKWOdAN",
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = json.loads(response.text)
    return response_data["Authorization"]


@app.route("/trains")
def trains():
    url = "http://20.244.56.144/train/trains"
    response = requests.get(url, headers=headers)
    return response.text


@app.route("/")
def index():
    return "Hello World"


@app.route("/trains")
def trains():
    return "This is the trains page"


if __name__ == "__main__":
    app.run(debug=True)
