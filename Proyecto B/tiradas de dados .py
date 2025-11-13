import random

def tirar_dados(tiradas):
    total = 0
    for i in range(tiradas):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        total += suma
        print("el numero del primer dado es...", dado1, ",el numero del segundo dado es...", dado2, ",y el total es", suma)
    return total

tiradas = int(input("¿cuantas tiradas quiere realizar el jugador 1? "))
total_j1 = tirar_dados(tiradas)
print("total final del jugador 1 es:", total_j1)

segundat = int(input("¿cuantas tiradas quiere realizar el jugador 2? "))
total_j2 = tirar_dados(segundat)
print("total final del jugador 2 es:", total_j2)