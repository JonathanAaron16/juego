from random import randint


#funcion que reciba lista y retorne un elemento de la misma manera alatoria 

def get_random_element(lista:list):
    indice = randint(0, len(lista )- 1)
    return lista[indice]


def get_random_color(colors:list):
    return get_random_element(colors)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r,g,b