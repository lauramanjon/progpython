#Definir lista vacia
alumnos=[]
nota=[]
#Agregamos 4 nombres de alumnos y notas
for x in range(4):
    nombre=input("Introduce un alumno:")
    alumnos.append(nombre)
    valor=float(input("Introduce una nota:"))
    nota.append(nota)
#Visualizar los productos superior al primero
muybueno=0
for x in range(4):
    if precios[x]<4:
        print(alumnos[x],"Insuficiente")
    else:
        if notas[x]<=7:
            print(alumnos[x],"Bueno")
        else:
            muybueno=muybueno+1
            print(alumnos[x],"Muy bueno")

print("Alumnos muy bueni:",muybueno)
