from flask import Flask, render_template, request
from model.view import ver_jugadores, ver_jugador, agregar_los_vacios, visu_pais, visu_pais1
from model.ingreso import ingreso_jugador, ingreso_pais
from model.actualizar import settpais, cambiar_estado
import pyodbc as sql

app = Flask(__name__)
conexion = sql.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=JAVIER-PC\MSSQLSERVER2021;DATABASE=bdjugadores;UID=sa;PWD=skater11')


# conexion

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/insert')
def insert():
    return render_template('jugador/insert.html')

@app.route('/insert2')
def insert2():
    return render_template('jugador/insert2.html')


@app.route('/save_insert', methods=['POST'])
def save_insert():
    if request.method == 'POST':
        nombre = request.form['nombre jugador']
        apellido = request.form['apellido jugador']
        aka = request.form['aka jugador']
        pais = request.form['pais jugador']
        equipo = request.form['equipo jugador']
        fecha_naci = request.form['cumple jugador']
        genero = request.form['genero jugador']
        rol = request.form['rol jugador']
        print(nombre, apellido, aka, pais, equipo, fecha_naci, genero, rol)
        ingreso_jugador(nombre, apellido, aka, pais, equipo, fecha_naci, genero, rol, conexion)
        return render_template('jugador/save_insert.html')
    return "error"


@app.route("/edit")
def edit():
    data = ver_jugadores(conexion)
    print(data)
    return render_template('jugador/edit.html', jugadores=data)


@app.route("/edit-2", methods=["POST"])
def edit_2():
    if request.method == 'POST':
        id = request.form['id jugador']
        # update_jugador(id)
        # datos=jugador(id)
        datos = ver_jugador(id, conexion)
    return render_template('jugador/edit-2.html', datos=datos[0])


@app.route('/save_edit', methods=['POST'])
def save_edit():
    if request.method == 'POST':
        ide = request.form['id']
        nombre = request.form['nombre jugador']
        apellido = request.form['apellido jugador']
        aka = request.form['aka jugador']
        pais = request.form['pais jugador']
        equipo = request.form['equipo jugador']
        fecha_naci = request.form['cumple jugador']
        genero = request.form['genero jugador']
        rol = request.form['rol jugador']
        print(ide, nombre, apellido, aka, pais, equipo, fecha_naci, genero, rol)
        agregar_los_vacios(ide, [ide, nombre, apellido, aka, pais, equipo, fecha_naci, genero, rol], conexion)

        return render_template('jugador/save_edit.html')
    return "error"


@app.route("/view")
def view():
    data = ver_jugadores(conexion)
    print(data)
    return render_template('jugador/view.html', jugadores=data)


@app.route("/view-2", methods=["POST"])
def view_2():
    if request.method == 'POST':
        id = request.form['id']
        # data = (1, "juan", "pere", "juanito", "chl", "xxx", "34343", "5345", "m", "sniper")
        data = ver_jugador(id, conexion)
        print(data)
    return render_template('jugador/view-2.html', jugador=data[0])


@app.route("/delete")
def delete():
    return render_template('jugador/delete.html')


@app.route("/delete-2", methods=['POST'])
def delete_2():
    if request.form['id']:
        id = request.form['id']
        data = (1, "juan", "pere", "juanito", "chl", "xxx", "34343", "5345", "m", "sniper")
        # data = view_jugador(id)
        return render_template('delete-2.html', jugador=data)

    return render_template('jugador/delete-2.html')


@app.route("/save-delete")
def save_delete():
    return render_template('jugador/save-delete.html')


@app.route("/pais")
def pais():
    return render_template("pais/pais.html")


@app.route("/pais/insert")
def insertpais():
    return render_template("pais/insert.html")


@app.route("/pais/saveinsert", methods=['POST'])
def saveinsertpais():
    if request.form['nombre pais']:
        pais = request.form['nombre pais']
        print(pais)
        ingreso_pais(pais, conexion)
        return render_template('pais/saveinsert.html')


@app.route("/pais/view")
def viewpais():
    paises = visu_pais(conexion)
    return render_template("pais/view.html", paises=paises)


@app.route("/pais/set")
def setpais():
    paises = visu_pais(conexion)
    return render_template("pais/set.html", paises = paises)


@app.route("/pais/set2", methods=['POST'])
def setpais2():
    if request.form['id pais']:
        id = request.form['id pais']
        pais = visu_pais1(id, conexion)
    return render_template("pais/set2.html", pais=pais[0])


@app.route("/pais/saveset", methods=['POST'])
def savepais():
    if request.method == 'POST':
        ide = request.form['id pais']
        nombre = request.form['nombre pais']
        abr = request.form['abr']
        settpais(ide, nombre, conexion)
    return render_template("pais/saveset.html")

@app.route("/pais/delete")
def deletepais():
    paises = visu_pais(conexion)
    return render_template("pais/delete.html", paises = paises)


@app.route("/pais/delete2", methods=['POST'])
def deletepais2():
    if request.form['id pais']:
        id = request.form['id pais']
        pais = visu_pais1(id, conexion)
    return render_template("pais/delete2.html",pais=pais[0])


@app.route("/pais/savedelete", methods=['POST'])
def savedeletepais():
    if request.method == 'POST':
        estado = request.form['estado']
        idpais = request.form["id pais"]
        cambiar_estado(idpais, estado, conexion)
    return render_template("pais/savedelete.html")


if __name__ == '__main__':
    app.run(port=3000, debug=True)
