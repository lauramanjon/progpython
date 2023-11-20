coordenadax=int(input("Introduzca coordenada x: "))
coordenaday=int(input("Introduzca coordenada y: "))

if coordenadax>=0 and coordenaday>=0:
        print("La coordenada se encuentra en el primer cuadrante")
else:
    if coordenadax<=0 and coordenaday<=0:
        print("La coordenada se encuentra en el tercer cuadrante")
    else:
        if coordenadax<=0 and coordenaday>=0:
            print("La coordenada se encuentra en el segundo cuadrante")
        else:
            if coordenadax>=0 and coordenaday<=0:
                print("La coordenada se encuentra en el cuarto cuadrante")
               
            else: print("Tu número no existe")
