N=5
A=[0,1,2,3,4]
#сдвиг влево
tmp=A[0]
for k in range(N-1):
    A[k]=A[k+1]
A[N-1]=tmp
print(A)
#сдвиг вправо
B=[0,1,2,3,4]
tmp=B[N-1]
for k in range(N-2,-1,-1):
    B[k+1]=B[k]
B[0]=tmp
print(B)