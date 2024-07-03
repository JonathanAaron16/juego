import pygame
from random import *
from setting import *
from aleatorio import *
from colision import *
from bloque import *
from pygame.locals import *
from sys import exit

def terminar():
    pygame-quit()
    exit()    

def mostrar_texto(superficie, texto, fuente, coordenada, color = BLACK , color_fondo = None ) :
    sticker = fuente.render(texto, True, color, color_fondo)
    rect = sticker.get_rect()
    rect.center = coordenada
    superficie.blit(sticker, rect)
    pygame.display.flip()
    

def wait_user(tecla) :
    continuar = True
    while continuar :
        for evento in pygame.event.get() :
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False

def wait_user_click(rect_imagen:pygame.Rect) :
    continuar = True
    while continuar :
        for evento in pygame.event.get() :
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.MOUSEBUTTONDOWN :
                if evento.button == 1: 
                    if punto_en_rect(evento.pos,rect_imagen):
                        continuar = False






cantidad_moneda = 25

# inicializar los modulos de pygame
pygame.init()

NEWCOINEVENT = USEREVENT + 1
GAMETIMEOUT = USEREVENT + 2


clock = pygame.time.Clock()



# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")
pygame.display.set_icon(pygame.image.load(r"src\assets\nave-espacial.png"))
# cargo imagenes
imagen_ovni = pygame.image.load("./src/assets/ovni.png")
imagen_asteroide = pygame.image.load("./src/assets/asteroide.png")
imagen_asteroide_2 = pygame.image.load("./src/assets/asteroide2.png")
imagen_fondo = pygame.transform.scale(pygame.image.load("./src/assets/fondo.jpg"), SCREEN_SIZE)

star_bottom = pygame.transform.scale(pygame.image.load("./src/assets/start_button.png"), STAR_BOTTOM)
fondo_star = pygame.transform.scale(pygame.image.load("./src/assets/fondostart.png"), SCREEN_SIZE)
rect_start_button = star_bottom.get_rect(center = SCREEN_CENTER)
# rect_start_button.center = SCREEN_CENTER
# cargo sonidos
collision_sound = pygame.mixer.Sound("./src/assets/coin.mp3")
congrats_sound = pygame.mixer.Sound("./src/assets/exito.mp3")
game_over_sound = pygame.mixer.Sound("./src/assets/game_over.mp3")
# laser_sound = pygame.mixer.Sound("./src/assets/laser1.wav")

# cargo musica
pygame.mixer.music.load("./src/assets/musica_fondo.mp3")
pygame.mixer.music.set_volume(0.1)


cont_colision = 0

# configuro fuente para el texto
fuente2 = pygame.font.SysFont(None, 48)
fuente3 = pygame.font.SysFont("Segoe Script", 48)
fuente = pygame.font.Font(r"src\assets\dash-horizon.otf", 48)




# screen.fill(BLACK)
# mostrar_texto(screen, "Asteroides", fuente, POS_MAIN_TITLE, WHITE)
# screen.blit(star_bottom,rect_start_button)
# pygame.display.flip()
# wait_user_click(rect_start_button)

high_score = 0

