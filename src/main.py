import pygame
from setting import *


pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")


SCREEN.fill(YELLOW)

contador = 0
is_running = True

while is_running:
    print(contador)
    contador += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.flip()


pygame.quit()
