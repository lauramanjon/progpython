#Leer una empleado
def cargar_empleado():
    nombre=input("Introduce un nombre:")
    sueldo=int(input("Introduce un sueldo:"))
    return(nombre,sueldo)

#Visualizar el mayor sueldo de dos empleados
def mayorsueldo(empleado1,empleado2):
    if(empleado1[1]>empleado2[1]):
        print("El mayor sueldo lo tiene",empleado1[0],"con",empleado1[1])
    else:
        print("El mayor sueldo lo tiene",empleado2[0],"con",empleado2[1])
#Programa principal
empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
