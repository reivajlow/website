# visualizar los elementos de las 3 tablas

def visu_jugador(idjugador, conexion):
    id = input("Ingrese el ID del jugador: ")
    cursorinsert = conexion.cursor()
    consulta = "Select * from jugador where JugadorID='"+id+"' and EstadoJugador='activp'"
    cursorinsert.execute(consulta)
    jugador = cursorinsert.fetchall()
    """
    for i in jugador:
        print("El ID del jugador es", i[0])
        print("El nombre del jugador es", i[1])
        print("El apellido del jugador es", i[2])
        print("El AKA del jugador es", i[3])
        print("El pais del jugador es", i[4])
        print("La abreviacion del pais del jugador es", i[5])
        print("El equipo del jugador es", i[6])
        print("La fecha de nacimiento del jugador es", i[7])
        print("El genero del jugador es", i[8])
        print("EL rol del jugador es", i[9])
    """
    cursorinsert.commit()
    cursorinsert.close()
    return jugador


def visu_pais(idpais, conexion):
    id = input("Ingrese el ID del pais: ")
    cursorinsert = conexion.cursor()
    consulta = "Select * from pais where PaisID='"+id+"' and EstadoPais='activo'"
    cursorinsert.execute(consulta)
    # una fila de 3 columnas
    pais = cursorinsert.fetchall()
    """
    for i in pais:
        print("El ID es", i[0])
        print("El nombre del pais es", i[1])
        print("La abreviacion del pais es", i[2])
    """
    cursorinsert.commit()
    cursorinsert.close()
    return pais


def visu_equipo(idequipo, conexion):
    id = input("Ingrese el ID del equipo: ")
    cursorinsert = conexion.cursor()
    consulta = "Select * from equipo where EquipoID='"+id+"' and EquipoEstado='activo'"
    cursorinsert.execute(consulta)
    equipo = cursorinsert.fetchall()
    """
    for i in equipo:
        print("El ID del equipo es", i[0])
        print("El nombre del equipo es", i[1])
    """
    cursorinsert.commit()
    cursorinsert.close()
    return equipo


def visu_registro(idregistro, conexion):
    id = input("Ingrese el ID del registro: ")
    cursorinsert = conexion.cursor()
    consulta = "Select * from registri where RegistroID='" + id + "' and EstadoRegistro='activo'"
    cursorinsert.execute(consulta)
    registro = cursorinsert.fetchall()
    """
    for i in equipo:
        print("El ID del equipo es", i[0])
        print("El nombre del equipo es", i[1])
    """
    cursorinsert.commit()
    cursorinsert.close()
    return registro


if __name__=="__main__":
    pass
    #visu_jugador()
    #visu_pais()
    #visu_equipo()
