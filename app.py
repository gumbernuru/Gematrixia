from flask import Flask, request, jsonify
from logic.sniper_engine import generate_prediction

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Gematrixia – Prediction Intelligence Activated"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    result = generate_prediction(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
