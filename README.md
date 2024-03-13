# Taller-1

Realizado por Daniel Santiago Barrera y Ana Sofia Vega; a continuacion el taller #1 con los respectivos codigos, sus explicaciones y diagramas de flujo:

1. Puntos pares: programa individual con extensión .py
2. Puntos impares: programa en notebook de jupiter

## Primer punto:
Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).

<a href='https://postimg.cc/6yP3t3fh' target='_blank'><img src='https://i.postimg.cc/6yP3t3fh/Whats-App-Image-2024-03-10-at-07-54-15.jpg' border='0' alt='Whats-App-Image-2024-03-10-at-07-54-15'/></a>

 ## Segundo punto
 Realice un programa que lea tres números reales y determine cuál es el mayor.
 
 - Explicacion:
   1) Definimos las tres variables, tres numeros reales (del tipo float).
   2) Indicamos los condicionales con desigualdades, con el fin de comparar cada uno de los numeros.
   4) Definimos cual de los tres valores reales es mayor.
  
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


 - Diagrama de flujo:
   [![](https://mermaid.ink/svg/pako:eNpVj0FrwzAMhf-K0KmDlkGPga2wJoFcdlh3i3sQsZIYHLk4NmMk-e-zt26w23tPn8TTgp3TjAX21n10I_kA76USeNk1YjrjHrKGw-EZzq3Eib0DuabsnLOybWTwPJOHKHAfeyabiTITVStPRkL2Vfb18saz0dGBZpDT4xF4hi6tnbaE1BlZX906tJX9vZcAM93IX_-Ai1nH_8B9PHwXbXa1kdx7_LFKkgbcY6InMjo9u-REYRh5YoVFkpp7ijYoVLIllGJwl0_psAg-8h7jTVPg0tDgacKiJzvz9gU90Gbl)](http://https://mermaid.ink/svg/pako:eNpVj0FrwzAMhf-K0KmDlkGPga2wJoFcdlh3i3sQsZIYHLk4NmMk-e-zt26w23tPn8TTgp3TjAX21n10I_kA76USeNk1YjrjHrKGw-EZzq3Eib0DuabsnLOybWTwPJOHKHAfeyabiTITVStPRkL2Vfb18saz0dGBZpDT4xF4hi6tnbaE1BlZX906tJX9vZcAM93IX_-Ai1nH_8B9PHwXbXa1kdx7_LFKkgbcY6InMjo9u-REYRh5YoVFkpp7ijYoVLIllGJwl0_psAg-8h7jTVPg0tDgacKiJzvz9gU90Gbl)

 ## Tercer punto
 Realice un programa que lea un número entero y determine si es par o impar.
 
 - Explicacion:
   1) Definimos la variable, en este caso, un numero n entero (del tipo int).
   2) Si el residuo de este numero (n) entre 2 es 0, el numero es par.
   3) Si no es 0, es impar.

 ## Cuarto punto
 Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
 
 - Explicacion:
   1) Definimos las dos variables, dos numeros reales (del tipo float).
   2) Hacemos un condicional, con el fin de definir si el residuo del primer numero entre el segundo numero es 0.
   3) Si es 0, si es multiplo, si no es 0, no es multiplo del segundo numero
  
 ## Quinto punto
 Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
 
 - Explicacion:
   1) Definimos las tres variables, tres numero reales (del tipo float).
   2) Hacemos una serie de condicionales teniendo en cuenta la suma de los dos primeros numeros.
   3) Esto con el fin de ver si el resultado de esta suma es mayor, menor o igual al tercer numero.

 ## Sexto punto
 Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
 
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

   - Explicacion:
     1) Definimos las 5 variables, 5 numeros reales (del tipo float).
     2) Hacemos un condicional para definir el promedio de las variables ingresadas:  la suma de estas entre el numero de datos.
     3) Realizamos otro condicional para definir el promedio multiplicativo: la raiz quinta (numero de datos) del producto de todos los valores.
     4) Realizamos una serie de condicionales, con el fin de organizar los numeros de manera ascendente y descendente.
     5) Definimos una variable (potencia) y le asignamos una operacion (Sacar potencia del mayor número elevado al menor número).
     6) Definimos una ultima variable (raiz) y le asignamos una operacion (La raíz cúbica del menor número).
        
 
 ## Octavo punto
 Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.
 
 - Explicacion:
   1) Definimos una variable (la frecuencia en hz).
   2) Hacemos una serie de condicionales utilizando if y elif, y empleando a su vez desigualdades con el fin de comparar el valor ingresado.
   3) De esta manera, podemos definir en que rango del espectro electromagnético se encuentra el valor ingresado.

## Noveno punto
Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.

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

 - Explicacion:
   1) Definimos las variables (la distancia) un numero real (del tipo float) en metros.
   2) Definimos las formulas para cada incongita, siguiendo distancia/velocidad (de la luz, del sonido, de un vehiculo comercial y de Bolt) respectivamente, en m/s.
   3) Imprimimos los valores obtenidos de las operaciones con los mensajes correspondientes para cada incognita.





