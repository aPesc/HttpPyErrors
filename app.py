import json
from os import path
from flask import Flask, request, render_template

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
            'key': "SVAvYWRtaW4tPmZsYWc=", #Ip/admin->flag
            'key2': "WnViaXJpMjMyNEp1c3RQYXN0ZU1lU29tZXdoZXJl" 
        }

        if setJsonData("output.json", data):
        
            return render_template("base.html", message = "Incidencia enviada, para consultar incidencias ve a su respectivo apartado")

@app.route('/incidencias', methods=["GET"])
def incidencias():
    if request.method == "GET":
        lstIncidencias = list()
        lstIncidencias = getJsonData("output.json")
        return render_template("incidencias.html", lstIncidencias = lstIncidencias)

@app.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "GET": return render_template("admin.html", result=0)

    if request.method == "POST":
        key = request.form.get("key")

        if key == "Zubiri2324JustPasteMeSomewhere":
            return render_template("admin.html",result = 1)

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
    if path.exists(file):
        with open(file,"r") as jfile:
            lst = json.load(jfile)
            return lst
    
    return 0

def setJsonData(file: str, adment):
    lst = list()

    if path.exists(file):
        lst = getJsonData(file)

    lst.append(adment)

    with open(file,"w") as jfile:
        json.dump(lst, jfile, indent=2)
        
        return True


if __name__ == "__main__" :
    app.run(host='0.0.0.0')