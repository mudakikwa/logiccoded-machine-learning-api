# started the ml model
from flask import Flask, request,jsonify

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def getCode():
    if(request.method == 'POST'):
        return jsonify(request.form("query"))
    return "ready"


if __name__ == "__main__":
    app.run(debug=True)
