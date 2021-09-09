from flask import Flask, request, jsonify



app = Flask(__name__)


@app.route("/", methods=["POST"])
def homen():
    return jsonify({ "messaje": "Entraste"})







if __name__ == "__main__":
    app.run(debug=True)
    