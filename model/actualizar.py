# actualizar la informacion de los elementos en las tablas
from model.ingreso import *

def settpais(id, nombre, conexion):
    cursorinsert = conexion.cursor()
    consulta = "SELECT * from pais"
    cursorinsert.execute(consulta)
    lista = cursorinsert.fetchone()
    cursorinsert.commit()
    cursorinsert.close()
    while True:
        if nombre == "":
            nombre = lista[1]
        else:
            break
    abre = recortar_nombre_pais(nombre)
    cursorinsert = conexion.cursor()
    consulta = "UPDATE Pais SET NombrePais = '"+nombre+"', AbreviacionPais='"+abre+"' where PaisID='"+id+"'"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()
    return

def update_jugador(id, conexion):
    while True:
        print("[1] Modificar nombre")
        print("[2] Modificar apellido")
        print("[3] Modificar AKA")
        print("[4] Modificar pais")
        print("[5] Modifcar equipo")
        print("[6] Modificar fecha de nacimiento")
        print("[7] Modificar genero")
        print("[8] Modificar rol")
        print("[9] Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion == "1":
            nombre = input("Ingrese el nuevo nombre: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set NombreJugador='"+nombre+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "2":
            apellido = input("Ingrese el nuevo apellido: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set ApellidoJugador='"+apellido+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "3":
            aka = input("Ingrese el nuevo AKA: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set AKAJugador='"+aka+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "4":
            nombre = input("Ingrese el nuevo nombre: ")
            abre = recortar_nombre_pais(nombre)
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set PaisJugador='"+nombre+"', AbreviacionPais='"+abre+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "5":
            equipo = input("Ingresar nuevo equipo: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set EquipoJugador='"+equipo+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "6":
            # ano-mes-dia
            fecha = input("Ingrese la nueva fecha: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set FechaNacimiento='"+fecha+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "7":
            genero = input("Ingrese el nuevo genero: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set Genero='"+genero+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "8":
            rol = input("Ingrese el nuevo rol: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set RolJugador='"+rol+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "9":
            break
        else:
            input("Opcion no valida, presione [ENTER]")


def update_equipo(idequipo, conexion):
    id = input("Ingrese el ID del equipo: ")
    while True:
        print("[1] Modificar nombre del equipo")
        print("[2] Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion == "1":
            equipo = input("Ingrese el nuevo nombre: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE jugador set NombreJugador='"+equipo+"' where JugadorID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "2":
            break
        else:
            input("Opcion no valida, presione [ENTER]")


def update_registro(idregistro, conexion):
    id = input("Ingrese el ID del registro: ")
    while True:
        print("[1] Modificar ID del jugador")
        print("[2] Modificar ID del equipo")
        print("[3] Modificar fecha de inicio")
        print("[4] Modificar fecha de termino")
        print("[5] Salir")
        opcion = input("Ingrese la opcion: ")
        if opcion == "1":
            jugador = input("Ingrese el nuevo ID del jugador: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE registro set JugadorID='"+jugador+"' where RegistroID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "2":
            equipo = input("Ingrese el nuevo ID del equipo: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE registro set EquipoID='"+equipo+"' where RegistroID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "3":
            fecha_inicio = input("Ingrese la nueva fecha de inicio: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE registro set FechaInicio='"+fecha_inicio+"' where RegistroID='" + id + "'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "4":
            fecha_termino = input("Ingrese la nueva fecha de termino: ")
            cursorinsert = conexion.cursor()
            consulta = "UPDATE registro set FechaTermino='"+fecha_termino+"' where RegistroID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
        elif opcion == "5":
            break
        else:
            input("Opcion no valida, presione [ENTER]")


def cambiar_estado(id, estado, conexion):
    cursorinsert = conexion.cursor()
    consulta = "SELECT * from pais"
    cursorinsert.execute(consulta)
    lista = cursorinsert.fetchone()
    cursorinsert.commit()
    cursorinsert.close()
    while True:
        if estado == "si":
            estado = "inactivo"
        elif estado == "no":
            estado = "activo"
        else:
            break
    cursorinsert = conexion.cursor()
    consulta = "UPDATE Pais SET EstadoPais = '" + estado + "' where PaisID='" + id + "'"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()