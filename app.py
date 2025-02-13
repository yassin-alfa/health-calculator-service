<<<<<<< HEAD
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

=======
from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur l'API Health Calculator! Utilisez /bmi ou /bmr."})

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.get_json()
    weight = data.get('weight')
    height = data.get('height')
    
    if not weight or not height:
        return jsonify({"error": "Missing weight or height"}), 400
    
>>>>>>> 72048be (ajout des fichiers)
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"BMI": bmi_value})

@app.route('/bmr', methods=['POST'])
def bmr():
<<<<<<< HEAD
    """Calculer le BMR à partir des données envoyées."""
=======
>>>>>>> 72048be (ajout des fichiers)
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
    app.run(host='0.0.0.0', port=5000)
