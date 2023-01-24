from flask import Flask, request
from flask_cors import cross_origin, CORS
from database_client import login
from admin_client import add_user
from decorators import block
from python.schemas.LoginSchema import LoginSchema


app = Flask(__name__)
api_cors = {
  "origins": ["*"],
  "methods": ["OPTIONS", "GET", "POST"],
  "allow_headers": ["Authorization", "Content-Type"]
}


@block
@app.route("/login", methods=["GET"])
@cross_origin(**api_cors)
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
@app.route("/add_user", methods=["POST"])
@cross_origin(**api_cors)
def add_user_api():
    info = request.get_json()
    result = add_user(info)
    return {
        "message": "result"
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
