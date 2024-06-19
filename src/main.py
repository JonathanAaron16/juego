from random import randint
import pygame
from setting import *
from aleatorio import get_random_color,random_color

#direciones
DR = 3
UR = 9
DL = 1
UL = 7   

block_width = 100
block_height = 100
pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

clock = pygame.time.Clock()

#comienzo random
blocks = [{"rect": pygame.Rect(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height),"color": RED,"dir": DR, "borde": 0, "radio": -1},
          {"rect": pygame.Rect(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height),"color": GREEN,"dir": UL, "borde": 0 , "radio": -1},
          {"rect": pygame.Rect(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height),"color": BLUE,"dir": DL , "borde": 0, "radio": -1}]



speed = 5

flag = False
flag_x = False

contador = 0
is_running = True

while is_running:
    clock.tick(FPS)
    # print(contador)
    contador += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    #actualizamos elemetos
    for block in blocks:
    #actualizamos direcion
        if block["rect"].right >= WIDTH:
            if block["dir"] == DR:
                block["dir"] = DL
            else:
                block["dir"] = UL
            block["color"] = get_random_color(colores)

        elif block["rect"].left <= 0:
            if block["dir"] == DL:
                block["dir"] = DR
            else:
                block["dir"] = UR
            block["color"] = random_color()
            
        elif block["rect"].bottom >= HEIGHT:
            if block["dir"] == DR:
                block["dir"] = UR
            else:
                block["dir"] = UL
            block["borde"] = randint(0,10)
        elif block["rect"].top <= 0:
            if block["dir"] == UR:
                block["dir"] = DR
            else:
                block["dir"] = DL
            block["radio"] = randint(-1,20)
        
        #actualizamos movimiento
        
        if block["dir"] == DR:
            block["rect"].x += speed
            block["rect"].y += speed
        elif block["dir"] == DL:
            block["rect"].x -= speed
            block["rect"].y += speed       
        elif block["dir"] == UL:
            block["rect"].x -= speed
            block["rect"].y -= speed 
        elif block["dir"] == UR:
            block["rect"].x += speed
            block["rect"].y -= speed 
        


    #dibujamos pantalla
    SCREEN.fill(CUSTOM) 
    for block in blocks:
        pygame.draw.rect(SCREEN,block["color"],block["rect"],block["borde"],block["radio"])



    ##actualizamos elemetos
    pygame.display.flip()


pygame.quit()
