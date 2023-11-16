import pygame
import sys
from Clases.bola import Bola
from Clases.pad import Pad

# ------------------------------
# ------------------------------
# ------------------------------
# Inicializar Pygame
pygame.init()
# ------------------------------
# Configuración de la pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bola en Pygame")

# ------------------------------
# ------------------------------
# ----C R E O  O B J E T O S----
# ------------------------------
bola = Bola(400, 300, 40, "black", vel_x = 0.2, vel_y= 0.2)
pad1 = Pad(50, 50, 20, 120)
pad2 = Pad(730, 50, 20, 120)

# ------------------------------
# ------------------------------
# -J U E G O  P R I N C I P A L-
# ------------------------------
# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bola.movimiento(screen)
    screen.fill('green')  # ACTUALIZA FONDO
    bola.dibujar(screen)
    pad1.dibujar(screen)
    pad2.dibujar(screen)
    pad1.movimiento(screen, pygame.K_w, pygame.K_s)
    pad2.movimiento(screen, pygame.K_UP, pygame.K_DOWN)
    pad1.golpeo_pad1(bola)
    pad2.golpeo_pad2(bola)


    # Actualizar la pantalla
    pygame.display.flip()

# ------------------------------
# ------------------------------
# ------------------------------

# Salir de Pygame
pygame.quit()
sys.exit()