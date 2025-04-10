import sys

def geny(n):
    for i in range(n):
        yield i**2

g= geny(10)
x= [i**2 for i in range(10000)]

print(sys.getsizeof(x))
print(sys.getsizeof(g))