def insert_sort(A):
    """сортировка вставками"""
    N=len(A)
    for top in range(1, N):
        k = top
        while k>0 and A[k-1]>A[k]:  #не вылезим за границы
            A[k], A[k-1]= A[k-1],A[k]
            k-=1


def choise_sort(A):
    """сортировка выбором"""
    N=len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k]<A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """сортировка пузырька"""
    N=len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k]>A[k+1]:
                A[k],A[k+1]=A[k+1],A[k]

def test_sort(sort_algoritm):
    print("test:" + sort_algoritm.__doc__)
    print("test1: ", end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algoritm(A)
    print("Ok" if A==A_sorted else "Fail")

    print("test2: ", end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algoritm(A)
    print("Ok" if A==A_sorted else "Fail")

    print("test3: ", end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algoritm(A)
    print("Ok" if A==A_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)