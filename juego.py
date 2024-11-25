import pygame
import random

# Configuración del juego
ANCHO, ALTO = 600, 600
TAMANIO_CASILLA = ANCHO // 10

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)

# Configuración de serpientes y escaleras
serpientes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 87: 24, 93: 73, 95: 75, 98: 78}
escaleras = {2: 38, 7: 14, 8: 31, 15: 26, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98}

# Inicializar Pygame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Serpientes y Escaleras Mejorado")
fuente = pygame.font.Font(None, 36)

# Función para dibujar el tablero
def dibujar_tablero():
    for fila in range(10):
        for columna in range(10):
            x = columna * TAMANIO_CASILLA
            y = (9 - fila) * TAMANIO_CASILLA
            color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
            pygame.draw.rect(pantalla, color, (x, y, TAMANIO_CASILLA, TAMANIO_CASILLA))

            # Número de la casilla
            numero = fila * 10 + columna + 1 if fila % 2 == 0 else fila * 10 + (9 - columna) + 1
            texto = fuente.render(str(numero), True, VERDE if color == BLANCO else ROJO)
            pantalla.blit(texto, (x + 5, y + 5))

# Dibujar las serpientes y escaleras
def dibujar_serpientes_escaleras():
    for inicio, fin in escaleras.items():
        dibujar_linea_tablero(inicio, fin, VERDE)
    for inicio, fin in serpientes.items():
        dibujar_linea_tablero(inicio, fin, ROJO)

def dibujar_linea_tablero(inicio, fin, color):
    x1, y1 = obtener_posicion_tablero(inicio)
    x2, y2 = obtener_posicion_tablero(fin)
    pygame.draw.line(pantalla, color, (x1, y1), (x2, y2), 5)

def obtener_posicion_tablero(casilla):
    fila = (casilla - 1) // 10
    columna = (casilla - 1) % 10 if fila % 2 == 0 else 9 - (casilla - 1) % 10
    x = columna * TAMANIO_CASILLA + TAMANIO_CASILLA // 2
    y = (9 - fila) * TAMANIO_CASILLA + TAMANIO_CASILLA // 2
    return x, y

# Función para mover al jugador
def mover_jugador(posicion, dado):
    nueva_posicion = posicion + dado
    if nueva_posicion > 100:
        return posicion
    if nueva_posicion in serpientes:
        return serpientes[nueva_posicion]
    if nueva_posicion in escaleras:
        return escaleras[nueva_posicion]
    return nueva_posicion

# Juego principal
def serpientes_y_escaleras():
    posiciones = [1, 1]
    turno = 0
    dado_actual = 1  # El dado ya no se dibuja, pero seguimos manteniendo su valor
    corriendo = True

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dado_actual = random.randint(1, 6)  # Genera un número aleatorio para el dado
                posiciones[turno] = mover_jugador(posiciones[turno], dado_actual)
                print(f"Jugador {turno + 1} tiró {dado_actual} y está en la casilla {posiciones[turno]}")
                turno = (turno + 1) % 2

        pantalla.fill(NEGRO)
        dibujar_tablero()
        dibujar_serpientes_escaleras()

        # Dibujar jugadores
        for i, posicion in enumerate(posiciones):
            x, y = obtener_posicion_tablero(posicion)
            color = VERDE if i == 0 else ROJO
            pygame.draw.circle(pantalla, color, (x, y), 15)

        pygame.display.flip()

        # Verificar si alguien ganó
        for i, posicion in enumerate(posiciones):
            if posicion == 100:
                print(f"¡Jugador {i + 1} ha ganado!")
                corriendo = False
                break

    pygame.quit()

if __name__ == "__main__":
    serpientes_y_escaleras()
