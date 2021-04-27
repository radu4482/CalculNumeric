from Ex1 import getU
u=getU()
a=1.0
b=u/10
c=u/10
print(u)

aux1=a+b
aux2=b+c
print(f"test, aux1={aux1} , aux2={aux2} ")

aux1=aux1+c
aux2=aux2+a

if aux1==aux2 : print(f"Da, aux1={aux1} , aux2={aux2} ")
else : print(f"Nu, aux1={aux1} , aux2={aux2}")