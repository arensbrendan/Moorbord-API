from flask import Flask, request
from flask_cors import cross_origin
from database_client import login
from decorators import block
from python.schemas.LoginSchema import LoginSchema


app = Flask(__name__)


@block
@app.route("/login", methods=["GET"])
@cross_origin(origins='*')
def login_api():
    data = {
        "username": request.args.get('username'),
        "password": request.args.get('password')
    }
    try:
        validate = LoginSchema().load(data)
    except Exception as e:
        return {
            "error": str(e)
        }
    result = login(data)
    return {
        "message": result.correct
    }


@block
@app.route("/check", methods=["GET"])
@cross_origin()
def check():
    return "check successful"


def main():
    app.run(host='0.0.0.0', port=8000)


if __name__ == "__main__":
    main()
# This is what everyone else sees
# http://136.34.239.66:8001/check
