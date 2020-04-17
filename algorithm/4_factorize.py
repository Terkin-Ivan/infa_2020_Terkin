def factorize(x):
    """Раскладывает на множители"""
    divizor = 2
    while x>1:
        if x%divizor==0:
            print(divizor)
            x//=divizor
        else:
            divizor+=1
factorize(999)