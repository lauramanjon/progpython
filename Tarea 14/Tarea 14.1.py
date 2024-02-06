#Leer una lista con 5 empleados
def cargarLista():
    notas=[]
    for x in range(5):
        nota=int(input("Introduce una nota"))
        nota.append(nota)
    return notas

#Devolver el mayor y el menor de una lista de 5 elementos
def mayorMenor(notas):
    mayor=notas[0]
    menor=notas[0]
    for nota in notas:
        if nota>mayor:
            mayor=nota
        if nota<menor:
            menor=nota
    return(mayor,menor)
#Programa principal
notas=cargarLista()
mayMen=mayorMenor(notas)
print("La nota más alta es",mayMen[0])
print("La nota más baja es",mayMen[1])
