# started the ml model
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/query", methods=["POST", "GET"])
def getCode():
    if(request.method == 'POST'):
        return jsonify({"query": request.form["query"]})
    return "<h1>Welcome </h1>"
