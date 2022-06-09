# Ingresar elementos de las 3 tablas


def recortar_nombre_pais(pais):
    pais = pais.lower()
    vocales = ('a', 'e', 'i', 'o', 'u')
    for letra in vocales:
        pais = pais.replace(letra, "")
    if len(pais) > 3:
        pais = pais[0:3]
    return pais


def ingreso_jugador(nombre, apellido, aka, pais, equipo, fecha_nacimiento, genero, rol, conexion):
    # los campos no pueden ser vacios, equipo puede ser vacio
    # el aka sea unico
    abre = recortar_nombre_pais(pais)
    cursorinsert = conexion.cursor()
    consulta2 = "if exists (select * from pais where NombrePais = '" + pais + "')" "select PaisID from pais where NombrePais ='" + pais + "' " "else INSERT INTO pais (NombrePais, AbreviacionPais, EstadoPais) VALUES ('" + pais + "', '" + abre + "', 'activo')"
    cursorinsert.execute(consulta2)
    cursorinsert.commit()
    cursorinsert.close()
    cursorinsert = conexion.cursor()
    consulta3 = "if exists (select * from equipo where EquipoNombre = '" + equipo + "')" "select EquipoID from equipo where EquipoNombre = '" + equipo + "' " "else INSERT INTO equipo (EquipoNombre, EquipoEstado) VALUES ('" + equipo + "', 'activo')"
    cursorinsert.execute(consulta3)
    cursorinsert.commit()
    cursorinsert.close()
    cursorinsert = conexion.cursor()
    consulta = "INSERT INTO jugador (NombreJugador, ApellidoJugador," \
               "AKAJugador, PaisJugador, EquipoJugador, FechaNacimiento, Genero, RolJugador, " \
               "EstadoJugador)" \
               " VALUES ('" + nombre + "', '" + apellido + "', '" + aka + "', (select PaisID from pais where NombrePais ='"+pais+"'), (select EquipoID from equipo where EquipoNombre ='"+equipo+"'), '" + fecha_nacimiento + "', '" + genero + "', '" + rol + "', 'activo')"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()


def ingresar_rol(NombreRol, conexion):
    # Falta que no se pueda ingresar de nuevo el mismo rol
    cursorinsert = conexion.cursor()
    consulta = "INSERT INTO rol (NombreRol, EstadoRol) VALUES ('"+NombreRol+"', 'activo')"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()


def ingreso_pais(nombre, conexion):
    # Falta robustez pa que no se caiga cuando se pone uno nuevo, solo bloquear consulta
    abrePais = recortar_nombre_pais(nombre)
    cursorinsert = conexion.cursor()
    consulta = "INSERT INTO pais (NombrePais, AbreviacionPais, EstadoPais) VALUES ('"+nombre+"', '"+abrePais+"', 'activo') "
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()

def ingreso_equipo(nombre, conexion):
    # Robustez
    cursorinsert = conexion.cursor()
    consulta = "INSERT INTO equipo (EquipoNombre, EquipoEstado) VALUES ('" + nombre + "', 'activo')"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()


def ingreso_registro(idjugador, roljugador, idequipo, fechainicio, fechatermino, conexion):
    # Robustez
    cursorinsert = conexion.cursor()
    consulta = "INSERT INTO registro (JugadorID, RolJugador, EquipoID, FechaInicio, FechaTermino, EstadoRegistro) VALUES ('" + idjugador + "','"+roljugador+"', '" + idequipo + "', '" + fechainicio + "', '" + fechatermino + "', 'activo')"
    cursorinsert.execute(consulta)
    cursorinsert.commit()
    cursorinsert.close()