while True:

    pygame.time.set_timer(NEWCOINEVENT, 5000)
    # configuro flags direccion

    move_left = False
    move_right = False
    move_up = False
    move_down = False
    flag_mute = False
    flag_pausa = False

    # creo el player
    block = create_player(imagen_ovni)
    # creo lista monedas
    coins = []
    # cargo la lista con 10 monedas
    load_coin_list(coins, cantidad_moneda, imagen_asteroide_2)

    score = 0
    pygame.mouse.set_visible(1)
    # texto = fuente.render(f"Score: {score}", True, BLUE)
    # print(f"Score: {score}")
    screen.blit(fondo_star,(0,0))
    mostrar_texto(screen, "Asteroides", fuente, POS_MAIN_TITLE, BLACK)
    wait_user_click(pygame.Rect(250,280,310,100))

    # pygame.mixer.music.play() 
    playing_music = True


    lives = 3
    laser = None


    pygame.mouse.set_visible(0)

    pygame.time.set_timer(GAMETIMEOUT, TIME_GAME,1)
    is_running = True
    while is_running:


        clock.tick(FPS)
        # ----> detectar los eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            # eventos presion tecla
            if evento.type == pygame.KEYDOWN:
                if evento.key == K_f:
                    if not laser:
                        laser = create_laser(block["rect"].midbottom)
                if evento.key == pygame.K_LEFT :
                    move_left = True
                    move_right = False
                if evento.key == pygame.K_RIGHT :               
                    move_right = True
                    move_left = False
                if evento.key == pygame.K_UP :               
                    move_up = True
                    move_down = False
                if evento.key == pygame.K_DOWN :               
                    move_down = True
                    move_up = False
                if evento.key == K_m :
                    if playing_music:
                        pygame.mixer.music.pause()
                        flag_mute = True
                    else :
                        pygame.mixer.music.unpause()
                        flag_mute = False 
                    playing_music = not playing_music # o False
                if evento.key == K_p:
                    pygame.mixer.music.pause()
                    mostrar_texto(screen,"Pause",fuente,SCREEN_CENTER,YELLOW)
                    wait_user(K_p)
                    if playing_music:
                        pygame.mixer.music.unpause()
                


                print(move_left, move_right, move_up, move_down)            
                
            # evento liberacion tecla
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT :
                    move_left = False
                if evento.key == pygame.K_RIGHT :               
                    move_right = False
                if evento.key == pygame.K_UP :               
                    move_up = False
                if evento.key == pygame.K_DOWN :               
                    move_down = False
  

            if evento.type == MOUSEBUTTONDOWN :
                if evento.button == 1 :
                    new_coin = create_coin()
                    new_coin["color"] = CUSTOM
                    new_coin["rect"].center = evento.pos
                    coins.append(new_coin)

            if evento.type == NEWCOINEVENT :
                new_coin = create_coin()
                new_coin["color"] = RED
                coins.append(new_coin)
            
            if evento.type == MOUSEMOTION:
                block["rect"].center = evento.pos
            
            if evento.type == GAMETIMEOUT:
                is_running = False
        # ----> actualizar los elementos

    # verifico si el bloque choca contra los limites de la pantalla
    # actualizo su direccion


    # muevo el bloque de acuerdo a su direccion

        if move_left and block["rect"].left > 0 :
            block["rect"].left -= SPEED
            if block["rect"].left < 0 :
                block["rect"].left = 0
        if move_right and block["rect"].right < WIDTH :
            block["rect"].right += SPEED
            if block["rect"].right > WIDTH :
                block["rect"].right = WIDTH
        if move_up and block["rect"].top > 0 :
            block["rect"].top -= SPEED
            if block["rect"].top < 0 :
                block["rect"].top = 0
        if move_down and block["rect"].bottom < HEIGHT:
            block["rect"].top += SPEED
            if block["rect"].top > HEIGHT :
                block["rect"].top = 0

        pygame.mouse.set_pos(block["rect"].center)

        
        for coin in coins:
            coin["rect"].move_ip(0,coin["speed"])
            if coin["rect"].top > HEIGHT:
                coin["rect"].bottom = 0

            if laser:
                laser["rect"].move_ip(0,-laser["speed"])
                if laser["rect"].top < HEIGHT :
                    laser = None


        for coin in coins[:] :
            if detectar_colision_circulo(block["rect"], coin["rect"]):
                coins.remove(coin)
                collision_sound.play()
                lives -= 1
                if len(coins) == 0 :
                    load_coin_list(coins, cantidad_moneda, imagen_asteroide)
                    congrats_sound.play()

                if lives == 0:
                    is_running = False

        for coin in coins[:] :
            if laser:
                if detectar_colision_circulo(laser["rect"], coin["rect"]):
                    coins.remove(coin)
                    laser = None
                    collision_sound.play()
                    score += 1
                    if len(coins) == 0 :
                        load_coin_list(coins, cantidad_moneda, imagen_asteroide)
                        congrats_sound.play()

                

        # dibujar pantalla

        screen.blit(imagen_fondo, (0,0))


        screen.blit(block["img"], block["rect"])

        
        for coin in coins :
            if coin["img"] : 
                screen.blit(coin["img"], coin["rect"])
            else :
                pygame.draw.rect(screen, coin["color"], coin["rect"], border_radius = coin["radio"])

        # screen.blit(texto, (350, 20))

        if laser:
            pygame.draw.rect(screen,laser["color"], laser["rect"]) 

        mostrar_texto(screen,f"lives: {lives} ",fuente,POS_LAST_SCORE,RED)
        mostrar_texto(screen,f"Score: {score} ",fuente,POS_SCORE,BLUE)

        if flag_mute :
            mostrar_texto(screen, "Mute", fuente, (50, HEIGHT - 50), GREEN)
        # actualizo la pantalla

        
        pygame.display.flip() 

    if score > high_score:
        high_score = score
    pygame.mixer.music.stop()
    game_over_sound.play()
    screen.fill(BLACK)
    mostrar_texto(screen,f"last Score: {score}",fuente,POS_LAST_SCORE,BLUE)
    mostrar_texto(screen,f"high Score: {high_score}",fuente,POS_HIGH_SCORE,BLUE)
    mostrar_texto(screen, "GAME OVER", fuente, SCREEN_CENTER, WHITE)
    mostrar_texto(screen, "Presione SPACE para continuar", fuente, (WIDTH // 2, HEIGHT - 50), WHITE)
    pygame.display.flip()
    wait_user(K_SPACE)


pygame.quit()