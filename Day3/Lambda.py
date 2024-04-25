#lambda arguments : expression
x = lambda a : a + 10
print(x(3))

x = lambda a , b : a * b
print(x(4,9))

#lambda functions
def func(n):
    return lambda a : a * n 
mul = func(4)
print(mul(7))
