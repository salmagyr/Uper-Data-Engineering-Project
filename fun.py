def make_class(x):
    class Dog:
        def __init__(self,name):
              self.name = name
        def print_value(self):
              print(x)
    return Dog

print((make_class(10)("gogy")).name)

#print(cls)
#fy=cls("puppy")
#print(fy.name)
#fy.print_value()