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
    
    bmi_value = calculate_bmi(height, weight)
    return jsonify({"BMI": bmi_value})

@app.route('/bmr', methods=['POST'])
def bmr():
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
