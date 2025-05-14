from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/welcome")
def welcome():
    return jsonify(message="Benvenuto utente!")
    #return "Benvenuto!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
