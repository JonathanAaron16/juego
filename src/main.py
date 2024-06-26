from random import randint, randrange
import pygame
from setting import *
from aleatorio import get_random_color,random_color
from colision import *
from bloque import *



cantidad_moneda = 25

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Juego")

clock = pygame.time.Clock()
    
#creo el player
block = create_player()
#creo lista monedas
coins = []
#cargo la lista con 10 monedas
load_coin_list(coins,cantidad_moneda)

#configuro fuente de texto
font = pygame.font.SysFont('Arial', 30)

text = font.render(f"Score: {len(coins)}", True, RED)

is_running = True

while is_running:
    clock.tick(FPS)


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
        # block["radio"] = randint(-1,20)
    
        #actualizamos movimiento
  
        
    if block["dir"] == DR:
        block["rect"].x += SPEED
        block["rect"].y += SPEED
    elif block["dir"] == DL:
        block["rect"].x -= SPEED
        block["rect"].y += SPEED       
    elif block["dir"] == UL:
        block["rect"].x -= SPEED
        block["rect"].y -= SPEED 
    elif block["dir"] == UR:
        block["rect"].x += SPEED
        block["rect"].y -= SPEED 

    for coin in coins[:]:   
        if detectar_colision(coin["rect"],block["rect"]):
            coins.remove(coin)

    #dibujamos pantalla
    SCREEN.fill(CUSTOM) 
    
    pygame.draw.rect(SCREEN,block["color"],block["rect"],block["borde"],block["radio"])

    for coin in coins:
        pygame.draw.rect(SCREEN,coin["color"],coin["rect"],coin["borde"],coin["radio"])

    SCREEN.blit(text, (0,0))


    ##actualizamos elemetos
    pygame.display.flip()


pygame.quit()
