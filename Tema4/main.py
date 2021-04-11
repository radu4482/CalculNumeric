from math import sqrt


def epsilon_value():
    aux = 1
    last_aux = aux
    while aux != 0 and aux + 1 != 1:
        last_aux = aux
        aux = aux / 10
    return aux

def read_triang_matrix(file_path):
    file = open(file_path, "r")

    size = int(file.readline())
    p = int(file.readline())
    q = int(file.readline())

    a = [0 for i in range(size)]
    b = [0 for i in range(size - p)]
    c = [0 for i in range(size - q)]

    size_b = len(b)
    size_c = len(c)

    file.readline()
    for i in range(size):
        a[i] = float(file.readline())
    file.readline()
    for i in range(size_b):
        b[i] = float(file.readline())
    file.readline()
    for i in range(size_c):
        c[i] = float(file.readline())

    file.close()

    return p, q, [a, b, c]

def read_f(file_path):
    file = open(file_path, "r")

    size = int(file.readline())

    f = [0 for i in range(size)]
    file.readline()

    for i in range(size):
        f[i] = float(file.readline())
    return f



def modul(x):
    if x < 0:
        return -x
    return x

def patrat(value):
    return value * value


def testare_myGauss(triag_details, f, myX):
    p, q, triag_matrix = triag_details
    a, b, c = triag_matrix
    size = len(a)

    for i in range(size):
        aux = 0
        if i - q > 0: aux += c[i - q] * myX[i - q]
        if i + p < size: aux += b[i] * myX[i + p]
        aux += a[i] * myX[i]
        if f[i] - aux > epsilon_value():
            return False
    return True

def getNorma(triag_details,f, x_GS):
    p, q, triag_matrix = triag_details
    a, b, c = triag_matrix
    size = len(a)

    helper=0
    for i in range(size):
        aux=0
        if i - q > 0: aux += c[i - q] * x_GS[i - q]
        if i + p < size: aux += b[i] * x_GS[i + p]
        aux += a[i] * x_GS[i]
        helper=max(helper,modul(f[i] - aux))
    return helper

def Gauss_Seidel(triag_details, f, last_X, iteration):
    p, q, triag_matrix = triag_details
    a, b, c = triag_matrix

    size = len(a)
    for i in range(size):
        if a[i] <= epsilon_value(): return False
    for i in range(size-1):
        if modul(b[i])<= epsilon_value(): return False
        if modul(c[i])<= epsilon_value(): return False


    bucket = 0
    for i in range(size):
        sum1 = 0; sum2 = 0

        #ce este inainte
        if (i - q >= 0): sum1 = c[i - q] * last_X[i - q]
        #ce este dupa
        if (i + p < size): sum2 = b[i] * last_X[i + p]
        aux = last_X[i]

        last_X[i] = (f[i] - sum1 - sum2) / a[i]
        bucket += patrat(last_X[i]-aux)
        #bucket = max(bucket,modul(last_X[i] - aux))

    #if bucket>epsilon_value():
    if sqrt(bucket)>epsilon_value():
        return Gauss_Seidel(triag_details, f, last_X, iteration + 1)
    else:
        return iteration, last_X


matrix_a = read_triang_matrix("a1.txt")
p, q, abc = matrix_a
f_array = read_f("f1.txt")
my_X = [25 for i in range(len(abc[0]))]

print("my epsilon", epsilon_value())
print("now the gauss:")
iteration, myGauss = Gauss_Seidel(matrix_a, f_array, my_X, 0)
print(f"iterations: {iteration}")
print(f"Gauss : {myGauss[0]} ,{myGauss[1]} ,{myGauss[2]} ,{myGauss[3]} ")
testare_myGauss(matrix_a, f_array, myGauss)
helper=getNorma(matrix_a,f_array,myGauss)
print(f"Norma: {helper}")