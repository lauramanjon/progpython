suma=0
producto=1
for x in range(10):
    numero=int(input("Número:"))
    if x<15:
         suma=suma+numero
    else:
          producto=producto*numero

print("La suma de los 5 primeros es ",suma)
print("El prodcucto de los 5 últimos es ",producto)
