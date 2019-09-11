#!/usr/bin/python
#-*- coding:UTF-8 -*-
import sys
import math
import random

# la cantidad de cazadores que controlas
busters_per_player = int(input())

# la cantidad de fantasmas en el mapa
ghost_count = int(input())

# si esto es 0, su base está en la parte superior izquierda del mapa
# si es 1, en la parte inferior derecha
my_team_id = int(input())

# fantasmas en el juego
fantasmas = {}

# fantasmas atrapados
fantasmas_atrapados = []

# cazadores por equipo
cazadores = [{},{}]

# tamaño de cuadrado a separar el mapa
cuadrado = 1700

# clase que genera una posición (x,y)
class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# funcion que calcula la distancia entre dos posiciones
def Distancia(posicion_uno, posicion_dos):
    dx = posicion_uno.x-posicion_dos.x
    dy = posicion_uno.y-posicion_dos.y
    return math.sqrt(dx*dx+dy*dy)

# bases de cada equipo según su ID
bases = [Posicion(0,0),Posicion(16000,9000)]

# función para mover al cazador
def Mover(x,y, mensaje):
    return "MOVE %s %s %s" % (x,y,mensaje)

# funcion para cazar un fantasma
def Cazar(id_fantasma):
    return "BUST %s Te caze puto" % id_fantasma

# funcion para soltar un fantasma
def Soltar():
    return "RELEASE Dentrate"

# clase que maneja los parametros básicos de cada jugador (cazador/fantasma)
class Entity(Posicion):
    def __init__(self, entity_id, x, y):
        Posicion.__init__(self, x, y)
        self.entity_id = entity_id
        self.tarea = Funcion(self)
        self.fuera_alcance = False


    def actualizar(self, x, y):
        self.x = x
        self.y = y
        self.fuera_alcance = False

        
    def accion(self):
        self.fuera_alcance = True
        return(self.tarea.accion())

# clase Cazador
class Cazador(Entity):
    def __init__(self, entity_id, x, y, id_team, state, id_fantasma):
        Entity.__init__(self, entity_id, x, y)
        self.id_team = id_team
        self.ocupado = state == 1
        self.id_fantasma = id_fantasma
        self.id_cazado = None
        cazadores[self.id_team][self.entity_id] = self

        
    def actualizar(self, x, y, state, id_fantasma):
        Entity.actualizar(self, x, y)
        self.ocupado = state == 1
        self.id_fantasma = id_fantasma

# clase Fantasma
class Fantasma(Entity):
    def __init__(self, entity_id, x, y, num_cazadores, state):
        Entity.__init__(self, entity_id, x, y)
        self.num_cazadores = num_cazadores
        self.vida = state
        fantasmas[self.entity_id] = self

        
    def actualizar(self, x, y, num_cazadores):
        Entity.actualizar(self, x, y)
        self.num_cazadores = num_cazadores
        self.vida = self.vida - self.num_cazadores


# clase para asignar las funciones
class Funcion:
    def __init__(self, entity, funcion_default=None):
        self.entity = entity

        if funcion_default == None:
            funcion_default = self

        self.funcion_default = funcion_default


    def accion(self):
        return Mover(8000,4500,'ALV')


# clase explorador
class Explorador(Funcion):
    def __init__(self, entity, funcion_default=None):
        # establecemos la funcion y posicion
        Funcion.__init__(self, entity, funcion_default)
        self.x = entity.x
        self.y = entity.y

    def accion(self):
        # si llegó a la posicion que fue enviado
        # calculamos un siguiente movimiento
        if self.entity.x == self.x and self.entity.y == self.y:
            self.x, self.y = self.movimiento()

        # lo movemos a la siguiente posicion
        return Mover(self.x, self.y,'Me voy ALV')

    # calcular un movimiento de forma aleatoria
    def movimiento(self):
        distancia = None
        x = random.randint(500,15500)
        y = random.randint(500,8500)

        for j in range(math.ceil(9000/cuadrado)):
            for i in range(math.ceil(16000/cuadrado)):
                posicion = Posicion(min(16000,i*cuadrado+(cuadrado/2)),min(9000,j*cuadrado+(cuadrado/2)))
                costo = 2100*random.randint(10000,16000)-Distancia(posicion,self.entity)
                if distancia == None or distancia < costo:
                    distancia = costo
                    x = posicion.x
                    y = posicion.y
        return (int(x),int(y))


