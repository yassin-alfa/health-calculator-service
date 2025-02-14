from flask import Flask, request, jsonify, send_from_directory
from health_utils import calculate_bmi, calculate_bmr
import os

app = Flask(__name__, static_folder="static")

@app.route('/')
def serve_front():
    """Servir le fichier index.html comme page d'accueil."""
    return send_from_directory("static", "index.html")

@app.route('/bmi', methods=['POST'])
def bmi():
    """Calculer le BMI à partir des données envoyées."""
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')

    if not weight or not height:
        return jsonify({"error": "Missing weight or height"}), 400

    bmi_value = calculate_bmi(height, weight)
    return jsonify({"BMI": bmi_value})

@app.route('/bmr', methods=['POST'])
def bmr():
    """Calculer le BMR à partir des données envoyées."""
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')
    age = data.get('age')
    gender = data.get('gender')

    if not all([weight, height, age, gender]):
        return jsonify({"error": "Missing one or more required fields"}), 400

    bmr_value = calculate_bmr(height, weight, age, gender)
    return jsonify({"BMR": bmr_value})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # ✅ Corrigé ici
    app.run(host='0.0.0.0', port=port)
