def array_search(A:list, N:int, x:int):
    """Осуществляет поиск х в массиве А
    от 0 до N-1 индекса включительно.
    Возвр. индекс или -1, если такого нет
    если в массиве несколько одинаковых то возр. первый"""
    for k in range(N):
        if A[k]==x:
            return k
    return -1

def test_array_search():
    A1 = [1,2,3,4,5]
    m = array_search(A1, 5, 8)
    if m==-1:
        print("ok")
    else:
        print(("Fail"))

    A2 = [-1,-2,-3,-4,-5]
    m = array_search(A2, 5, -3)
    if m==2:
        print("ok")
    else:
        print(("Fail"))

    A3 = [10,20,30,10,10]
    m = array_search(A3, 5, 10)
    if m==0:
        print("ok")
    else:
        print(("Fail"))
test_array_search()