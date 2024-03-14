# Definir dos conjuntos con sus elementos
vocales=["a","e","i","o","u"]
consonantes= ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

# Leer una letra cualquiera
letra = input("ingrese una letra: ")

# Determinar si la letra hace parte del conjunto Vocales
if letra in vocales:
    print("La letra " + str(letra)+ " es una vocal")
elif letra in consonantes:
        print("La letra " + str(letra)+ " es consonante")
