from dojoninja_app.modelos.modelo_dojo import Dojo
from dojoninja_app.modelos.modelo_ninja import Ninja
from flask import render_template, request, redirect, session
from dojoninja_app import app

@app.route( '/ninja', methods=["GET"] )
def paginaNinjas():
    listaDojos = Dojo.obtenerListaDojo()
    return render_template( "ninja.html", Dojos=listaDojos)

@app.route('/ninja/registro', methods=["POST"])
def registroNinja():
    nuevoNinja = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo_id"],
    }
    resultado = Ninja.agregaNinja(nuevoNinja)
    print("esete es el nuevo ninja",nuevoNinja)
    return redirect('/')

