import pygame 

class Campo:
    def __init__(self, screen):
        self.screen = screen

    def dibujar_campo(self):
        self.screen.fill('green')
        # BORDE
        pygame.draw.rect(self.screen,'white', (10, 10,self.screen.get_width()-20,self.screen.get_height() -20), width= 4)
        # MITAD
        pygame.draw.line(self.screen, 'white', (self.screen.get_width() // 2, 10), (self.screen.get_width() // 2, self.screen.get_height()-14), 4)
        # CENTRO
        pygame.draw.circle(self.screen, 'white', (self.screen.get_width() // 2, self.screen.get_height() // 2), 50, width=4)
        # AREA IZQ GRANDE
        pygame.draw.rect(self.screen,'white', (10,self.screen.get_height() // 4,120,self.screen.get_height() // 2), width= 4)
        # AREA DER GRANDE
        pygame.draw.rect(self.screen,'white', (self.screen.get_width()- 130, self.screen.get_height() // 4,120,self.screen.get_height() // 2), width= 4)
        # AREA IZQ PEQ
        pygame.draw.rect(self.screen,'white', (10,self.screen.get_height() // 3,40,self.screen.get_height() // 3), width= 4)
        # AREA DER PEQ
        pygame.draw.rect(self.screen,'white', (self.screen.get_width()- 50, self.screen.get_height() // 3,40,self.screen.get_height() // 3), width= 4)
