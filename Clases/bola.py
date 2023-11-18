# bola.py
import pygame

class Bola:
    def __init__(self, x, y, radio, color, vel_x, vel_y):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.vel_x = vel_x
        self.vel_y = vel_y
        # 
    puntuacion_pad1 = 0
    puntuacion_pad2 = 0
    def dibujar(self, screen):
        pelota = pygame.image.load("imgs/pelota.png")
        pelota = pygame.transform.scale(pelota, (2 * self.radio, 2 * self.radio))
        screen.blit(pelota, (self.x - self.radio, self.y - self.radio))         # pygame.draw.circle(screen, self.color, (self.x, self.y), self.radio)

    
    def ajustar_direccion(self):

        self.vel_x = -self.vel_x  # Invierte la dirección horizontal

    def gestionar_puntuacion(self):
        # Verificar si la bola alcanza los límites de la pantalla y actualizar la puntuación
        if self.x - self.radio >= 800:
            return 'pad1'
        elif self.x + self.radio <= 0:
            return 'pad2'
        return None


    def movimiento(self, screen):
            # Actualizar la posición de la bola en función de su velocidad
            self.x += self.vel_x
            self.y += self.vel_y

            # Revertir la dirección si la bola alcanza los límites de la pantalla
            if self.x - self.radio >= screen.get_width():
                self.x = 400
                self.y = 300
                self.puntuacion_pad1 += 1
                print(self.puntuacion_pad1)
            if self.x + self.radio <= 0:
                self.x = 400
                self.y = 300
                self.puntuacion_pad2 += 1


            if self.y + self.radio >= screen.get_height() or self.y - self.radio <= 0:
                self.vel_y = - self.vel_y
