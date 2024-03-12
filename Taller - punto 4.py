primer_numero: float 
primer_numero = float(input("Ingrese un numero real: "))
segundo_numero: float 
segundo_numero = float(input("Ingrese otro numero real: "))
if (primer_numero%segundo_numero) == 0:
    print("El numero " + str(primer_numero)+ " es multiplo de " + str(segundo_numero))
else:
    print("El numero " + str(primer_numero)+ " no es multiplo de " + str(segundo_numero))
