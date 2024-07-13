import pygame
import sys
from pygame.locals import *

pygame.init()


width, height = 500, 500
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption('Relleno de Polígonos: Poligono #2')

poligono_2 = [(321, 335), (288, 286), (339, 251), (374, 302)]

def poligono(puntos):
    pygame.draw.polygon(PANTALLA, (0, 0, 255), puntos)
    pygame.draw.polygon(PANTALLA, (0, 0, 0), puntos, 1)


while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        PANTALLA.fill((255, 255, 255))
        poligono(poligono_2)
        pygame.display.flip()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()
        sys.exit()