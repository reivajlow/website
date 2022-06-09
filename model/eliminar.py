# eliminar (cambiar el estado) de los elementos en las tablas
from model.leer import *


def matar_jugador(id, conexion):
    cursorinsert = conexion.cursor()
    consulta = "UPDATE jugador set EstadoJugador='inactivo' where JugadorID='"+id+"'"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()


def matar_pais(idpais, conexion):
    id = input("Ingrese el ID del pais a modificar el estado: ")
    pais = visu_pais()
    """
    cursorinsert = conexion.cursor()
    consulta = "Select * from pais where PaisID='"+id+"' and EstadoPais='activo'"
    cursorinsert.execute(consulta)
    # una fila de 3 columnas
    pais = cursorinsert.fetchall()
    for i in pais:
        print("El ID es", i[0])
        print("El nombre del pais es", i[1])
        print("La abreviacion del pais es", i[2])
    cursorinsert.commit()
    cursorinsert.close()
    """
    while True:
        va = input("En caso de querer confirmar la operacion ingrese 1, caso contrario 2: ")
        if va == "1":
            cursorinsert = conexion.cursor()
            consulta = "UPDATE pais set EstadoPais='inactivo' where PaisID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
            break
        elif va == "2":
            break
        else:
            input("Opcion no valida, presione [ENTER]")


def matar_equipo(idequipo, conexion):
    id = input("Ingrese el ID del equipo a modificar: ")
    equipo = visu_equipo()
    """
    cursorinsert = conexion.cursor()
    consulta = "Select * from equipo where EquipoID='" + id + "' and EquipoEstado='activo'"
    cursorinsert.execute(consulta)
    equipo = cursorinsert.fetchall()
    for i in equipo:
        print("El ID del equipo es", i[0])
        print("El nombre del equipo es", i[1])
    cursorinsert.commit()
    cursorinsert.close()
    """
    while True:
        va = input("En caso de querer confirmar la operacion ingrese 1, caso contrario 2: ")
        if va == "1":
            cursorinsert = conexion.cursor()
            consulta = "UPDATE equipo set EquipoEstado='inactivo' where EquipoID='" + id + "'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
            break
        elif va == "2":
            break
        else:
            input("Opcion no valida, presione [ENTER]")


def matar_registro(idregistro, conexion):
    id = input("Ingrese el ID del registro a mostrar: ")
    registro = visu_registro()
    """
    cursorinsert = conexion.cursor()
    consulta = "Select * from registri where RegistroID='" + id + "' and EstadoRegistro='activo'"
    cursorinsert.execute(consulta)
    registro = cursorinsert.fetchall()
    for i in registro:
        print("El ID del equipo es", i[0])
        print("El nombre del equipo es", i[1])
    cursorinsert.commit()
    cursorinsert.close()
    """
    while True:
        va = input("En caso de querer confirmar la operacion ingrese 1, caso contrario 2: ")
        if va == "1":
            cursorinsert = conexion.cursor()
            consulta = "UPDATE registro set EstadoRegistro='inactivo' where RegistroID='"+id+"'"
            cursorinsert.execute(consulta)
            cursorinsert.commit()
            cursorinsert.close()
            break
        elif va == "2":
            break
        else:
            input("Opcion no valida, presione [ENTER]")


if __name__ == "__main__":
    pass
    #matar_pais()
    #matar_registro()
    #matar_jugador()
    #matar_registro()
