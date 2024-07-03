def detectar_colision(rect1,rect2):
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
def distancia_entre_puntos(pto_1:tuple[int,int],pto_2:tuple[int,int]):
    base = pto_1[0] - pto_2[0]
    altura = pto_1[1] - pto_2[1]
    return (base ** 2 + altura ** 2) **0.5
    
def calcular_radio(rect):
    return rect.width // 2

def detectar_colision_circulo(rect1,rect2):
    r1 = calcular_radio(rect1)
    r2 = calcular_radio(rect2)
    distancia = distancia_entre_puntos(rect1.center,rect2.center)
    return distancia <= r1 + r2
        