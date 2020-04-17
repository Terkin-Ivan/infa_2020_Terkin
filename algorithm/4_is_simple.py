def is_simple(x):
    """Определяет простое число,
    x - целое, Если простое возвращает True, иначе False"""
    devisor=2
    while devisor<x:
        if x%devisor==0:
            return False
        devisor+=1
    return True
is_simple(4)