
import random
def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    memoria=[]
    while len(memoria)<=5:
        agregar = random.randint(0, 9)
        memoria.append(agregar)
    print("memoriza estos números",memoria)

    respuesta=input('escribe los números que memorizaste sin coma, ejemplo: 12345  ')
    '''respuesta=int(respuesta)'''
    respuesta1=list(respuesta)
    respuesta1 = [int(elemento) for elemento in respuesta1]

    if memoria==respuesta1:
        print("GANASTE")
    else:
        respuestan=input('Intenta de nuevo escribe los números que memorizaste sin coma, ejemplo: 12345  ')
        '''respuesta=int(respuesta)'''
        respuesta2=list(respuestan)
        respuesta2 = [int(elemento) for elemento in respuesta2]
        if memoria==respuesta2:
            print("GANASTE")
        else:
            print("Perdiste")