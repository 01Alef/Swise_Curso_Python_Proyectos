######################################################################
"""
Juego: Escapar de Honduras.

Mision: Es un juego del tipo trivias en el que el Personaje va a elegir un destino, a que se quiere dedicar en la vida, al elegir su carrera debe ser capaz de resolver ciertos desafíos, estos desafios serán trivias en un tiempo estimado, si logra resolverlos podrá terminar su carrera, luego deberá enfrentarse a un desafio final, el cual le permitirá salir de Honduras.

"""
#####################################################################

"""
MEJORAR LA CLASE PARA EL OTRO STR
"""


import numpy as np
import pandas as pd
import os
import time as t

class  Personaje(object):
    """Este Personaje se irá creando segun las indicaciones del jugador"""

    def __init__(self, nombre, edad, sexo):
        super( Personaje, self).__init__()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return(self.nombre)

    def age(self):
        return(self.edad)


class Joh(object):
    """docstring for ."""

    def __init__(self, cargo):
        super(Joh, self).__init__()
        self.cargo = cargo

    def __str__(self):
        return(self.cargo)

seguir = ""

while True:
    print(""" Bienvenido, el único fin de este juego es salir de Honduras, esto fin será posible mediante las desiciones que usted tome y un desafío final.

    Honduras, es un lugar utópico, en el cual las oportunidades de salir adelante son un tanto dificiles para la mayoria de las personas, utópico porque desde sus inicios las ideas de un país digno solo se quedaron en el colectivo imaginario, solo con la idea de progreso pero sin progresar, un lugar hundido en la corrupción que la unica manera de progresar es salir del lugar.

    Para iniciar, ingrese sus datos para crear su personaje:
    """)

    Nombre = str(input("Nombre: "))
    Edad = int(input("Edad: "))
    sex = str(input("género (puede ser un Saiyajin si quiere :D): "))

    os.system("clear")

    datos_usuario = Personaje(Nombre, Edad, sex)

    t.sleep(1)
    print("\n ...................................................")
    print("\n Imagine que se escucha una cancion de polache de fondo")
    print("\n ...................................................\n")
    t.sleep(3)

    if sex == "mujer":
        print(f"{datos_usuario.__str__()}, una {sex} que desafortunadamente nació en Honduras, ahora está intentando escapar a la edad de {datos_usuario.age()} años.")
        print("""
        Antes debe superar muchas pruebas para poder finalmente salir de Honduras, una de ellas es hacer una elección correcta de la carrera que lo llevará a su destino, luego, al final deberá enfrentarse a un desafío.

         """)
    else:
        print(f"{datos_usuario.__str__()}, un {sex} que desafortunadamente nació en Honduras, ahora está intentando escapar a la edad de {datos_usuario.age()} años.")
        print("""
        Antes debe superar muchas pruebas para poder finalmente salir de Honduras, una de ellas es hacer una elección correcta de la carrera que lo llevará a su destino, luego, al final deberá enfrentarse a un desafío.

         """)

    t.sleep(3)
    print("\n ...................................................")
    print("\n sigue sonando una cancion de polache de fondo ")
    print("\n ...................................................\n")
    t.sleep(3)
    print("¿Estaba imaginando la cancion que se llama 'Pedazo de mujer' de polache?")
    d = input("si/no: ")
    if d == "si":
        print("\n Interesante :)")
        t.sleep(3)
        print("\n ...................................................")
        print("\n sigue sonando una cancion de polache de fondo")
        print("\n ...................................................\n")
        t.sleep(3)
    else:
        print("\n ...................................................")
        print("\n sigue sonando una cancion de polache de fondo, la que imaginó seguramente.")
        print("\n ...................................................\n")
        t.sleep(3)

    os.system("clear")



    seguir2 = ""

    while True:

        print("""Elija una carrera de vida:

        1. Matemáticas.
        2. Física.
        3. Astronomía.
        4. Química.

        Nota: Si por ejemplo elige fisica, escriba la palabra Física, luego entrará al desafío.
        """)



        area = str(input("Elija una área: "))

        contador = 0

        for i in range(contador < 5):
            contador += 1

            if (area == "Matemáticas" or area == "matemáticas" or area == "matematicas"):
                print("""

                seleccione la respuesta correcta
                ¿Qué es el gradiente?
                a) El gradiente representa la pendiente de la línea tangente a la gráfica de una función.
                b) Es una derivada.
                c) Es el cambio de la posición con respecto a al espacio.
                """)
                respuesta_1 = str(input("Respuesta = "))
                print(" su respuesta es:",respuesta_1)
                if (respuesta_1 == "a"):
                    print("respuesta correcta :D ")
                else:
                    print("incorrecta")

                print("""

                ¿Qué es una matriz?
                a) es una arreglo de numeros.
                b) una matriz es un conjunto ordenado en una estructura de filas y columnas.
                c) es una serie.

                """)

                respuesta_2 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_2)
                if respuesta_2 == "b":
                    print("respuesta correcta :D\n")
                else:
                    print("incorrecta")

                print("""

                ¿Defina la factorización?
                a) Se utiliza para simplificar la tarea de encontrar la solución de ecuaciones, simplificar expresiones y en general para facilitar su manipulación.
                b) Arreglo de variables en una ecuación.
                c) Es una técnica para simplificar una ecuación.

                """)

                respuesta_3 = str(input("Respuesta = "))
                print("su respuesta es:", respuesta_3)

                if respuesta_3 == "a":
                    print("respuesta correcta :D\n")
                else:
                    print("incorrecta")

            elif  (area == "Física" or area == "fisica" or area == "física"):
                print("""

                ¿Qué es el efecto de coriolis?
                a) El efecto Coriolis hace que un objeto que se mueve sobre el radio de un disco en rotación tienda a acelerarse con respecto a ese disco según si el movimiento es hacia el eje de giro o alejándose de este.
                b) Es una fuerza que actua cuando un objeto va en caida libre.
                c) Es un efecto producido por la gravedad.

                """)

                respuesta_1 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_1)
                if respuesta_1 == "a":
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

                print("""

                ¿Qué es la ley de Ampere?
                a) La ley de Ampère explica que la circulación de la intensidad del campo magnético en un contorno cerrado es proporcional a la corriente que recorre en ese contorno.
                b) Nos esplica como funciona el campo magnetico y electrico alrededor de una espira.
                c) Nos da el valor exacto del campo magnetico.
                """)

                respuesta_2 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_2)
                if respuesta_2 == "a":
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

                print("""

                ¿Qué es la velocidad de grupo?
                a) La velocidad de grupo es la velocidad de la envolvente.
                b) Es la velocidad a la cual se mueve un electrón.
                c) Es la velocidad a la cual se mueve un proyectil.
                """)

                respuesta_3 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_3)
                if respuesta_3 == "b":
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

            elif (area == "Química" or area == "química" or area == "quimica"):
                print("""

                ¿Qué es la quimica?

                a) Ciencia que estudia la composicion y propiedades de la materia.
                b) Ciencia que estudia la cantidad de amor que tienes tu con tu pareja.
                c) Ciencia que estudia la composicion y conocimientos de la materia.

                """)

                respuesta_1 = str(input("Respuesta = "))
                print(" su respuesta es:",respuesta_1)
                if (respuesta_1 == "a"):
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

                print("""

                ¿Que es el atomo?
                a) Es una particula subatomica
                b) Es la unidad basica de la quimica
                c) Es la unidad basica de la fisica
                """)
                respuesta_2 = str(input("Respuesta = "))
                print(" su respuesta es:",respuesta_2)
                if (respuesta_2 == "b"):
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

                print("""
                ¿Cuantos elementos quimicos hay en la tabla periodica actualmente?
                a) 118
                b) 117
                c) 119
                """)
                respuesta_3 = str(input("Respuesta = "))
                print(" su respuesta es:",respuesta_3)
                if (respuesta_3 == "a"):
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

            elif  (area == "Astrofísica" or area == "astrofísica" or area == "astrofica"):

                print("""

                ¿Qué es astronomía de posición?
                a) Nos ayuda a posicionarnos en la esfera celeste.
                b) Nos da la ubicación precisa de una estrella.
                c) Nos sirve para localizar un objeto en la esfera celeste la posición de los astros, hallando los distintos ángulos y coordenadas astronómicas respecto a los planos fundamentales.
                """)
                respuesta_1 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_1)
                if respuesta_1 == "c":
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

                print("""

                ¿Qué es la constante de Hubble?
                a) Es un valor que nos dice cuanto se expande el universo.
                b) Es una ley de la física que establece que el corrimiento al rojo de una galaxia es proporcional a la distancia a la que está.
                c) Nos ayuda a comprender la materia oscura.
                """)

                respuesta_2 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_2)
                if respuesta_2 ==  "b":
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

                print("""

                ¿Qué es la cosmología?
                a) Estudia el nacimiento y evolución de las estrellas.
                b) Rama de la astronomí que se encarga de la expanción del universo.
                c) Se ocupa del estudio de las leyes generales del origen del mundo y la evolución del universo.

                """)

                respuesta_3 = str(input("Respuesta = "))
                print("su respuesta es :", respuesta_3)
                if respuesta_3 == "c":
                    print("respuesta correcta :D")
                else:
                    print("incorrecta")

            else:
                print("esta opción no es valida")
                break

        print("")
        seguir2 = str(input("¿Quieres elegir otra carrera? (si/no): "))
        if(seguir2 == "no"):
            break
        os.system("clear")

    os.system("clear")

    print(f"Al haber avanzado o fracasado en su carrera profesional, {datos_usuario.__str__()}, ha decidido abandonar su pais de origen, de esta manera podrá triunfar en la vida, pero ahora debe cumplir un último desafío, el cual es vencer al villano que aterroriza al pais:")

    t.sleep(6)

    final = ""

    while True:
        print("\n ...................................................")
        print("\n Suena Requiem in D menor de Mozart uwu ")
        print("\n ...................................................\n")
        t.sleep(3)

        print("""

        ****************************************************************
        ************************ DESAFÍO FINAL *************************

        VILLANO: JUAN ORLANDO HERNANDEZ (JOH).
        VIDAS : 3

        Instrucciones: Consigue quitarle las 3 vidas al contestar correctamente las siguientes preguntas:

        """)

        cargo_1 = str(input("¿Cargo actual que desempeña el villano?: "))
        villano = Joh(cargo_1)

        print(f"JOH atualmente ocupa el cargo de {villano.__str__()}, por lo cual lo debes derrotar contestando las siguientes preguntas: \n")

        vida = 3
        for i in range(3):
            print("¿Qué se necesita para que desaparezca la corrupción estatal?")
            print("a) Quitarle poder al estado.")
            print("b) Votar por el partido libre")
            print("c) Votar por otro partido político menos el Partido Nacional")
            resp_1 = str(input("Respuesta = "))
            print("Su respuesta es:",resp_1)
            if (resp_1 == "a"):
                vida = vida - 1
                print("BIEN!, lo heriste, sigue asi, aun le queda 2 de hp")
            else:
                print("Incorrecto :( suerte a la proxima")
            print(" ")
            print("¿Qué se ocupa para que Honduras Prospere?")
            print("a) Liberar la economía y aplicar las leyes del libre mercado.")
            print("b) Darle mas poder al estado.")
            print("c) Aplicar las ideas de Marx")
            resp_2 = str(input("Respuesta = "))
            print("Su respuesta es:",resp_2)
            if (resp_2 == "a"):
                vida = vida - 1
                print("BIEN!, lo heriste, sigue asi")
            else:
                print("Incorrecto :( suerte a la proxima")
            print(" ")
            print("¿Dónde está el dinero?")
            print("a) En cualquier lado.")
            print("b) JOH se lo robó")
            print("c) Están invertidos en los hospitales móviles.")
            resp_3 = str(input("Respuesta = "))
            print("Su respuesta es:",resp_3)
            if (resp_3 == "b"):
                vida = vida - 1
                print("BIEN!, lo heriste")
            else:
                print("Incorrecto :(")

            if vida == 0:
                print(" BIEEEEN, HAS MATADO A JOH, HONDURAS ES LIBREEE GRACIAS A VOS")
                print(" ")
            if vida == 1:
                print("UFFF CASI :(, pero lo intetaste, y lo dejaste moribundo, Bien.")
                print(" ")

            else:
                print("Quedó vivo :(")
                break

        if vida == 0:
            print(" ")
            print("Aqui tiene su visa de salida de salida de Honduras, feliz viaje :D: ")
            print(" ")
            print("******************************************************")
            print("******************************************************")
            print("*************** VISA PARA CUALQUIER LADO ************")
            print(f"***{datos_usuario.__str__()} ***************************")
            print(f"*** genero: {sex} **********************************")
            print(f"*** Edad: {datos_usuario.age()} ***************************")
            print(f"*** Destino: Cualquier pais fuera de Latinoamerica *** ")
            print("******************************************************")
            print("******************************************************")


        final = str(input("¿Quieres intentarlo de nuevo? (si/no)//(Si lo has matado escribe no.):  "))
        if(final == "no"):
            break
        os.system("clear")



    os.system("clear")
    try:
        seguir = str(input("\t¿Desea jugar de nuevo? (si/no): "))
        assert(len(seguir) == 2)
    except Assertion_Error:
        print("\nHa ingresados mas caracteres de los requerido o bien ha ingresado la palabra en mayusculas.")
        print("No ha ingresado las palabras que se le indican, 'si' para una respuesta afirmativa para volver a jugar, 'no' para salir del juego.")

    os.system("clear")

    if(seguir=="no"):
        print("Gracias por jugar :D")
        break
