# Función que crea una lista de n elementos
def crearLista():
    lista=[]
    n=int(input("¿Cuántos elementos tiene la lista?"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista

# Función que multiplica los elemtos de una lista por un valor
def multiplicar(lista):
    palabra=lista[0]
    for x in range(1,len(lista)):
        if len(lista[x])>len(palabra):
            palabra=lista[x]
    return palabra

#Programa principal
lista=crearLista()
print(lista)
print("Palabra con mas caracteres:",mascarecteres(palabras))
