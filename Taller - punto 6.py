Vocales=["a","e","i","o","u"]
Consonantes= ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
x = input("ingrese una letra: ")
if x in Vocales:
    print("La letra " + str(x)+ " es una vocal")
elif x in Consonantes:
        print("La letra " + str(x)+ " es consonante")