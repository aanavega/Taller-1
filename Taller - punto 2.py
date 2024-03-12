primer_numero:float
segundo_numero:float
tercer_numero:float
primer_numero = input("Digite un primer numero real: ")
segundo_numero = input("Digite un segundo numero real: ")
tercer_numero = input("Digite un tercer numero real: ")
if primer_numero > segundo_numero and primer_numero > tercer_numero:
    print("El numero " + str(primer_numero) + " es el numero mayor")
elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
        print("El numero " + str(segundo_numero) + " es el numero mayor")
elif tercer_numero > primer_numero and tercer_numero > segundo_numero:
          print("El numero " + str(tercer_numero) + " es el numero mayor")
