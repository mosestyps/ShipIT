from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(message="Hello from ShipIt", version="1.0")

@app.get("/health")
def health():
    return jsonify(status="ok")
