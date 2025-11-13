import  random
tiradas = int(input("¿cuantas tiradas quieres realizar?"))
for i in range(tiradas): 
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    print("el numero del primer dado es...",dado1, ",el numero del segundo dado es..." ,dado2,",y el total es",suma)