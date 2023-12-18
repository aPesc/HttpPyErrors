from urllib import error
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generateResponse():
    
    if request.method == 'GET':
        return """<h1>INICIO</h1>
                    <p>Lorem ipsum sir amet</p>
                """


@app.route('/profile', methods=["GET"])
def profile():
    devices = ["iphone", "android"]

    #print(request.headers["User-Agent"])
    agent = request.headers.get("User-Agent")

    if devices[0] in agent.lower():
        return """<p>Listado de perfiles</p>
                    <ul>
                        <li>Admin</li>
                        <li>Root</li>
                    </ul>"""
    else:
        return redirect("\\")

@app.errorhandler(401)
def err401(error):
    return "<h2>Ups, ha sucedido algo raro</h2>"

@app.errorhandler(403)
def err403(error):
    return "<h2>Ups, ha sucedido algo raro</h2>"

@app.errorhandler(404)
def err404(error):
    return "<h2>Ups, ha sucedido algo raro</h2>"


if __name__ == "__main__" :
    app.run(host='0.0.0.0')