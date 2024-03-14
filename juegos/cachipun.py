import random
def cachipun():
    persona= input("Elije entre piedra, papel, o tijera")
    computador=random.randint(1,3)
    if computador == 1:
        print("piedra")
        if persona == "piedra":
            print("Empate")
        if persona =="papel":
            print("Ganaste!")
        if persona == "tijeras":
            print("Perdiste")
    if computador == 2:
        print("papel")
        if persona == "piedra":
            print("Perdiste")
        if persona =="papel":
            print("Empate")
        if persona == "tijeras":
            print("Ganaste!")
    if computador == 3:
        print("tijera")
        if persona == "piedra":
            print("Ganaste!")
        if persona =="papel":
            print("Perdiste")
        if persona == "tijeras":
            print("Empate")
    pass
