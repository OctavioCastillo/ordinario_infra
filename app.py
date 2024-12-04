from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para el endpoint GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Hola Mundo'}), 200

@app.route('/prueba', methods=['GET'])
def prueba():
    return jsonify({'mensaje': 'Repo actualizado correctamente'}), 200

@app.route('/ordinario', methods=['GET'])
def ordinario():
    return jsonify({'mensaje': 'Prueba para video de ordianrio'}), 200


# Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
