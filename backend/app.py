from flask import Flask, request, jsonify
from utils import generate_recommendations
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()

app = Flask(__name__)

@app.route("/suggest", methods=["POST"])
def suggest():
    data = request.json
    user_input = data.get("input")

    if not user_input:
        return jsonify({"error": "Missing input"}), 400

    try:
        recommendations = generate_recommendations(user_input)
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
