import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 500, 500
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption('Relleno de Polígonos. Polígono #1')


while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    except Exception as e:
        print(f"Ocurrió un error: {e}")