# clase capturador
class Capturador(Explorador):
    def accion(self):
        # verificar si tiene un fantasma atrapado
        if self.entity.ocupado:
            # determinamos la base correspondiente
            base = bases[self.entity.id_team]

            # verificamos si la distancia es inferior a 1600 unidades
            if Distancia(self.entity, base) < 1600:
                # soltamos el fantasma
                del fantasmas[self.entity.id_fantasma]
                return Soltar()
            else:
                # de lo contrario nos movemos a la base
                return Mover(base.x, base.y,'pa la base putito')

        # variables de distancias
        distancia_minima = 16000*9000
        fantasma_cerca = 0

        # guardar los fantasmas que pueden ser cazados
        cazar = []

        # recorremos los fantasmas disponibles
        for id_fantasma, fantasma in fantasmas.items():
            # verificamos si el fantasma está disponible para atraparlo
            # y si no esta fuera del alcance
            if id_fantasma not in fantasmas_atrapados and not fantasma.fuera_alcance:
                # calculamos la distancia entre el fantasma y el cazador
                distancia = Distancia(self.entity, fantasma)

                # si está entre 900 y 1760 
                if 900 < distancia < 1760:
                    # el fantasma puede ser atrapado
                    # lo guardamos en el array de cazar
                    cazar.append(fantasma)

                elif distancia >= 1760:
                    # de lo contrario establecemos las distancias minimas
                    # hacia el fantasma
                    if distancia_minima > distancia:
                        distancia_minima = distancia
                        fantasma_cerca = fantasma

        # si el array cazar no está vacío
        # cazamos al fantasmas
        if cazar != []:
            if self.entity.id_cazado and fantasmas[self.entity.id_cazado] in cazar:
                return Cazar(self.entity.id_cazado)
            else:
                return Cazar(cazar[0].entity_id)

        # de lo contrario nos movemos hacia el fantasma
        if fantasma_cerca == 0:
            return self.funcion_default.accion()

        return Mover(fantasma_cerca.x, fantasma_cerca.y,'QVERGA')


# funcion para definir las tareas
def Tareas(buster):
    # funciones que desarrolla un cazador
    # E: explorador, C: capturador
    funciones = ['E','C']

    # tarea por default es ninguna
    tarea = None

    # recorremos las funciones
    for funcion in funciones:
        if funcion == "C":
            tarea = Capturador(buster, tarea)
        elif funcion == "E":
            tarea = Explorador(buster, tarea)

    # y la asignamos
    buster.tarea = tarea


# actualizar jugadores (cazadores y fantasmas)
def Jugadores(entity_id, x, y, entity_type, state, value):
    # verificar si es un fantasma
    if entity_type == -1:
        # verificar si ya está guardado en el array
        if entity_id in fantasmas:
            # si esta guardado actualizamos sus parametros
            fantasmas[entity_id].actualizar(x, y, value)
        else:
            # de lo contrario lo guardamos en el array
            Fantasma(entity_id, x, y, value, state)
    else:
        # si no es un fantasma, es un cazador
        # verificamos si está guardado
        if entity_id in cazadores[entity_type]:
            # de estar guardado, actualizamos sus parametros
            cazadores[entity_type][entity_id].actualizar(x, y, state, value)
        else:
            # de no estar guardado lo guardamos
            cazador = Cazador(entity_id, x, y, entity_type, state, value)

            # si el cazador es de mi equipo, le asignamos una tarea
            if entity_type == my_team_id:
                Tareas(cazador)

# loop del juego
while True:
    # la cantidad de cazadores y fantasmas visibles para ti
    entities = int(input())

    for i in range(entities):
        # entity_id: ID del cazador o ID del fantasma
        # y: posición del cazador / fantasma
        # entity_type: ID del equipo si es un cazador, -1 si es un fantasma.
        # state: Para cazadores: 0=inactivo, 1=llevando un fantasma
        # value: Para cazadores: ID del fantasma siendo llevado. Para fantasmas: número de cazadores que intentan atraparlo.
        entity_id, x, y, entity_type, state, value = [int(j) for j in input().split()]
        Jugadores(entity_id, x, y, entity_type, state, value)

    # fantasmas atrapados
    fantasmas_atrapados = [fantasma for fantasma in fantasmas.values() if fantasma.vida <= 0]

    for entity_id in sorted(cazadores[my_team_id].keys()):
        buster = cazadores[my_team_id][entity_id]
        print(str(buster.accion()))

    # definir a los fantasmas atrapados como fuera de alcance
    # para que no se repitan los cazadores en la misma direccion
    for id_fantasma in sorted(fantasmas.keys()):
        fantasma = fantasmas[id_fantasma]
        fantasma.accion()