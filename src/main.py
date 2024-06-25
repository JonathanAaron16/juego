from random import randint, randrange
import pygame
from setting import *
from aleatorio import get_random_color,random_color

#direciones
DR = 3
UR = 9
DL = 1
UL = 7   

direcciones = (DR,UR,DL,UL)

block_width = 100
block_height = 100
count_coins = 25

width_coin = 20
height_coin = 20

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

clock = pygame.time.Clock()

def dectetar_colision(rect1,rect2):
    if punto_en_rect(rect1.topleft,rect2) or\
        punto_en_rect(rect1.topright,rect2) or\
        punto_en_rect(rect1.bottomleft,rect2) or\
        punto_en_rect(rect1.bottomright,rect2) or\
        punto_en_rect(rect2.topleft,rect1) or\
        punto_en_rect(rect2.topright,rect1) or\
        punto_en_rect(rect2.bottomleft,rect1) or\
        punto_en_rect(rect2.bottomright,rect1):
        return True
    else:
        return False

def punto_en_rect(punto,rect):
    x , y = punto
    if x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom:
        return True
    else:
        return False
        

def create_block(left = 0,top= 0,width= 50, height=50, color = (255,255,255 ),dire = 3,borde = 0,radio = -1):
    return {"rect": pygame.Rect(left,top,width, height),"color": color,"dir": dire, "borde": borde, "radio": radio}
          


block = create_block(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height,random_color(), direcciones[randrange(len(direcciones))])

coins = []
for i in range(count_coins):
    coins.append(create_block(randint(0,WIDTH -width_coin),randint(0,HEIGHT -height_coin),width_coin,height_coin,YELLOW,0,0,height_coin // 2))

#comienzo random
# blocks = [{"rect": pygame.Rect(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height),"color": GREEN,"dir": UL, "borde": 0 , "radio": -1},
#           {"rect": pygame.Rect(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height),"color": BLUE,"dir": DL , "borde": 0, "radio": -1}]



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

    for coin in coins[:]:   
        if dectetar_colision(coin["rect"],block["rect"]):
            coins.remove(coin)

    #dibujamos pantalla
    SCREEN.fill(CUSTOM) 
    
    pygame.draw.rect(SCREEN,block["color"],block["rect"],block["borde"],block["radio"])

    for coin in coins:
        pygame.draw.rect(SCREEN,coin["color"],coin["rect"],coin["borde"],coin["radio"])




    ##actualizamos elemetos
    pygame.display.flip()


pygame.quit()
