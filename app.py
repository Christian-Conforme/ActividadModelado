from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    operacion = data.get('operacion')
    num1 = data.get('num1')
    num2 = data.get('num2')

    if operacion == 'sumar':
        resultado = num1 + num2
    elif operacion == 'restar':
        resultado = num1 - num2
    elif operacion == 'multiplicar':
        resultado = num1 * num2
    elif operacion == 'dividir':
        if num2 == 0:
            return jsonify({"error": "No se puede dividir entre cero."}), 400
        resultado = num1 / num2
    else:
        return jsonify({"error": "Operación no válida."}), 400

    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
