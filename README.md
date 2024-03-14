# Taller-1

### RootNgine

<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/ZRY4ZZN2/Whats-App-Image-2024-03-13-at-19-10-46.jpg' border='0' alt='Whats-App-Image-2024-03-13-at-19-10-46'/></a>

Realizado por Daniel Santiago Barrera y Ana Sofia Vega; a continuacion el taller #1 con los respectivos codigos, sus explicaciones y diagramas de flujo:

1. Puntos pares: programa individual con extensión .py
2. Puntos impares: programa en notebook de jupiter


## Primer punto:
Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).

[![Whats-App-Image-2024-03-10-at-07-54-15.jpg](https://i.postimg.cc/6TJPWLSq/Whats-App-Image-2024-03-10-at-07-54-15.jpg)](https://postimg.cc/5QggpvfW)


 ## Segundo punto
 Realice un programa que lea tres números reales y determine cuál es el mayor.

 ```Python
    # Leer tres numeros reales
      primer_numero:float
      segundo_numero:float
      tercer_numero:float
      primer_numero = input("Digite un primer numero real: ")
      segundo_numero = input("Digite un segundo numero real: ")
      tercer_numero = input("Digite un tercer numero real: ")

    # Evaluar las desigualdades de magnitud de cada numero
      if primer_numero > segundo_numero and primer_numero > tercer_numero:
          print("El numero " + str(primer_numero) + " es el numero mayor")
      elif segundo_numero > primer_numero and segundo_numero > tercer_numero:
             print("El numero " + str(segundo_numero) + " es el numero mayor")
      elif tercer_numero > primer_numero and tercer_numero > segundo_numero:
                 print("El numero " + str(tercer_numero) + " es el numero mayor")

 ```

 - Explicacion:
   1) Definimos las tres variables, tres numeros reales (del tipo float).
   2) Indicamos los condicionales con desigualdades, con el fin de comparar cada uno de los numeros.
   4) Definimos cual de los tres valores reales es mayor.

 - Diagrama de flujo:
   [![](https://mermaid.ink/svg/pako:eNpVj0FrwzAMhf-K0KmDlkGPga2wJoFcdlh3i3sQsZIYHLk4NmMk-e-zt26w23tPn8TTgp3TjAX21n10I_kA76USeNk1YjrjHrKGw-EZzq3Eib0DuabsnLOybWTwPJOHKHAfeyabiTITVStPRkL2Vfb18saz0dGBZpDT4xF4hi6tnbaE1BlZX906tJX9vZcAM93IX_-Ai1nH_8B9PHwXbXa1kdx7_LFKkgbcY6InMjo9u-REYRh5YoVFkpp7ijYoVLIllGJwl0_psAg-8h7jTVPg0tDgacKiJzvz9gU90Gbl)](http://https://mermaid.ink/svg/pako:eNpVj0FrwzAMhf-K0KmDlkGPga2wJoFcdlh3i3sQsZIYHLk4NmMk-e-zt26w23tPn8TTgp3TjAX21n10I_kA76USeNk1YjrjHrKGw-EZzq3Eib0DuabsnLOybWTwPJOHKHAfeyabiTITVStPRkL2Vfb18saz0dGBZpDT4xF4hi6tnbaE1BlZX906tJX9vZcAM93IX_-Ai1nH_8B9PHwXbXa1kdx7_LFKkgbcY6InMjo9u-REYRh5YoVFkpp7ijYoVLIllGJwl0_psAg-8h7jTVPg0tDgacKiJzvz9gU90Gbl)


 ## Tercer punto
 Realice un programa que lea un número entero y determine si es par o impar.

```Python
# Leer un numero real
numero_real : int
numero_real = int(input("Ingrese un numero real: "))

# Determinar si el residuo del numero entre 2 es 0
if ((numero_real) % 2) == 0 :
    print("El numero " + str(numero_real) + " es par")
else:
    print("El numero " + str(numero_real) + " es impar")
 
 ```

 - Explicacion:
   1) Definimos la variable, en este caso, un numero n entero (del tipo int).
   2) Si el residuo de este numero (n) entre 2 es 0, el numero es par.
   3) Si no es 0, es impar.


 ## Cuarto punto
 Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

