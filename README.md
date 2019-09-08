# CODEBUSTERS
**Tarea Evaluativa Nº 2** - Agentes Inteligentes

**Curso:** Inteligencia Artificial

**Código:** IN1070C

**Año:** 2019


## Objetivo

Capturar una cantidad de fantasmas mayor que el equipo rival.

## Reglas

El juego se desarrolla en un mapa de 16001 unidades de ancho y 9001 de alto. La coordenada X=0, Y=0 se
corresponde con el extremo superior izquierdo.

Cada jugador controla un equipo de varios cazafantasmas. Cada equipo comienza en esquinas opuestas del
mapa, cerca de su base. Los fantasmas se encuentran dispersos en el mapa y deben ser capturados y devueltos
a la base. Cada fantasma en la base o atrapado por un cazafantasma cuenta un punto para el jugador. Sin
embargo, puede perderse un punto si un cazafantasma libera a un fantasma fuera de la base.

## Organización del Mapa

- Siempre habrá exactamente dos equipos en el juego

- Al comenzar el juego cada competidor recibe un ID que indica en qué extremo del mapa tendrá su base. El extremo superior izquierdo (X=0, Y=0) corresponde al equipo con ID=0. El extremo inferior derecho (X=16000, Y=9000) corresponde al jugador con ID=1.

- La niebla hace imposible conocer las posiciones de los fantasmas y de los cazadores del equipo contrario a menos que se encuentren dentro de un radio de 2200 unidades de alguno de los cazafantasmas propios.

- Los cazadores y los fantasmas tienen un ID propio. No hay dos cazadores con el mismo ID ni tampoco
dos fantasmas con el mismo ID. Sin embargo, un fantasma y un cazador pueden tener el mismo ID.

## Funcionamiento de los cazafantasmas

-  En cada turno, el cazafantasma puede realizar una de las siguientes acciones: **MOVE** , **BUST** o **RELEASE**

- **MOVE** , seguido de dos enteros X Y separados por espacios indicando coordenadas del mapa. Esta acción hará que el cazafantasma avance 800 unidades en dirección a ese punto. Notar que si la coordenada (X, Y) se encuentra a una distancia menor de 800 unidades entonces el cazafantasma solo avanzará la
distancia necesaria para llegar al destino indicado.

- **BUST** , seguido del ID de un fantasma provocará que éste sea capturado en la trampa cazafantasmas si se encuentra a una distancia 900 <= D <= 1760 del cazador. Fantasmas fuera de este rango no serán capturados. Los fantasmas capturados dejarán de ser visibles en el mapa. Notar que, aunque el fantasma
se encuentre en el rango indicado no será capturado inmediatamente. Tener en cuenta condiciones adicionales que se explican posteriormente. Un cazador no puede llevar más de un fantasma a la vez.

- **RELEASE** , causará que el cazador libere al fantasma, si es que lleva uno. Si esta acción se realiza a una
distancia menor que 1600 unidades del extremo correspondiente al jugador entonces el fantasma se retira del juego y se considera seguro dentro de la base y garantiza el punto al equipo.

## Funcionamiento de los fantasmas
- Los fantasmas permanecen estacionarios salvo que un cazafantasma se acerque a menos de 2200 unidades y no esté intentando capturarlo. Puede haber varios cazafantasmas en este rango. En esta circunstancia, el fantasma escapará 400 unidades alejándose del cazafantasma más cercano. Si hay varios cazadores situados a la misma distancia, y ésta es la mínima, entonces el fantasma intentará
alejarse de la posición media de los cazadores.

- Si hay varios cazadores intentando atrapar a un mismo fantasma, el equipo con la mayor cantidad de cazafantasmas tendrá la prioridad. Dentro de este equipo, el cazador más próximo al fantasma será quien lo capture. Si ambos equipos tienen igual cantidad de cazadores intentando atrapar al fantasma, entonces este no será atrapado durante el turno actual.

- Un fantasma que es transportado por un cazafantasma escapará si este intenta atrapar a otro fantasma.

## Entrada y Salida

Su programa debe leer primero los datos de inicialización desde la entrada estándar y, a continuación, en un
bucle infinito, leer los datos contextuales del juego (cantidad de entidades visibles, sus coordenadas etc.) y
escribir en la salida estándar las acciones de cada cazafantasma. El protocolo se detalla a continuación.

**Entrada para la fase de inicialización**

- Línea 1 un entero **bustersPerPlayer** , indicando la cantidad de cazafantasmas que cada equipo controla.

- Línea 2, un entero **ghostCount** indicando la cantidad de fantasmas que se encuentran en el mapa.

-  Línea 3, un entero **myTeamId** indicando su equipo.

**Entrada en cada turno:**

En cada turno, el estado del juego se suministra como una lista de entidades cada una con el ID, posición, tipo,
estado y valor. Cada elemento con el significado que a continuación se detalla:

**Tipo:**

-  0 para los cazafantasmas del equipo 0.
- 1 para los cazafantasmas del equipo 1.
- \-1 para los fantasmas.

**Estado:**

 - Para los cazafantasmas:
   -  0 si no tiene atrapado ningún fantasma.
    - 1 si lleva algún fantasma.

- Para los fantasmas:
   - El estado siempre es 0

Línea 1 un entero **entities** que indica la cantidad de **entindades** en el mapa (fantasmas y cazadores)
visibles.

Siguientes **entities** líneas, 6 enteros separados por espacio **entityId x y entityType state value** indicando información relativa a cada fantasma o cazador. Los valores x , y indican las coordenadas de la entidad.


## Salida durante cada turno

- Una línea por cada cazafantasma de acuerdo al siguiente formato:
   - MOVE X Y MSG
   - BUST ghostID MSG
   - RELEASE MSG

En las instrucciones anteriores, MSG es un mensaje de texto opcional que se mostrará junto al cazafantasma al realizar la acción.


## Condiciones de Victoria:
- Ganará el jugador que haya capturado mayor cantidad de fantasmas al finalizar el juego.

-  El juego termina una vez que todos los fantasmas han sido capturados o luego de un tiempo límite igual a 250 turnos.


## Condiciones de Derrota

- El programa produce una salida no reconocida, es decir diferentes a las antes especificadas.

- Se agota el tiempo de respuesta, que serán 100ms.

- El equipo tiene menos fantasmas que el oponente al finalizar el juego.

## Otras consideraciones

- La posición inicial de cada fantasma es aleatoria. Sin embargo, las posiciones son simétricas con respecto a la base de cada equipo.

-  Los fantasmas se mueven un turno después de que algún cazafantasma entre a su radio de visión.

- Si un fantasma o un cazador intenta salirse de los límites del mapa, es colocado en la posición más cercana dentro del mapa.