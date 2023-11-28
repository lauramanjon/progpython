negativos=0
positivos=0
mult15=0
sumapares=0
for x in range(10):
    negativos=int(input("Negativos:"))
    if numero>0:
        positivos=positivos+1
    else:
        negativos=negativos+1
    if numero%15==0:
        mult15=mult15+1
    if numero%2==0:
        sumapares=sumapares+numero
print("Positivos:",positivos)
print("Negativos:",negativos)
print("Multiplos de 15:",mult15)
print("Suma de pares:",sumapares)



    
    
