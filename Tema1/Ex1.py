u=1
aux=0

while u!=0 and 1+u!=1:
    lastU=u
    u/=10
    aux=aux+1


print(f"Number of iterations :{aux-1}, with {lastU}")

def getU():
    u = 1
    aux = 0

    while u != 0 and 1 + u != 1:
        lastU = u
        u /= 10
        aux = aux + 1
    return lastU
