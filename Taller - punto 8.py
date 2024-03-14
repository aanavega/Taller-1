
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
