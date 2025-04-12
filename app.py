from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return jsonify(message="Benvenuto!")
    #return "Benvenuto!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
