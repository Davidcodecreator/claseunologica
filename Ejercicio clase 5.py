# Cálcular valores para a,b,c
a= int(input('Agrega la primera variable: '))
b= int(input('Agrega la segunda variable: '))
c= int(input('Agrega la tercera variable: '))
x1=0
x2=0
x1= (-b-pow(((b**2) - (4*((a)*(c)))), 1/2))/ (2 *(a))
x2= (-b+pow(((b**2) - (4*((a)*(c)))), 1/2))/ (2 *(a))
print('El resultado de x1 es : ', round(x1,2))
print('El resultado de x2 es : ', round(x2,2))