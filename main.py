from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def generateResponse():
    if request.method == 'GET':
        return "<h1>Hola esto es un texto generado de prueba</h1>"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')