```Python
# Leer dos numeros reales
primer_numero: float 
primer_numero = float(input("Ingrese un numero real: "))
segundo_numero: float 
segundo_numero = float(input("Ingrese otro numero real: "))

# Dterminar si el residuo del primer numero entre el segundo es 0
if (primer_numero%segundo_numero) == 0:
    print("El numero " + str(primer_numero)+ " es multiplo de " + str(segundo_numero))
else:
    print("El numero " + str(primer_numero)+ " no es multiplo de " + str(segundo_numero))
```

 - Explicacion:
   1) Definimos las dos variables, dos numeros reales (del tipo float).
   2) Hacemos un condicional, con el fin de definir si el residuo del primer numero entre el segundo numero es 0.
   3) Si es 0, si es multiplo, si no es 0, no es multiplo del segundo numero

  
 ## Quinto punto
 Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

```Python
# Leer tres numeros reales
primer_real: float 
primer_real = float(input("Ingrese un primer numero real: "))
segundo_real: float 
segundo_real = float(input("Ingrese un segundo numero real: "))
tercer_real: float
tercer_real = float(input("Ingrese un tercer numero real: "))

# Determinar si la suma de los dos primeros es mayor, menor o igual que el tercer número
if (primer_real+segundo_real) > tercer_real:
    print("La suma de los dos primeros numeros es mayor que " + str(tercer_real))
elif (primer_real+segundo_real) < tercer_real:
        print("La suma de los dos primeros numeros es menor que " + str(tercer_real))
elif (primer_real+segundo_real) == tercer_real:
      print("La suma de los dos primeros numeros es igual a " + str(tercer_real))
```

 - Explicacion:
   1) Definimos las tres variables, tres numero reales (del tipo float).
   2) Hacemos una serie de condicionales teniendo en cuenta la suma de los dos primeros numeros.
   3) Esto con el fin de ver si el resultado de esta suma es mayor, menor o igual al tercer numero.


 ## Sexto punto
 Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

