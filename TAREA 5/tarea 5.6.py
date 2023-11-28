turno1=0
turno2=0
turno3=0
print("Turno de mañana:")
for x in range(5):
    edad=inr(input("Edad:"))
    turno1=turno1+edad
print("Turno de tarde:")
for x in range(6):
    edad=inr(input("Edad:"))
    turno2=turno2+edad
print("Turno de noche:")
for x in range(11):
    edad=inr(input("Edad:"))
    turno3=turno3+edad
promedio1=turno1/5
promedio2=turno2/5
promedio3=turno3/5
print("Edad media de la mañana:",promedio1)
print("Edad media de la tarde:",promedio2)
print("Edad media de la noche:",promedio3)
if promedio1>promedio2 and promedio1>promedio3:
    print("El turno de la mañana tiene mayor promedio")
else:
    if promedio2>promedio3:
        print("El turno de tarde tiene mayor promedio de edad")
    else:
        print("El turno de noche tiene mayor promedio de edad")
