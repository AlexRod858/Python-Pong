import pygame 

def campo(screen):

    screen.fill('green')  # ACTUALIZA FONDO
    pygame.draw.line(screen, (255, 255, 255), (screen.get_width() // 2, 0), (screen.get_width() // 2, screen.get_height()), 2)


    # pygame.draw.ellipse(screen, (0, 0, 255), (screen.get_width() // 2, screen.get_height() // 2), (200, 200), width=10)
    pygame.draw.ellipse(screen, (0, 0, 255), (screen.get_width() // 2, screen.get_height() // 2, 200, 200), width=10)
