from flask import Flask, request
from flask_cors import cross_origin, CORS
from client import run, run_goodbye, run_insult, db_call, info_from_name
import json
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import http

app = Flask(__name__)
fastapp = FastAPI()

origins = ['*']

fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.route("/hello", methods=["POST"])
@cross_origin()
def post():
    print('hit')
    data = request.get_json()
    name = data['name']
    return run(name)


@app.route("/goodbye", methods=["POST"])
@cross_origin()
def goodbye():
    data = request.get_json()
    name = data['name']
    return run_goodbye(name)


@app.route("/insult", methods=["POST"])
@cross_origin(origins='*')
def insult():
    data = request.get_json()
    name = data['name']
    return run_insult(name)


@app.route("/dbcall", methods=["POST"])
@cross_origin(origins='*')
def db():
    data = request.get_json()
    name = data['firstname']
    name = db_call(name)
    print(name)
    print(isinstance(name, str))
    print(str(name))
    return str(name)


@app.route("/info", methods=["POST"])
@cross_origin()
def info():
    data = request.get_json()
    the_id = data['id']
    print(the_id)
    info = info_from_name(the_id)
    print(isinstance(info, str))
    print(str(info))
    return json.dumps({"message": info})


@fastapp.get("/check", status_code=http.HTTPStatus.ACCEPTED)
@cross_origin()
def check():
    return "check successful"


@app.route("/check", methods=["GET"])
@cross_origin()
def check_flask():
    return "check successful"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
    # uvicorn.run("main:fastapp", host="192.168.86.134", port=8000)
