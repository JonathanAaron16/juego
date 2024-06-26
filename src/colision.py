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
    
def detectar_colision_circulo(rect1,rect2):
    r1 = rect1.width // 2
    r2 = rect2.width // 2
    distancia = 0
    if distancia <= r1 + r2:
        return True
    else:
        return False