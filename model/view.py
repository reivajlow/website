

def ver_jugadores(conexion):
    cursor = conexion.cursor()
    consulta = "SELECT JugadorID, NombreJugador, AKAJugador from Jugador where EstadoJugador = 'activo'"
    cursor.execute(consulta)
    resu = cursor.fetchall()
    cursor.commit()
    cursor.close()
    return resu


def ver_jugador(id, conexion):
    cursor = conexion.cursor()
    consulta = "SELECT JugadorID, NombreJugador, ApellidoJugador, AKAJugador, (Select NombrePais from pais where PaisID = PaisJugador), (Select EquipoNombre from equipo where EquipoID = EquipoJugador), FechaNacimiento, Genero, RolJugador  from Jugador where JugadorID = '" + id + "' and EstadoJugador = 'activo'"
    cursor.execute(consulta)
    resu = cursor.fetchall()
    cursor.commit()
    cursor.close()
    return resu


def get_estado(id, conexion):
    cursor = conexion.cursor()
    consulta = "SELECT EstadoJugador from Jugador where JugadorID = '" + id + "' and EstadoJugador = 'activo'"
    cursor.execute(consulta)
    resu = cursor.fetchall()
    cursor.commit()
    cursor.close()
    return resu


# tomar los elementos de la lista del jugador que ya conocemos
# lista_modifcada son todos los atgributos modificados
def agregar_los_vacios(id, lista_modificada, conexion):
    cursorinsert = conexion.cursor()
    consulta = "SELECT * from Jugador"
    cursorinsert.execute(consulta)
    lista = cursorinsert.fetchone()
    cursorinsert.commit()
    cursorinsert.close()
    while True:
        if lista_modificada[1] == "":
            lista_modificada[1] = lista[1]
        elif lista_modificada[2] == "":
            lista_modificada[2] = lista[2]
        elif lista_modificada[3] == "":
            lista_modificada[3] = lista[3]
        elif lista_modificada[4] == "":
            lista_modificada[4] = lista[4]
        elif lista_modificada[5] == "":
            lista_modificada[5] = lista[5]
        elif lista_modificada[6] == "":
            lista_modificada[6] = lista[6]
        elif lista_modificada[7] == "":
            lista_modificada[7] = lista[7]
        elif lista_modificada[8] == "":
            lista_modificada[8] = lista[8]
        else:
            break
    #print(lista, lista_modificada, lista_modificada)
    cursorinsert = conexion.cursor()
    consulta = "UPDATE Jugador SET NombreJugador='" + lista_modificada[1] + "', ApellidoJugador='" + lista_modificada[2] + "', AKAJugador='" + lista_modificada[3] + "', PaisJugador=(select PaisID from pais where NombrePais ='"+lista_modificada[4]+"'), EquipoJugador=(select EquipoID from equipo where EquipoNombre ='"+lista_modificada[5]+"'), FechaNacimiento='" + lista_modificada[6] + "', Genero='" + lista_modificada[7] + "', RolJugador='" + lista_modificada[8] + "' where JugadorID='"+id+"'"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()

def visu_pais(conexion):
    cursorinsert = conexion.cursor()
    consulta = "Select * from pais where EstadoPais='activo'"
    cursorinsert.execute(consulta)
    paises = cursorinsert.fetchall()
    cursorinsert.commit()
    cursorinsert.close()
    return paises


def visu_pais1(ide, conexion):
    cursorinsert = conexion.cursor()
    consulta = "Select * from pais where PaisID='"+ide+"' and EstadoPais='activo'"
    cursorinsert.execute(consulta)
    pais1 = cursorinsert.fetchall()
    cursorinsert.commit()
    cursorinsert.close()
    return pais1