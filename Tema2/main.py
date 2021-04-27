import random


def getPrecision():
    u = 1
    aux = 0
    while u != 0 and 1 + u != 1:
        lastU = u
        u /= 10
        aux = aux + 1
    return lastU


def getDiagonal(Matrix):
    return [Matrix[i][i] for i in range(len(Matrix))]


def getRandomTerms(n):
    return [random.randrange(1000) for i in range(n)]


def generareMatricePatraticaSimetrica(n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, i):
            aux = random.randrange(-1000, 1000)
            A[i][j] = aux
            A[j][i] = aux
        A[i][i] = random.randrange(1, 1000)
    return A


def determinantMatriceTriunghiulara(Matrice):
    aux = 1
    for i in len(Matrice):
        aux *= Matrice[i][i]
    return aux


def getXofIndexInferior(BArray, Matrix, Index):
    aux = 0

    if Index == 0:
        helper = [BArray[0] / Matrix[0][0]]
        return helper

    Xi_List = getXofIndexInferior(BArray, Matrix, Index - 1)

    for i in range(0, Index):
        aux += Xi_List[i] * Matrix[Index][i]

    Xi = (BArray[Index] - aux) / Matrix[Index][Index]
    Xi_List.append(Xi)

    return Xi_List


def getXofIndexSuperior(BArray, Matrix, Index):
    size = len(BArray)
    aux = 0
    if Index == size:
        helper = [BArray[size - 1] / Matrix[size - 1][size - 1]]
        return helper
    elif Index <= 0:
        Index = 1
    Xi_List = getXofIndexSuperior(BArray, Matrix, Index + 1)
    for i in range(Index, size):
        aux += Xi_List[size - 1 - i] * Matrix[Index][i]

    Xi = (BArray[Index] - aux) / Matrix[Index][Index]
    Xi_List.append(Xi)

    return Xi_List


def getMatriceInferioara(Matrix):
    n = len(Matrix)
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, i+1):
            A[i][j] = Matrix[i][j]
    return A


def getMatriceSuperioara(Matrix):
    n = len(Matrix)
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, i+1):
            A[j][i] = Matrix[j][i]
    return A


def getColumn(Matrix, Index):
    aux = [0 for i in range(len(Matrix))]
    for i in range(len(Matrix)):
        aux[i]=Matrix[i][Index]
    return aux


def getRow(Matrix, Index):
    aux = [0 for i in range(len(Matrix))]
    for i in range(len(Matrix)):
        aux[i]= Matrix[Index][i]
    return aux


def inmultireMatrice(Matrix1, Matrix2, n):
    aux = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            sum = 0
            column = getColumn(Matrix1, i)
            row = getRow(Matrix2, j)
            for index in range(n):
                sum += (column[index] * row[index])
            aux[i][j]=sum
    return aux


# Dimensiunea sistemului = n
n = 200
# Precizia calculelor = e
e = getPrecision()
# Matricea sistemului = A
A = generareMatricePatraticaSimetrica(n)
# Vectorul termenilor liberi = b
b = getRandomTerms(n)

print("Inf")
for i in getMatriceInferioara(A):
    print(i)

print("\nSup:")
for i in getMatriceSuperioara(A):
    print(i)

sum=inmultireMatrice(getMatriceInferioara(A),getMatriceSuperioara(A),n)
print("Original Matrix:")
for i in A:
    print(i)

print("\nNext One:")
for i in sum:
    print(i)
