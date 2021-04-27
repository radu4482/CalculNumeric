import random
from math import sin, cos
import numpy as np
from scipy.misc import derivative
from numpy.linalg import pinv,solve
from matplotlib import pyplot as plt

def epsilon():
    aux = 1
    lastaux = aux
    while aux != 0 and aux + 1 != 1:
        lastaux = aux
        aux /= 10
    return lastaux


def function1(X):
    return X ** 2 - 12 * X + 30


def function2(X):
    return sin(X) - cos(X)


def function3(X):
    return X ** 3 - 3 * X + 15


def function(functionI, x):
    y = []
    for i in range(10):
        y.append(functionI(x[i]))
    return y


def generateArrayX(x0, xn, nrValues):
    x = []
    x.append(x0)
    for i in range(nrValues - 2):
        aux = xn
        while aux - x[len(x) - 1] > (xn - x0) / (nrValues / 2) or aux == xn:
            aux = random.uniform(x[len(x) - 1], xn)
        x.append(aux)
    x.append(xn)
    return x


def modul(value):
    if value < 0: return -value
    return value

def P(m, x0, x, y):
    p = np.polyfit(np.array(x), np.array(y), m)
    aux = 0
    for i in range(m + 1):
        aux += x0 ** (m - i) * p[i]
    return aux


#--------------------------------------------------------
def Horner(x,y,m):
    ##matricea in care imi bag valorile
    B=[]
    for i in range (len(y)):
        ## fiecare linie
        aux=[]
        for j in range(m)[::-1]:
            aux.append(x[i]**j)
        B.append(aux)

    ## inversez matricea
    B = pinv(B)
    ## calculez Array ul a
    a=np.matmul(B,y)
    return a

#Calculez in mod recursiv
def valueHorner(x,a,i):
    if i==0: return a[0]
    else: return a[i]+ x*valueHorner(x,a,i-1)
#-----------------------------------------------------


def printerFunction(myFunction, x0, m):
    x = generateArrayX(x0, xn, 10)
    y = function(myFunction, x)

    print("\n")
    diferenta = 0
    for i in range(len(x)):
        myP = P(4, x[i], x, y)
        diferenta += modul(myP - y[i])
    print(f"SUMA(|Pm(Xi) - y[i]| | i=0,n) = {diferenta}")

    print(f"\n X0={x0}  "
          f"||  Pm(X0)={P(m, x0, x, y)}  "
          f"||  f(X0)={myFunction(x0)}  "
          f"||  |Pm(X0)-f(x0)|={modul(P(m, x0, x, y) - myFunction(x0))}")


def S(myX, x, y, da):
    size = len(x)
    if myX < x[0] or myX > x[size - 1]: return 0

    A = []
    last = da
    for i in range(0, size - 1):
        A.append(last)
        last = (2 * (y[i + 1] - y[i]) / (x[i + 1] - x[i])) - last
    A.append(last)

    print("x:", x, "\n", "A:", A, "\n\n")

    aux = 0
    while x[aux] > myX or myX > x[aux + 1] and aux < size - 1:
        aux += 1
    print(x[aux], " < ", myX, " < ", x[aux + 1])
    print(A[aux], " < ", "the A s", " < ", A[aux + 1], "\n")

    return ((A[aux + 1] - A[aux]) / (2 * (x[aux + 1] - x[aux]))) * ((myX - x[aux]) ** 2) + (A[aux] * (myX - x[aux])) + y[aux]


x0 = 0
xn = 7

x_test = 3.34653657
m = 6

x = generateArrayX(x0, xn, 10)
y = function(function3, x)

a=Horner(x,y,7)
print(len(a))
print(valueHorner(x_test,a,len(a)-1),function3(x_test))
Shelper=[]
for i in range(len(x)-1):
    Shelper.append(S(x[i],x,y,6))
plt.plot(x[:-1],Shelper)
plt.show()
helper = derivative(function3, x0, dx=1e-6)
#print(helper, "\n")
#print(S(1, x, y, helper))
#print(function3(2),"\n")
#print(S(.34563456, x, y, helper)-function3(.34563456))