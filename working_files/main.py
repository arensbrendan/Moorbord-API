from flask import Flask, request
from flask_cors import cross_origin, CORS
from client import call_database, get_student_info_from_name, test_connection
import json
from decorators import log

app = Flask(__name__)


@app.route("/dbcall", methods=["POST"])
@cross_origin(origins='*')
def db_call():
    data = request.get_json()
    name = data['firstname']
    name = call_database(name)
    return str(name)


@app.route("/info", methods=["POST"])
@cross_origin()
def get_student_info():
    data = request.get_json()
    the_id = data['id']
    the_info = get_student_info_from_name(the_id)
    return json.dumps({"message": the_info})


@app.route("/test", methods=["POST"])
@cross_origin()
def test_conn():
    data = request.get_json()
    the_word = data['word']
    the_reply = test_connection(the_word)
    return json.dumps({"message": the_reply})


@app.route("/check", methods=["GET"])
@cross_origin()
def check():
    return "check successful"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

# This is what everyone else sees
# http://136.34.239.66:8001/check
