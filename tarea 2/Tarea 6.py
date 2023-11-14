nota1=int(input("Introduce nota 1: "))
nota2=int(input("Introduce nota 2: "))
nota3=int(input("Introduce nota 3: "))

suma=nota1+nota2+nota3
media=suma/3
if media>=5:
    print("Estas aprobado con una media de: ",media)
else:
    print("Estás suspenso con una media de: ",media)
    
