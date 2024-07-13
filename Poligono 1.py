import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 500, 500
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption('Relleno de Polígonos: Poligono #1')

poligono_1 = [(165, 380), (185, 360), (180, 330), (207, 345),
              (233, 330), (230, 360), (250, 380), (220, 385),
              (205, 410), (193, 383)]


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
        poligono(poligono_1)
        pygame.display.flip()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()
        sys.exit()
