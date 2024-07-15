import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 800, 600
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption('Relleno de Polígonos: Poligono #4')

poligono_4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
              (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
              (597, 215), (552, 214), (517, 144), (466, 180)]


poligono_4 = [(x, height - y) for x, y in poligono_4]

def dibujar_rellenar_poligono(puntos):
    pygame.draw.polygon(PANTALLA, (0, 0, 255), puntos)
    pygame.draw.polygon(PANTALLA, (0, 0, 0), puntos, 1)

while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        PANTALLA.fill((255, 255, 255))
        dibujar_rellenar_poligono(poligono_4)
        pygame.display.flip()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()
        sys.exit()
