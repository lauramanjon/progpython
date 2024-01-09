# Definir lista vacia
lista=[]
# Agregamos 5 nombres
for x in range(5):
    valor=int(input("Introduce un nombre:"))
    lista.append(valor)
# Calculamos cuantos cuantos tienen 5 o más caracteres
for x in range(5):
    if len(lista[x])>=5:
        print(lista[x],end="")
print()
