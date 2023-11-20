from math import sqrt
a=int(input("Introduza coeficiente a: "))
b=int(input("Introduzca coeficiente b: "))
c=int(input("Introduzca coeficiente c: "))

aux=b*b-4*a*c
if aux<0:
    print("Soluciones complejas")
else:
    raiz=sqrt(aux)
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
    print("Solución 1: ",x1)
    print("Solución 2. ",x2)
