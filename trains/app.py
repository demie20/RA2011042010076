# Flask app to fetch train data from a server and get train data

from flask import Flask
import requests
import json

app = Flask(__name__)

headers = {"Content-Type": "application/json"}


def get_auth_token():
    url = "http://20.244.56.144/train/auth"
    data = {
	"companyName": "Janvi Travels",
	"clientID": "a715fcdc-dae7-437b-9d0f-98ad6ed6e232",
	"clientSecret": "gZHBrygpEwTtSVun",
	"ownerName": "Janvi Somani",
	"ownerEmail": "js0182@srmist.edu.in",
	"rollNo": "RA2011042010076"
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
