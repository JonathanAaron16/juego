import pygame
from random import randrange,randint
from setting import *
from aleatorio import *

def create_block(imagen = None,left = 0,top= 0,width= 50, height=50, color = (255,255,255 ),dire = 3,borde = 0,radio = -1):
    return {"rect": pygame.Rect(left,top,width, height),"color": color,"dir": dire, "borde": borde, "radio": radio, "img": imagen}

def create_player(imagen= None):
    if imagen:
        imagen = pygame.transform.scale(imagen,(player_w,player_h))
    return create_block(imagen,randint(0,WIDTH -player_w),randint(0,WIDTH -
                                            player_w),player_w,player_h,random_color(), 
                                            direcciones[randrange(len(direcciones))],radio = player_h // 2)


def create_coin(imagen =None, visible = True):

    width_coin = 20
    height_coin = 20
    if visible:
        y = randint(0,HEIGHT -height_coin)
    else:
        y = 0 - randint(0,HEIGHT -height_coin)

    if imagen:
        imagen = pygame.transform.scale(imagen,(width_coin,height_coin))
    a = create_block(imagen,randint(0,WIDTH -width_coin), y ,width_coin,height_coin,YELLOW,0,0,height_coin // 2)
    a["speed"] = randint(min_speed_asteroid,max_speed_asteroid)
    
    return a

def create_laser(midbottom = (0,0),color =RED):
    rect = pygame.Rect(0,0,laser_width,laser_heigth)
    rect.midbottom= midbottom
    return {"rect": rect, "color": color,"speed" : laser_speed} 


def load_coin_list(lista:list,cant:int,imagen=None):
    for _ in range(cant):
        lista.append(create_coin(imagen,False))