```Python
# Definir dos conjuntos con sus elementos
Vocales=["a","e","i","o","u"]
Consonantes= ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

# Leer una letra cualquiera
letra = input("ingrese una letra: ")

# Determinar si la letra hace parte del conjunto Vocales
if letra in Vocales:
    print("La letra " + str(letra)+ " es una vocal")
elif x in Consonantes:
        print("La letra " + str(letra)+ " es consonante")
```
 
 - Explicacion:
   1) Definimos dos conjuntos: el conjunto vocales y el conjunto consonantes; y a su vez, definimos los elementos que los componen respectivamente.
   2) Definimos una variable 'letra'.
   3) Evaluamos si la variable 'letra' se encuentra en el conjunto vocales.
   4) Si 'letra' se encuentra en el conjunto vocales, la variable es una vocal.
   5) Si no, no es una vocal.

 - Diagrama de flujo:
  [![](https://mermaid.ink/svg/pako:eNptkN1qwzAMhV9F-GoD9QUC22ANLYWym47dJL3QHKVx68iZY_dnbd999lYGg4EQ4ujTkdBZadewKlRr3UF35AO8lrXA891CjDbuPtcwmTzCtFpy8ATHdZKm31JZLWTjeSQPUQhs7uduijIDs-rNabI8PhAyGnQY86yT0QlJSPo7amywxQ12uMUdWuxRcMAP9DhiwD0e8Ign_MTsO8um8_MRBvaBhTUDWdBOtlGCg9uyp2tC5xm9rMylq5a3y8D8HNsQ8Aj7DK9_yRd3Mf-RIO4PXUtKoFD17HsyTfrcOSu1Ch33XKsilQ23FG2oVS3XhFIMbnUSrYrgI6OKQ0OBS0MbT70qWrIjX78A83GC1g)](http://https://mermaid.ink/svg/pako:eNptkN1qwzAMhV9F-GoD9QUC22ANLYWym47dJL3QHKVx68iZY_dnbd999lYGg4EQ4ujTkdBZadewKlRr3UF35AO8lrXA891CjDbuPtcwmTzCtFpy8ATHdZKm31JZLWTjeSQPUQhs7uduijIDs-rNabI8PhAyGnQY86yT0QlJSPo7amywxQ12uMUdWuxRcMAP9DhiwD0e8Ign_MTsO8um8_MRBvaBhTUDWdBOtlGCg9uyp2tC5xm9rMylq5a3y8D8HNsQ8Aj7DK9_yRd3Mf-RIO4PXUtKoFD17HsyTfrcOSu1Ch33XKsilQ23FG2oVS3XhFIMbnUSrYrgI6OKQ0OBS0MbT70qWrIjX78A83GC1g)


 ## Septimo punto
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
- El promedio
- La mediana
- El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
- Ordenar los números de forma ascendente
- Ordenar los números de forma descendente
- La potencia del mayor número elevado al menor número
- La raíz cúbica del menor número

```Python
# Leer cinco numeros reales
Primer_numero: int
Segundo_numero : int
Tercer_numero : int
Cuarto_numero: int
Quinto_numero : int
Primer_numero= int(input("Ingrese su primer numero real: "))
Segundo_numero= int(input("Ingrese su segundo numero real: "))
Tercer_numero= int(input("Ingrese su Tercer numero real: "))
Cuarto_numero= int(input("Ingrese su Cuarto numero real: "))
Quinto_numero= int(input("Ingrese su Quinto numero real: "))

# Definir variables
mayor_numero:int
menor_numero:int
potencia:int
raiz:int

# Sacar promedio
Promedio= ((Primer_numero+Segundo_numero+Tercer_numero+Cuarto_numero+Quinto_numero)/5)
print("El promedio de los numeros ingresados es: " + str(Promedio))

# Sacar promedio multiplicativo
Promedio_Multiplicativo= ((Primer_numero*Segundo_numero*Tercer_numero*Cuarto_numero*Quinto_numero)**(1/5))
print("El promedio multiplicativo de los numeros ingresados es: " + str(Promedio_Multiplicativo))

# Ordenar de manera ascedente y descendente cumpliendo el caso donde 1 > resto de numeros 'No hubo tiempo :('
if Primer_numero > Segundo_numero and Segundo_numero > Tercer_numero and Tercer_numero > Cuarto_numero and Cuarto_numero > Quinto_numero: #1>2>3>4>5
    print("Los numeros ordenados de forma descendente van: " +str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str( Cuarto_numero)+ ","+ str(Quinto_numero)+ ".")
    print("Los numeros ordenados de forma ascendente van: "+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+".")
elif Primer_numero > Segundo_numero and Segundo_numero > Tercer_numero and  Tercer_numero > Quinto_numero and Quinto_numero > Cuarto_numero:#1>2>3>5>4
    print("Los numeros ordenados de forma descendente van: " +str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ".")
    print("Los numeros ordenados de forma ascendente van: "+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+".") 
elif Primer_numero > Segundo_numero and Segundo_numero > Cuarto_numero and Cuarto_numero > Quinto_numero and Quinto_numero > Tercer_numero:#1>2>4>5>3
    print("Los numeros ordenados de forma ascendente van: " +str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ".")
elif Primer_numero > Segundo_numero and Segundo_numero >  Cuarto_numero and Cuarto_numero > Tercer_numero and Tercer_numero > Quinto_numero:#1>2>4>3>5
    print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ".")
elif Primer_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Tercer_numero and Tercer_numero > Cuarto_numero:#1>2>5>3>4
    print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ".")
elif Primer_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Cuarto_numero and Cuarto_numero > Tercer_numero:#1>2>5>4>5
    print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ".")
elif Primer_numero > Tercer_numero and Tercer_numero > Segundo_numero and Segundo_numero > Cuarto_numero and Cuarto_numero > Quinto_numero:#1>3>2>4>5:
    print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ".") 
elif Primer_numero > Tercer_numero and Tercer_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Cuarto_numero:#1>3>2>5>4
    print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ".")
elif Primer_numero > Tercer_numero and Tercer_numero > Cuarto_numero and Cuarto_numero > Segundo_numero and Segundo_numero > Quinto_numero: #1>3>4>2>5
    print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ".")
elif Primer_numero > Tercer_numero and Tercer_numero > Cuarto_numero and Cuarto_numero >Quinto_numero and Quinto_numero > Segundo_numero: #1>3>4>5>2
    print("Los numeros ordenados de forma ascendente van: " +str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ".")
elif Primer_numero > Tercer_numero  and Tercer_numero > Quinto_numero and Quinto_numero > Cuarto_numero and Cuarto_numero > Segundo_numero: #1>3>5>4>2
    print("Los numeros ordenados de forma ascendente van: " +str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ".")
elif Primer_numero > Tercer_numero and Tercer_numero > Quinto_numero and Quinto_numero > Segundo_numero and Segundo_numero > Cuarto_numero: # 1>3>5>2>4
    print("Los numeros ordenados de forma ascendente van: " +str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ".")
elif Primer_numero > Cuarto_numero and Cuarto_numero > Tercer_numero and Tercer_numero > Segundo_numero and Segundo_numero > Quinto_numero: #1>4>3>2>5
    print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ".")
elif Primer_numero > Cuarto_numero and Cuarto_numero > Tercer_numero and Tercer_numero > Quinto_numero  and Quinto_numero  >  Segundo_numero:
    print("Los numeros ordenados de forma ascendente van: " +str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ".")
elif Primer_numero > Cuarto_numero and Cuarto_numero > Segundo_numero and Segundo_numero > Tercer_numero and Tercer_numero > Quinto_numero:
    print("Los numeros ordenados de forma ascendente van: " +str(Quinto_numero)+ ","+ str(Tercer_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Tercer_numero)+ ","+ str(Quinto_numero)+ ".")
elif Primer_numero > Cuarto_numero and Cuarto_numero > Segundo_numero and Segundo_numero > Quinto_numero and Quinto_numero > Tercer_numero:
    print("Los numeros ordenados de forma ascendente van: " +str(Tercer_numero)+ ","+ str(Quinto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Primer_numero)+ ".")
    print("Los numeros ordenados de forma descendente van: " + str(Primer_numero)+ ","+ str(Cuarto_numero)+ ","+ str(Segundo_numero)+ ","+ str(Quinto_numero)+ ","+ str(Tercer_numero)+ ".")

# Determinar cual de los cinco numeros es el mayor
if Primer_numero>Segundo_numero and Primer_numero>Tercer_numero and Primer_numero>Cuarto_numero and Primer_numero>Quinto_numero:
    mayor_numero= Primer_numero
elif Segundo_numero>Primer_numero and Segundo_numero>Tercer_numero and Segundo_numero>Cuarto_numero and Segundo_numero>Quinto_numero:
    mayor_numero= Segundo_numero
elif Tercer_numero>Primer_numero and Tercer_numero>Segundo_numero and Tercer_numero>Cuarto_numero and Tercer_numero>Quinto_numero:
    mayor_numero= Tercer_numero
elif Cuarto_numero>Primer_numero and Cuarto_numero>Segundo_numero and Cuarto_numero>Cuarto_numero and Cuarto_numero>Quinto_numero:
    mayor_numero= Cuarto_numero
elif Quinto_numero>Primer_numero and Quinto_numero>Segundo_numero and Quinto_numero>Cuarto_numero and Quinto_numero>Quinto_numero:
        mayor_numero= Quinto_numero

# Determinar cual de los cinco numeros es el menor
if Primer_numero<Segundo_numero and Primer_numero<Tercer_numero and Primer_numero<Cuarto_numero and Primer_numero<Quinto_numero:
    menor_numero= Primer_numero
elif Segundo_numero<Primer_numero and Segundo_numero<Tercer_numero and Segundo_numero<Cuarto_numero and Segundo_numero<Quinto_numero:
    menor_numero= Segundo_numero
elif Tercer_numero<Primer_numero and Tercer_numero<Segundo_numero and Tercer_numero<Cuarto_numero and Tercer_numero<Quinto_numero:
    menor_numero= Tercer_numero
elif Cuarto_numero<Primer_numero and Cuarto_numero<Segundo_numero and Cuarto_numero<Tercer_numero and Cuarto_numero<Quinto_numero:
    menor_numero= Cuarto_numero
elif Quinto_numero<Primer_numero and Quinto_numero<Segundo_numero and Quinto_numero<Tercer_numero and Quinto_numero<Cuarto_numero:
    menor_numero= Quinto_numero

# Sacar la potencia del mayor numero elevado al menor numero
potencia = (mayor_numero**(menor_numero))
print(" La potencia del mayor numero elevado a el menor numero es: " + str(potencia))

# Sacar la raiz cubica del menor numero
raiz = (menor_numero**(1/3))                
print(" La raiz cubica del menor numero es: " + str(raiz))
```

   - Explicacion:
     1) Definimos las 5 variables, 5 numeros reales (del tipo float).
     2) Hacemos un condicional para definir el promedio de las variables ingresadas:  la suma de estas entre el numero de datos.
     3) Realizamos otro condicional para definir el promedio multiplicativo: la raiz quinta (numero de datos) del producto de todos los valores.
     4) Realizamos una serie de condicionales, con el fin de organizar los numeros de manera ascendente y descendente.
     5) Definimos una variable (potencia) y le asignamos una operacion (Sacar potencia del mayor número elevado al menor número).
     6) Definimos una ultima variable (raiz) y le asignamos una operacion (La raíz cúbica del menor número).
        
 
 ## Octavo punto
 Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

 ```Python

# Leer un numero real
Frecuencia_hz: float
Frecuencia_hz = float(input("Ingrese una frecuencia de onda en hz: "))

# Determinar a que rango del espectro electromagnético se encuentra el numero 
if Frecuencia_hz > 30.0*(10**18):
    print('Se encuentra en el espectro electromagnetico de "rayos gamma"')
elif 30.0*(10**18)> Frecuencia_hz > 30.0*(10**15):
    print('Se encuentra en el espectro electromagnetico de "Rayos x"')
elif 30.0*(10**15)> Frecuencia_hz > 1.5*(10**15):
    print('Se encuentra en el espectro electromagnetico de "Ultravioleta extremo"')
elif 1.5*(10**15)> Frecuencia_hz > 7.89*(10**14):
    print('Se encuentra en el espectro electromagnetico de "Ultravioleta cercano"')
elif 7.89*(10**14)> Frecuencia_hz > 384*(10**12):
    print('Se encuentra en el espectro electromagnetico de "Espectro visible"')
elif 384*(10**12)> Frecuencia_hz > 120*(10**12):
    print('Se encuentra en el espectro electromagnetico de "Infrarrojo cercano"')
elif 120*(10**12)> Frecuencia_hz > 6.00*(10**12):
    print('Se encuentra en el espectro electromagnetico de "Infrarrojo mediano"')
elif 6.00*(10**12)> Frecuencia_hz > 300*(10**9):
    print('Se encuentra en el espectro electromagnetico de "Infrarrojo lejano/sublumétrico"')
elif 300*(10**9)> Frecuencia_hz > 3*(10**8):
    print('Se encuentra en el espectro electromagnetico de "Microondas"')
elif 3*(10**8)> Frecuencia_hz > 300*(10**6):
    print('Se encuentra en el espectro electromagnetico de "Utra alta Frecuencia-Radio"')
elif 300*(10**6)> Frecuencia_hz > 30*(10**6):
    print('Se encuentra en el espectro electromagnetico de "Muy alta Frecuencia-Radio"')
elif 30*(10**6)> Frecuencia_hz > 1.7*(10**6):
    print('Se encuentra en el espectro electromagnetico de "Onda Corta - Radio"')
elif 1.7*(10**6)> Frecuencia_hz > 650*(10**3):
    print('Se encuentra en el espectro electromagnetico de "Onda Media - Radio"')
elif 650*(10**3)> Frecuencia_hz > 30*(10**3):
    print('Se encuentra en el espectro electromagnetico de "Onda Larga - Radio"')
elif 30*(10**3)> Frecuencia_hz:
    print('Se encuentra en el espectro electromagnetico de "Muy baja frecuencia - radio"')
 ```
 
 - Explicacion:
   1) Definimos una variable (la frecuencia en hz).
   2) Hacemos una serie de condicionales utilizando if y elif, y empleando a su vez desigualdades con el fin de comparar el valor ingresado.
   3) De esta manera, podemos definir en que rango del espectro electromagnético se encuentra el valor ingresado.


