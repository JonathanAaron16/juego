import pygame
from setting import *

#direciones
DR = 3
UR = 9
DL = 1
UL = 7   



pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

clock = pygame.time.Clock()

# rect_1 = pygame.Rect(300,250,200,100)
bloque = pygame.Rect(300,250,200,100) #centrado rect
bloque_dir = DR
bloque_color = RED



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

    #actualizamos direcion
    if bloque.right >= WIDTH:
        if bloque_dir == DR:
            bloque_dir = DL
        else:
            bloque_dir = UL
    elif bloque.left <= 0:
        if bloque_dir == DL:
            bloque_dir = DR
        else:
            bloque_dir = UR
    elif bloque.bottom >= HEIGHT:
        if bloque_dir == DR:
            bloque_dir = UR
        else:
            bloque_dir = UL
    elif bloque.top <= 0:
        if bloque_dir == UR:
            bloque_dir = DR
        else:
            bloque_dir = DL
    

    #actualizamos movimiento
    
    if bloque_dir == DR:
        bloque.x += speed
        bloque.y += speed
    elif bloque_dir == DL:
        bloque.x -= speed
        bloque.y += speed       
    elif bloque_dir == UL:
        bloque.x -= speed
        bloque.y -= speed 
    elif bloque_dir == UR:
        bloque.x += speed
        bloque.y -= speed 
        


    # if rect_1.top <= HEIGHT:

    #     rect_1.y  += speed
    # else:
    #     rect_1.bottom = 0

    # if rect_1.top >= 0:
    #     rect_1.y -= speed
    #--------------------------------------
    # if flag:
    #     if rect_1.bottom <= HEIGHT:
    #         rect_1.y  += speed
    #     else:
    #         flag = False
    # else:
    #     if rect_1.top >= 0:
    #         rect_1.y -= speed
    #     else:
    #         flag = True
    # if flag_x:
    #     if rect_1.right <= WIDTH:
    #         rect_1.x  += speed
    #     else:
    #         flag_x = False
    # else:
    #     if rect_1.left >= 0:
    #         rect_1.x -= speed
    #     else:
    #         flag_x = True


    #dibujamos pantalla
    SCREEN.fill(CUSTOM) 
    pygame.draw.rect(SCREEN,bloque_color,bloque)



    

    ##actualizamos elemetos
    pygame.display.flip()


pygame.quit()

    # rect_2 =pygame.draw.ellipse(SCREEN,RED,(0, 0, 200, 100))
    # pygame.draw.rect(SCREEN,BLUE,rect_2,3)
    # # rect_3 =pygame.draw.rect(SCREEN,BLUE,rect_1)

    # pygame.draw.line(SCREEN,BLUE,(0,0),(WIDTH,HEIGHT))
    
    # rect_4 = pygame.draw.line(SCREEN,GREEN,rect_1.center,rect_2.center,3)
    
    # pygame.draw.rect(SCREEN,BLACK,rect_4,3)
    
    # rect_5= pygame.draw.polygon(SCREEN,WHITE,[(50,50),(500,100),(200,500)],3)
    # pygame.draw.rect(SCREEN,WHITE,rect_5,3)

    
    # pygame.draw.circle(SCREEN,GREEN,SCREEN_CENTER,75,3)