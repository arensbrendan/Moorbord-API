from flask import Flask, request, Response
from flask_cors import cross_origin, CORS
from login_client import login
from admin_client import add_user, remove_user
from decorators import block
from python.schemas.LoginSchema import LoginSchema
from python.schemas.AddUserSchema import AddUserSchema
import json
from marshmallow.exceptions import ValidationError

app = Flask(__name__)
api_cors = {
    "origins": ["*"],
    "methods": ["OPTIONS", "GET", "POST", "DELETE"],
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
        return Response(json.dumps({"error": str(e)}, status=400))
    result = login(data)
    return Response(json.dumps({"valid" if result.correct else "error": result.correct if result.correct else result.error}), status=result.status_code)


@block
@app.route("/add_user", methods=["POST"])
@cross_origin(**api_cors)
def add_user_api():
    info = request.get_json()
    try:
        validate = AddUserSchema().load(info)
    except ValidationError as v:
        errors = []
        for i in v.messages.values():
            errors.append(i[0])
        return Response(json.dumps({"errors": errors}), status=400)
    except Exception as e:
        return Response(json.dumps({"errors": str(e)}), status=400)
    result = add_user(info)
    return Response(json.dumps({"message" if result.message else "error": result.message if result.message else result.error}), status=result.status_code)



@block
@app.route("/remove_user", methods=["DELETE"])
@cross_origin(**api_cors)
def remove_user_api():
    info = request.get_json()
    result = remove_user(info)
    return Response(
        json.dumps({"message" if result.message else "error": result.message if result.message else result.error}),
        status=result.status_code)


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
