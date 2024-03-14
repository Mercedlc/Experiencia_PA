import random
def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    suma=[]
    while sum(suma)<30:
        lanzar = input("aprete Enter para lanzar el dado")
        lanzado = random.randint(1, 6)
        suma.append(lanzado)
        print("sacaste un:",lanzado)
        print("la suma de los que llevas lanzado es:",sum(suma))
        if sum(suma)>=30:
            print ("GANASTE")