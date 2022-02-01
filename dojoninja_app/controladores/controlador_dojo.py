from dojoninja_app.modelos.modelo_dojo import Dojo
from flask import render_template, request, redirect, session
from dojoninja_app import app

@app.route('/')
def paginablanca():
    return redirect('/dojos')

@app.route( '/dojos', methods=["GET"] )
def enumeraciondeDojos():
    listaDojos = Dojo.obtenerListaDojo()
    print("EnumeraciondeDojos", listaDojos)
    return render_template( "dojos.html", Dojos=listaDojos)

@app.route('/dojo/registro', methods=["POST"])
def registroDojo():
    nuevoDojo = {
        "name" : request.form["name"]
    }
    resultado = Dojo.agregarDojo(nuevoDojo)
    return redirect('/')

@app.route('/dojo/<int:id>')
def listaninjaDojo(id):
    Dojos={
        "id":id
    }
    Ninjas=Dojo.listaNinjas(Dojos)
    print("Verificar si retorna listaNinjas", Ninjas)
    return render_template('ninjadojos.html', dojo=Ninjas )
    

