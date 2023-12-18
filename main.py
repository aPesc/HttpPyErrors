from urllib import error
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def generateResponse():
    try:
        if request.method == 'GET':
            return "<h1>Hola esto es un texto generado de prueba</h1>"
    except error.HTTPError as err:
        
        match err.code:
            case 404:
                return "<h1>Hi, you are not supose to be here</h1>"
            case 401:
                return "<h1>Not autorized</h1>"
    

if __name__ == "__main__" :
    app.run(host='0.0.0.0')