## Noveno punto
Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.

```Python
# Determinar un conjunto con sus elementos
paises = ["canada" , "estados unidos", "brasil" , "mexico", "argentina", "ecuador" , "venezuela", "colombia", "republica dominicana", "costa rica", "cuba", "puerto rico", "peru" , "chile" , "panama", "uruguay", "paraguay", "bolivia" , "panama", "guatemala" , "nicaragua"]

# Leer un pais de America en minusculas
nombre_pais = input("Ingrese el nombre de un pais de America en  minusculas: ")

# Determinar si el pais ingresado se encuentra en el conjunto incial e imprimir su capital correspondiente
if nombre_pais in paises:
    if nombre_pais == "mexico":
        print("ciudad de mexico")
    elif nombre_pais == "canada":
        print("ottawa")
    elif nombre_pais == "estados unidos":
        print("washignton")
    elif nombre_pais == "brasil":
        print("brasilia")
    elif nombre_pais == "argentina":
        print("buenos aires")
    elif nombre_pais == "ecuador":
        print("quito")
    elif nombre_pais == "venezuela":
        print("caracas")
    elif nombre_pais ==  "colombia":
        print("bogota")
    elif nombre_pais == "republica dominicana":
        print("santo domingo")
    elif nombre_pais == "costa rica":
        print("san jose")
    elif nombre_pais == "cuba":
        print("la habana")
    elif nombre_pais == "peru":
        print("lima")
    elif nombre_pais == "paraguay":
        print("asuncion")
    elif nombre_pais == "chile":
        print("santiago")
    elif nombre_pais == "uruguay":
        print("montevideo")
    elif nombre_pais == "bolivia":
        print("la paz")
    elif nombre_pais == "panama":
        print("panama")
    elif nombre_pais == "guatemala":
        print("guatemala")
    elif nombre_pais == "nicaragua":
        print("managua")
    elif nombre_pais == "el salvador":
        print("el salvador")

else:
    print("El pais no pertenece a America")
 ```

