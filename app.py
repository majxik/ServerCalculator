from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    if 'operation' not in data or 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing data'}), 400

    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return jsonify({'error': 'Non-numeric data'}), 400

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'})
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'})

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)