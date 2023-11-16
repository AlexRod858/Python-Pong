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
    def dibujar(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radio)

    def movimiento(self, screen):
        # Actualizar la posición de la bola en función de su velocidad
        self.x += self.vel_x
        self.y += self.vel_y

        # Revertir la dirección si la bola alcanza los límites de la pantalla
        if self.x - self.radio >= screen.get_width()  or self.x + self.radio <= 0:
            # self.velocidad = (-self.velocidad[0], self.velocidad[1])
            self.x = 400
            self.y = 300

        if self.y + self.radio >= screen.get_height() or self.y - self.radio <= 0:
            self.vel_y = - self.vel_y

    def ajustar_direccion(self):

        self.vel_x = -self.vel_x  # Invierte la dirección horizontal
