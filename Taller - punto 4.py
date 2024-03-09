
n: int 
n = int(input("Ingrese un numero real: "))
z: int 
z = int(input("Ingrese otro numero real: "))
if (n%z) == 0:
    print("El numero " + str(n)+ " es multiplo de " + str(z))
else:
    print("El numero " + str(n)+ " no es multiplo de " + str(z))