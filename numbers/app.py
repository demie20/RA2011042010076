from flask import Flask, request
import requests


app = Flask(__name__)


@app.route("/numbers", methods=["GET"])
def numbers():
    url_list = request.args.getlist("url")
    print(url_list)

    nums = []
    for url in url_list:
        response = requests.get(url)
        try:
            for num in response.json()["numbers"]:
                if num not in nums:
                    nums.append(num)
        except Exception as e:
            # print(e)
            pass

    nums = sorted(nums)

    return {"numbers": nums}


if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)
