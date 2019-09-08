#!/usr/bin/python
#-*- coding:UTF-8 -*-
import sys
import math

# la cantidad de cazadores que controlas
busters_per_player = int(input())

# la cantidad de fantasmas en el mapa
ghost_count = int(input())

# si esto es 0, su base está en la parte superior izquierda del mapa, si es 1, en la parte inferior derecha
my_team_id = int(input())

# fantasmas en el juego
fantasmas = {}

# fantasmas atrapados
fantasmas_atrapados = []

# cazadores por equipo
cazadores = [{},{}]

# clase que genera una posición (x,y)
class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# bases de cada equipo según su ID
bases = [Posicion(0,0),Posicion(16000,9000)]

# función para mover al cazador
def Mover(x,y):
    return "MOVE %s %s" % (x,y)

# funcion para cazar un fantasma
def Cazar(id_fantasma):
    return "BUST %s" % id_fantasma

# funcion para soltar un fantasma
def Soltar():
    return "RELEASE"

# loop
while True:
	# la cantidad de cazadores y fantasmas visibles para ti
    entities = int(input())

    for i in range(entities):
        # entity_id: ID del cazador o ID del fantasma
        # y: posición de este cazador / fantasma
        # entity_type: ID del equipo si es un cazador, -1 si es un fantasma.
        # state: Para cazadores: 0=inactivo, 1=llevando un fantasma
        # value: Para cazadores: ID del fantasma siendo llevado. Para fantasmas: número de cazadores que intentan atraparlo.
        entity_id, x, y, entity_type, state, value = [int(j) for j in input().split()]

    for i in range(busters_per_player):
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # MOVE x y | BUST id | RELEASE
        print("MOVE 8000 4500")