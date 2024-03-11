n:float
c:float
d:float
n = input("Digite un primer numero real: ")
c = input("Digite un segundo numero real: ")
d = input("Digite un tercer numero real: ")
if n>c and n>d:
    print("El numero " + str(n) + " es el numero mayor")
elif c>n and c>d:
        print("El numero " + str(c) + " es el numero mayor")
elif d>n and d>c:
            print("El numero " + str(d) + " es el numero mayor")
