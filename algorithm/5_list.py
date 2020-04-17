A=[1,2,3,4,5]
"""имена = объекты"""
print(A)
for i in A:
    print(i, type(i))
    i+=1
    print(i)
print(A)

for k in range(5):
    #старт стоп шаг
    A[k]=A[k]*A[k]
print(A)

N=5
B=[0]*N
C=[0]*N
for k in range(N):
    B[k]=int(input())
print(B)
for k in range(N):
    C[k]=B[k]
print(C)
D=[]
D=C #еще одно имя одного объекта
print(D)
E = list(A) # новый лист
