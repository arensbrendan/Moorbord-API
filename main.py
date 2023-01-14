from flask import Flask, request
from flask_cors import cross_origin
from client import run, run_goodbye, run_insult, db_call, info_from_name

app = Flask(__name__)


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
@cross_origin()
def insult():
    data = request.get_json()
    name = data['name']
    return run_insult(name)


@app.route("/dbcall", methods=["POST"])
@cross_origin()
def db():
    data = request.get_json()
    name = data['firstname']
    return db_call(name)


@app.route("/info", methods=["POST"])
@cross_origin()
def info():
    data = request.get_json()
    the_id = data['id']
    return info_from_name(the_id)


if __name__ == "__main__":
    app.run(host='192.168.56.1', port=8000)
