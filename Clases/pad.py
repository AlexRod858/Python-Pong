# bola.py
import pygame
import sys

class Pad:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def dibujar(self, screen):
        pygame.draw.rect(screen, 'red', pygame.Rect(self.x, self.y, self.w, self.h))

    def movimiento(self, screen, tecla_arriba, tecla_abajo):
        keys = pygame.key.get_pressed()

            # Verificar teclas presionadas y mover el Pad en consecuencia

        if keys[tecla_arriba]:
            self.y -= 0.5
        elif keys[tecla_abajo]:
            self.y += 0.5

            # Restringir el movimiento para que el Pad no salga de la pantalla
        if self.y < 0:
            self.y = 0
        elif self.y + self.h > screen.get_height():
            self.y = screen.get_height() - self.h



    def golpeo_pad1(self, bola):
        if self.y < bola.y < self.y + self.h and bola.x - bola.radio <= self.x:
            # Calcula la posición relativa al centro del Pad y ajusta la dirección de la bola
            offset = bola.y - (self.y + self.h / 2)
            bola.ajustar_direccion(offset)

    def golpeo_pad2(self, bola):
        if self.y < bola.y < self.y + self.h and bola.x + bola.radio >= self.x:
            # Calcula la posición relativa al centro del Pad y ajusta la dirección de la bola
            offset = bola.y - (self.y + self.h / 2)
            bola.ajustar_direccion(offset)