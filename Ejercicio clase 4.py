# Cálcular grados C°, F°, K°
gradosc1 = float(input('Inserta los grados Celsius a cálcular :'))
gradosf1 = float(input('Inserta los grados Farenheit a cálcular :'))
gradosk1 = float(input('Inserta los grados Kelvin a cálcular :'))
gradosc2 = 0
gradosf2 = 0
gradosk2 = 0
gradosc3 = 0
gradosf3 = 0
gradosk3 = 0
gradosc2 = gradosk1 - 273.15
gradosc3 = ((gradosf1 - 32)*5)/9
gradosk2 = gradosc1 + 273.15
gradosk3 = (((gradosf1 - 32)*5)/9) + 273.15
gradosf2 = (((gradosc1*9)/5) + 32)
gradosf3 = (((gradosk1 - 273.15)*9)/5) + 32
print('Los grados celsius que insertaste son:', round(gradosc1,2))
print('Y su conversión a grados farenheit es:', round(gradosf2,2))
print('Y su conversión a grados kelvin es:', round(gradosk2,2))
print('Los grados farenhiet que insertaste son:', round(gradosf1,2))
print('Y su conversión a grados celsius es:', round(gradosc3,2))
print('Y su conversión a grados kerlvin es:', round(gradosk3,2))
print("Los grados kelvin que insertaste son:", round(gradosk1,2))
print("Y su conversión a grados celsius es:", round(gradosc2,2))
print("Y su converisón a grados farenheit es:", round(gradosf3,2))

