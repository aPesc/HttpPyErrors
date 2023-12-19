import json
import os
from flask import Flask, request, redirect, render_template, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    
    if request.method == 'POST':

        titulo = request.form.get("titulo")
        asunto = request.form.get("asunto")
        fecha = request.form.get("fecha")

        data = {
            'date': fecha,
            'titulo': titulo,
            'asunto': asunto,
            'sqluser': "admin",
            'pwd': "passw0rd"
        }

        if setJsonData("output.json", data):
        
            return render_template("base.html", message = "Incidencia enviada, para consultar incidencias ve a su respectivo apartado")

@app.route('/profile', methods=["GET"])
def profile():
    devices = ["iphone", "android"]

    #print(request.headers["User-Agent"])
    agent = request.headers.get("User-Agent")

    if devices[0] in agent.lower():
        return '''<p>Listado de perfiles</p>
                    <ul>
                        <li>Admin</li>
                        <li>Root</li>
                    </ul>
                '''
    else:
        return redirect("\\")

@app.route('/incidencias', methods=["GET"])
def incidencias():
    if request.method == "GET":
        lstIncidencias = list()
        lstIncidencias = getJsonData("output.json")
        return render_template("incidencias.html", lstIncidencias = lstIncidencias)
        #return open("./output.json", "r") 
        
    else: return render_template("index.html")
    
    


@app.errorhandler(401)
def err401(error):
    return render_template("errcode.html")

@app.errorhandler(403)
def err403(error):
    return render_template("errcode.html")

@app.errorhandler(404)
def err404(error):
    return render_template("errcode.html")


def getJsonData(file: str) -> list:

    with open(file,"r") as jfile:
        lst = json.load(jfile)
        return lst
    

def setJsonData(file: str, adment):
    lst = list()

    if os.path.exists(file):
        lst = getJsonData(file)

    lst.append(adment)

    with open(file,"w") as jfile:
        json.dump(lst, jfile, indent=2)
        
        return True



if __name__ == "__main__" :
    app.run(host='0.0.0.0')