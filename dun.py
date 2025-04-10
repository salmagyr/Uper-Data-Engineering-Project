x = [1,2,             3]
y = [4,5]

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person({self.name})"
    def __mul__(self,x):
        if type(x) is not int:
            raise Exception("Nooop") 
        else:
            self.name = self.name * x
    def __call__(self,u):
        print(u)
    def __len__(self):
        return len(self.name)

p = Person("jody")()
print(len(p))