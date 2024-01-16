#Definir lista vacia
productos=[]
precios=[]
#Agregamos 5 nombres de productos y precios
for x in range(5):
    nombre=input("Introduce un producto:")
    productos.append(nombre)
    valor=float(input("Introduce un precio:"))
    precios.append(precios)
#Visualizar los productos superior al primero
print("El precio del primer productos, ",productos[0],"es",precios[0])
print("Los productos con precio superior son:")
for x in range(1,5):
      if(precios[x]>precios[0]):
          print(productos[x],"",precios[x])
