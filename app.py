from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a la Calculadora API. Usa las rutas /sumar, /restar, /multiplicar o /dividir para realizar operaciones."

@app.route('/sumar', methods=['POST'])
def sumar():
    data = request.json
    resultado = data['a'] + data['b']
    return jsonify({'resultado': resultado})

@app.route('/restar', methods=['POST'])
def restar():
    data = request.json
    resultado = data['a'] - data['b']
    return jsonify({'resultado': resultado})

@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    data = request.json
    resultado = data['a'] * data['b']
    return jsonify({'resultado': resultado})

@app.route('/dividir', methods=['POST'])
def dividir():
    data = request.json
    if data['b'] == 0:
        return jsonify({'error': 'No se puede dividir entre cero.'}), 400
    resultado = data['a'] / data['b']
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
