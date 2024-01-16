#Definir lista vacia
nombres=[]
sueldos=[]
#Agregamos 5 nombres y sueldos
for x in range(5):
    nombre=input("Introduce un nombre:")
    nombres.append(nombre)
    valor=int(input("Introduce una nota:"))
    sueldos.append(nota)
#Visualizar la persona con mayor sueldo y con menor sueldo
print("Alumnos aprobados:")
for x in range(10):
    if notas[x]>=5:
        print(nombres[x]," ",notas [x])
print("Alumnos suspensos:")
for x in range(10):
    if notas[x]<5:
               print(nombres[x]," ",notas[x])
