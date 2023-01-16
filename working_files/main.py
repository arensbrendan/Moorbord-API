from flask import Flask, request
from flask_cors import cross_origin, CORS
from client import db_call, info_from_name
import json
from decorators import hit

app = Flask(__name__)


@app.route("/dbcall", methods=["POST"])
@cross_origin(origins='*')
@hit
def db():
    data = request.get_json()
    name = data['firstname']
    name = db_call(name)
    return str(name)


@app.route("/info", methods=["POST"])
@cross_origin()
@hit
def info():
    data = request.get_json()
    the_id = data['id']
    the_info = info_from_name(the_id)
    return json.dumps({"message": the_info})


@app.route("/check", methods=["GET"])
@cross_origin()
@hit
def check():
    return "check successful"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

# This is what everyone else sees
# http://136.34.239.66:8001/check
