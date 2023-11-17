import pygame
import sys
from Clases.bola import Bola
from Clases.pad import Pad
from Campo import Campo
# ------------------------------
# ------------------------------
# ------------------------------
# Inicializar Pygame
pygame.init()
# ------------------------------
# Configuración de la pantalla
screen_width, screen_height = 960, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game por AlexRod")

# ------------------------------
# ------------------------------
# ----C R E O  O B J E T O S----
# ------------------------------
bola = Bola(400, 300, 40, "black", vel_x = 0.2, vel_y= 0.2)
pad1 = Pad(20, 50, 20, 120)
pad2 = Pad(920, 50, 20, 120)

# ------------------------------
# ------------------------------
# -J U E G O  P R I N C I P A L-
# ------------------------------
font = pygame.font.Font(None, 48)  

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la posición y manejar la puntuación de la bola
    bola.movimiento(screen)
    # screen.fill('green')  # ACTUALIZA FONDO
    Campo(screen).dibujar_campo()
    # Resto del código para dibujar y gestionar la lógica del juego
    bola.dibujar(screen)
    pad1.dibujar(screen)
    pad2.dibujar(screen)
    pad1.movimiento(screen, pygame.K_w, pygame.K_s)
    pad2.movimiento(screen, pygame.K_UP, pygame.K_DOWN)
    pad1.golpeo_pad1(bola)
    pad2.golpeo_pad2(bola)
    # Asignar las variables locales después de la actualización de la bola
    puntuacion_pad1 = bola.puntuacion_pad1
    puntuacion_pad2 = bola.puntuacion_pad2


    # campo.campo()
    puntuacion_texto = font.render(f'{puntuacion_pad1} - {puntuacion_pad2}', True, 'purple')
    screen.blit(puntuacion_texto, (screen.get_width() // 2 - puntuacion_texto.get_width() // 2, 16))

    # Actualizar la pantalla
    pygame.display.flip()

# ------------------------------
# ------------------------------
# ------------------------------

# Salir de Pygame
pygame.quit()
sys.exit()