- Explicacion:
  1) Definimos un conjunto: el conjunto paises; y a su vez, y los elementos que lo compononen (paises de America).
  2) Definimos una variable (el nombre del pais).
  3) Hacemos una serie de condicionales evaluando si la variable (nombre_pais) corresponde a un elemento del conjunto paises.
  4) Si si, asignamos la capital correspondiente al pais, como la impresion predeterminada del condicional. 
 

## Decimo punto
Escriba un programa que dada una distancia calcule:
- El tiempo que le tomaría a la luz recorrer la distancia.
- El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
- El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
- El tiempo que le tomaría a Bolt recorrer la distancia.

```Python
# Leer un numero real, la distancia
Distancia:float
Distancia = float(input("Ingrese una distancia en metros: "))

# Asignar y realizar la operacion determinada para cada caso
Tiempo_Luz= Distancia/299792458
Tiempo_Sonido = Distancia/343.2
Tiempo_Vehiculo_Comercial = Distancia/141.111
Tiempo_Usaint_Bolt = Distancia/11.6667
print("El tiempo que le tomaría a la luz recorrer la distancia: " + str(Tiempo_Luz) + " Seg")
print("El tiempo que le tomaría al sonido (en el aire) recorrer la distancia: " + str(Tiempo_Sonido)  + " Seg")
print("El tiempo que le tomaría al vehiculo comercial más veloz (SSC Tuatara) recorrer la distancia: " + str(Tiempo_Vehiculo_Comercial)  + " Seg")
print("El tiempo que le tomaría a Bolt recorrer la distancia: " + str(Tiempo_Usaint_Bolt) + " Seg" )
```

 - Explicacion:
   1) Definimos las variables (la distancia) un numero real (del tipo float) en metros.
   2) Definimos las formulas para cada incongita, siguiendo distancia/velocidad (de la luz, del sonido, de un vehiculo comercial y de Bolt) respectivamente, en m/s.
   3) Imprimimos los valores obtenidos de las operaciones con los mensajes correspondientes para cada incognita.





