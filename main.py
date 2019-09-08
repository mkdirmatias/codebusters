import sys
import math

# Send your busters out into the fog to trap ghosts and bring them home!

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