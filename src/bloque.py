import pygame
from random import randrange,randint
from setting import *
from aleatorio import *

def create_block(left = 0,top= 0,width= 50, height=50, color = (255,255,255 ),dire = 3,borde = 0,radio = -1):
    return {"rect": pygame.Rect(left,top,width, height),"color": color,"dir": dire, "borde": borde, "radio": radio}

def create_player():
    block_width = 50
    block_height = 50
    return create_block(randint(0,WIDTH -block_width),randint(0,WIDTH -block_width),block_width,block_height,random_color(), direcciones[randrange(len(direcciones))],radio = block_height // 2)


def create_coin():
    width_coin = 20
    height_coin = 20
    return create_block(randint(0,WIDTH -width_coin),randint(0,HEIGHT -height_coin),width_coin,height_coin,YELLOW,0,0,height_coin // 2)


def load_coin_list(lista:list,cant:int):
    for _ in range(cant):
        lista.append(create_coin())