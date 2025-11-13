for i in range(5):
    vidas = int(input("Ingrese la cantidad de vidas:"))
    if vidas >= 5:
        print("El nivel es FÁCIL")
    elif vidas >= 3:
        print("El nivel es MEDIO")
    else:
        print("El nivel es DIFÍCIL")