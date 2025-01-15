from flask import Flask, render_template, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/bmi', methods=['POST'])
def bmi():
    try:
        data = request.get_json()
        
        height = float(data['height'])
        weight = float(data['weight'])
        
        bmi_result = calculate_bmi(height, weight)
        
        return jsonify({
            'bmi': bmi_result
        }), 200
        
    except KeyError:
        return jsonify({
            'error': 'Missing required fields. Please provide height and weight.'
        }), 400
    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred.'
        }), 500

@app.route('/bmr', methods=['POST'])
def bmr():
    try:
        data = request.get_json()
        
        height = float(data['height'])
        weight = float(data['weight'])
        age = int(data['age'])
        gender = data['gender']
        
        bmr_result = calculate_bmr(height, weight, age, gender)
        
        return jsonify({
            'bmr': bmr_result
        }), 200
        
    except KeyError:
        return jsonify({
            'error': 'Missing required fields. Please provide height, weight, age, and gender.'
        }), 400
    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'error': 'An unexpected error occurred.'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
