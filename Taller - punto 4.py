n: float 
n = float(input("Ingrese un numero real: "))
z: float 
z = float(input("Ingrese otro numero real: "))
if (n%z) == 0:
    print("El numero " + str(n)+ " es multiplo de " + str(z))
else:
    print("El numero " + str(n)+ " no es multiplo de " + str(z))
