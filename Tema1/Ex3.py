def laputerea(x, putere):
    if putere == 0:
        return 1
    elif putere < 0:
        return 1 / x * laputerea(x, putere + 1)
    elif putere > 0:
        return x * laputerea(x, putere - 1)


def my_tan(x,epsilon):
    a=[0,]
    b = [1, ]
    f = [b[0], ]
    mic = laputerea(10, -12)
    if f[0] == 0: f[0] = mic
    C = [f[0], ]
    D = [0, ]
    j = 1

    teta = [0,]

    while True:
        b.insert(j,j*2+1)
        a.insert(j,-(x*x))

        D.insert(j,b[j] + a[j] * D[j - 1])
        if D[j] == 0: D[j] = mic

        C.insert(j,b[j] + a[j] / C[j - 1])
        if C[j] == 0: C[j] = mic

        D[j] = 1/D[j]

        teta.insert(j, C[j] * D[j])
        f.insert(j,teta[j] * f[j - 1])
        j = j + 1

        aux = teta[j-1] - 1
        if aux < 0: aux = aux * (-1)
        if aux < epsilon:
            break
        print(teta)
    return aux

print(my_tan(4,1))