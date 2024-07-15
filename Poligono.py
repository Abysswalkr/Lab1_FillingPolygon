import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 800, 600
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption('Relleno de Polígonos')

poligono_1 = [(165, 380), (185, 360), (180, 330), (207, 345),
              (233, 330), (230, 360), (250, 380), (220, 385),
              (205, 410), (193, 383)]

poligono_2 = [(321, 335), (288, 286), (339, 251), (374, 302)]

poligono_3 = [(377, 249), (411, 197), (436, 249)]

poligono_4 = [(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
              (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
              (597, 215), (552, 214), (517, 144), (466, 180)]

poligono_5 = [(682, 175), (708, 120), (735, 148), (739, 170)]

poligono_1 = [(x, height - y) for x, y in poligono_1]
poligono_2 = [(x, height - y) for x, y in poligono_2]
poligono_3 = [(x, height - y) for x, y in poligono_3]
poligono_4 = [(x, height - y) for x, y in poligono_4]
poligono_5 = [(x, height - y) for x, y in poligono_5]


def rellenar_poligono(puntos, color_relleno, color_contorno, ancho_contorno):
    pygame.draw.polygon(PANTALLA, color_relleno, puntos)
    pygame.draw.polygon(PANTALLA, color_contorno, puntos, ancho_contorno)

while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        PANTALLA.fill((255, 255, 255))
        rellenar_poligono(poligono_1, (0, 0, 255), (0, 0, 0), 1)
        rellenar_poligono(poligono_2, (0, 255, 0), (0, 0, 0), 1)
        rellenar_poligono(poligono_3, (255, 0, 0), (0, 0, 0), 1)
        rellenar_poligono(poligono_4, (0, 0, 255), (0, 0, 0), 1)
        rellenar_poligono(poligono_5, (255, 255, 255), (0, 0, 0),
                                  1)
        pygame.display.flip()
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()
        sys.exit()
