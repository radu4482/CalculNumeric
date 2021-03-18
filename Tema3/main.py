def readMatrix(fileLink):
    file = open(fileLink, "r")
    size = int(file.readline())

    myMatrix = [[] for j in range(size)]

    file.readline()
    for f in file:
        line = f.split()
        value = float(line[0][0:len(line[0]) - 1])
        i = int(line[1][0:len(line[1]) - 1])
        j = int(line[2])
        for item in myMatrix[i]:
            if item[1] == j:
                value = value + item[0]
                myMatrix[i].remove(item)
        myMatrix[i].append((value, j))
    file.close()
    return myMatrix
def readTriagonalMatrix(fileLink):
    file = open(fileLink, "r")

    size = int(file.readline())
    p = int(file.readline())
    q = int(file.readline())

    a = [0 for i in range(size)]
    b = [0 for i in range(size)]
    c = [0 for i in range(size)]

    file.readline()
    for i in range(size):
        a[i] += float(file.readline())
    file.readline()
    for i in range(size - 1):
        b[i] += float(file.readline())
    file.readline()
    for i in range(size - 1):
        c[i] += float(file.readline())
    file.close()

    return p, q, [a, b, c]


def adauga(Matrice, i, j, value):
    for aux in (Matrice[i]):
        if aux[1] == j:
            value += aux[0]
            Matrice[i].remove(aux)
    Matrice[i].append((value, j))
    return Matrice


def adunare(Matrice, TriagonalABC, TriagonalP, TriagonalQ):
    size = len(Matrice)
    for i in range(size):
        Matrice = adauga(Matrice, i, i, TriagonalABC[0][i])
        if i + TriagonalQ < size - 1:
            Matrice = adauga(Matrice, i, i + TriagonalQ, TriagonalABC[1][i])
        if i - TriagonalP > 0 and i < size - 1:
            Matrice = adauga(Matrice, i, i - TriagonalP, TriagonalABC[2][i - TriagonalP])
    return Matrice


def getItem(Matrice, i, j):
    for aux in Matrice[i]:
        if aux[1] == j: return aux
    return 0


def getValue(Matrice, i, j):
    for aux in Matrice[i]:
        if aux[1] == j: return aux[0]
    return 0


# def inmultire(Matrice, TriagonalABC, TriagonalP, TriagonalQ):
#     size = len(Matrice)
#     matriceAux = [[] for j in range(size)]
#     # Pentru fiecare rand
#     for i in range(size):
#         myIndex = [i + TriagonalQ, i, i - TriagonalP]
#         helper = [(i, TriagonalABC[0][i])]
#         if i - TriagonalP >= 0: helper.append((i - TriagonalP, TriagonalABC[2][i - TriagonalP]))
#         if i + TriagonalQ < size: helper.append((i + TriagonalQ, TriagonalABC[1][i]))
#
#         # Exista ~3 randuri
#         for j in helper:
#             value = 0
#             # Pentru fiecare dintre cele 3
#             for k in range(len(helper)):
#                 # daca intra in parametri
#                 if 0 <= helper[k][0] < size:
#                     aux = getValue(Matrice, i, myIndex[k])
#                     # adaugam inmultirea dintre valoarea sa si valoare corespondenta in cealalta matrice
#                     value += helper[k][1] * aux
#             matriceAux[i].append((value, j[0]))
#     return matriceAux

def inmultire2(Matrice, TriagonalABC, TriagonalP, TriagonalQ):
    #initializez size-ul si o matrice auxiliara
    size = len(Matrice)
    matriceAux = [[] for j in range(size)]

    #pentru ficare linie
    for i in range(1, size - 2):
        #in matricea tridiagonala avem 3 elemente in ordinea : C(i-1) , A(i) , B(i)
        for j in range(i - 1, i + 2):
            valueTriagonal = 0

            #C
            valueTriagonal += TriagonalABC[2][i - 1] * getValue(Matrice, i - 1, j)
            #A
            valueTriagonal += TriagonalABC[0][i] * getValue(Matrice, i, j)
            #B
            valueTriagonal += TriagonalABC[1][i] * getValue(Matrice, i + 1, j)
            matriceAux[i].append((valueTriagonal, j))
    return matriceAux

def makeMatrix(helperMatrix):
    size = 2022
    myMatrix = [[0 for x in range(size)] for j in range(size)]
    for i in range(size - 1):
        for j in helperMatrix[i]:
            helper = j[0]
            myMatrix[i][j[1]] = helper
    return myMatrix


matriceInitiala = readMatrix("a.txt")

triagonalP, triagonalQ, triagonalMatrix = readTriagonalMatrix("b.txt")
#triagonalMatrix:
#[0] => lista cu elementele A cu n elemente
#[1] => lista cu elementele B cu n-1 elemente
#[2] => lista cu elementele C cu n-1 elemente

matriceTest = inmultire2(matriceInitiala, triagonalMatrix, triagonalP, triagonalQ)

matriceRezultat = readMatrix("aorib.txt")



#Verifica daca elementele din matriceTest corespund cu cele din matriceRezultat
aux = 0
for i in range(len(matriceTest)):
    for j in matriceTest[i]:
        if matriceRezultat[i].__contains__(j):
            print(f"Ok [{i}][{j[1]}]")
        #            print(f"GoodValue: {getItem(original, i, j[1])}")
        else:
            print(f"Didn't work [{i}][{j[1]}] with values: {j} and {getItem(matriceRezultat, i, j[1])}")
            #           print(f"Also original: {getItem(myMatrix, i, j[1])}")
            aux = aux + 1
print(f"{aux} errors")