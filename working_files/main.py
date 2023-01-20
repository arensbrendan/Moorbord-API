from flask import Flask, request
from flask_cors import cross_origin, CORS
from client import db_call, info_from_name, the_test
import json
from decorators import hit

app = Flask(__name__)


@app.route("/dbcall", methods=["POST"])
@cross_origin(origins='*')
def db():
    data = request.get_json()
    name = data['firstname']
    name = db_call(name)
    return str(name)


@app.route("/info", methods=["POST"])
@cross_origin()
def info(origins='*'):
    data = request.get_json()
    the_id = data['id']
    the_info = info_from_name(the_id)
    #return json.dumps({"message": the_info})
    return str(the_info)


@app.route("/check", methods=["GET"])
@cross_origin()
def check():
    return "check successful"


@app.route("/test", methods=["POST"])
@cross_origin()
def test():
    data = request.get_json()
    the_word = data['word']
    the_reply = the_test(the_word)
    return json.dumps({"message": the_reply})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

# This is what everyone else sees
# http://136.34.239.66:8001/check
