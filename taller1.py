import pandas as pd
from pyswip import Prolog

""""
El archivo games.txt contiene la base de conocimietos a ocupar:
** Por cada juego se debe agregar: 
- categoria (arcade, puzzle, plataforma, etc)
- duracion del speedrun basada en el actual world record (larga, media, corta)
- antiguedad del juego (antiguo o nuevo)
- dificultad del juego (facil, media o dificil)
- caracteristicas adicionales (juego de disparos, de ingenio, etc)

** Respecto a las preguntas
El objetivo es determinar una categoría que al usuario le gustaría respecto a sus respuestas
y mostrarle opciones dentro de esa categoria que cumplan sus requerimientos.

Preguntas:
¿Cuanto tiempo dispone para jugar? Mucho - moderado - poco 
¿Que antiguedad de juegos le gustaría? antiguos - nuevos
¿Que tan bueno se considera en juegos? Excelente - regular - novato
¿Tiene preferencia por alguna caracteristica extra ? 
"""
# Se fija como variable global
prolog = Prolog()


# Permite cargar la base de conocimientos contenida en otro archivo.
# Entrada: nombre del archivo.
# Salida: True si logro hacer la operación.
def cargarBaseConocimientos(nombreArchivo):
    file = open(nombreArchivo, 'r')
    for linea in file:
        lineaSeparada = linea.replace("\n", "").split("-")
        agregarJuego(lineaSeparada[0], lineaSeparada[1])
    file.close()
    return True


# Permite cargar un juego a la base de conocimientos
# Entrada: Dos strings, una correspondiente al juego y la otra a la caracteristica de este
# Salida:
def agregarJuego(juego, caracteristica):
    juego = "game('" + juego + "','" + caracteristica + "')"
    prolog.assertz(juego)


# Muestra por pantalla toda la base de conocimiento y sus hechos, requiere que exista una base de conocimientos creada
# Entrada:
# Salida:
def mostrarBaseConocimiento():
    for soln in prolog.query("game(Juego, Caracteristica)"):
        print("[Juego] " + soln["Juego"] + ": " + soln["Caracteristica"])


# Permite conseguir los juegos que cumplan con todas las caracteristicas ingresadas
# Entrada: una lista que contiene como string caracteristicas
# Salida: una lista con los juegos que cumplen con todas las caracteritsticas
def juegosPorCaracteristicas(caracteristicas):
    resultados_df = pd.DataFrame()
    for c in caracteristicas:
        juegos = []
        # Consulta
        query = "game(Juego,'" + c + "')"
        # Respuesta, devuelve un juego
        response = list(prolog.query(query))
        for juego in response:
            # Se verifica que el juego conseguido efectivamente tenga todas las caracteristicas de la lista - Pendiente
            juegos.append(juego)
        juegos_df = pd.DataFrame(juegos)
        if resultados_df.shape[0] != 0:
            resultados_df = pd.merge(resultados_df, juegos_df, how='inner', on='Juego')
        else:
            resultados_df = juegos_df

    return resultados_df


"""
Ejemplos de consultas:
- Muestra todos los juegos clasificados como plataforma:
print(list(prolog.query("game(Juego,dificultad facil)")))
- Muestra un juego clasificado como dificultad facil (Por algun motivo no funciona si se ingresa directamente la string)
x = "dificultad facil"
print(list(prolog.query("game(Juego,dificultad facil)")))
"""


def main():
    prolog.consult('base.pl')
    #cargarArchivo = cargarBaseConocimientos("games.txt")
    #mostrarBaseConocimiento()
    #x = "dificultad facil"
    #print(list(prolog.query("game(Juego,dificultad facil)")))
    #print(list(prolog.query("game(Juego,'"+x+"')")))
    #print(juegosPorCaracteristicas(["sandbox","nuevo"])) -> pendiente
    #print(juegosPorCaracteristicas(["sandbox","nuevo"]))
    #print(juegosPorCaracteristicas(["antiguo","dificultad media"]))
    consulta = list(prolog.query("game(G,X,dur_media,antiguo,J,L)"))
    print(consulta)


# Ejecuta el programa en la función principal
main()
