from flask import Flask, request
from flask_cors import cross_origin, CORS
from database_client import login
from decorators import log, block

app = Flask(__name__)


@block
@app.route("/login", methods=["POST"])
@cross_origin(origins='*')
def login_api():
    data = request.get_json()
    result = login(data)
    return "Correct combination: " + str(result.correct)


@block
@app.route("/check", methods=["GET"])
@cross_origin()
def check():
    return "check successful"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

# This is what everyone else sees
# http://136.34.239.66:8001/check
