import random
def adivinar_par_o_impar(persona):
    numero = random.randint(1, 1000)
    if persona == 'par'and numero % 2 == 0:
        return print("Adivino correctamente")
    elif persona == 'par'and numero % 2 != 0:
        return print("No adivino")
    elif persona == 'impar'and numero % 2 != 0:
        return print("Adivino correctamente")
    elif persona == 'impar'and numero % 2 == 0:
        return print("No adivino")
        
    
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
adivinar_par_o_impar('impar')