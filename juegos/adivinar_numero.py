def adivinar_numero(num):
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    import random
    n = random.randint(1,10)
    #num = int(input())
    if num == n:
        return print('Adivinaste!')
    else:
        return print('sigue intentando')
    
adivinar_numero(9)