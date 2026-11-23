import os
from flask import Flask, jsonify, request

app = Flask(__name__)

PORT = int(os.environ.get("APP_PORT", "5000"))
GREETING = os.environ.get("APP_GREETING", "Hola mundo!")
SLOPE = float(os.environ.get("MODEL_SLOPE", "2.0"))
INTERCEPT = float(os.environ.get("MODEL_INTERCEPT", "1.0"))


@app.route("/")
def home():
    return GREETING


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/predict")
def predict():
    x = request.args.get("x")
    if x is None:
        return jsonify(error="falta el parametro 'x'"), 400
    try:
        x = float(x)
    except ValueError:
        return jsonify(error="'x' debe ser numerico"), 400
    y = SLOPE * x + INTERCEPT
    return jsonify(
        x=x,
        prediction=y,
        model={"slope": SLOPE, "intercept": INTERCEPT},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)