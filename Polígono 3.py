import pygame
import sys
from pygame.locals import *

pygame.init()


width, height = 500, 500
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption('Relleno de Polígonos: Poligono #3')

poligono_3 = [(377, 249), (411, 197), (436, 249)]

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
        poligono(poligono_3)
        pygame.display.flip()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()
        sys.exit()