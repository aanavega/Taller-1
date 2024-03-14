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
