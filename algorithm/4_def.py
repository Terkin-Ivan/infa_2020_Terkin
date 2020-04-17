def hello(name="World"):
    print('Hello,', name)
hello('Vasy')
hello()
#больше из двух
def max2(x,y):
    if x>y:
        return x
    return y
#больше из трех
def max3(x,y,z):
    return max2(x, max2(y,z))
print(max3(33,2,1))
print(max3(0.1, 55, 77.3))
print(max3('a','abc','dc')) #duck typing ()

def hello_separated(name="World", separator="-"):
    print('Hello,', name, sep=separator)
hello_separated("John","***")
hello_separated(separator="***")

#синхронность
#переполнение стека

