#x = [i**2 for i in range(10000000000)]

class Gen:
    def __init__(self, n):
        self.n=n
        self.last=0

    def __next__(self):
        return self.b3d()

    def b3d(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last +=1
        return rv

g = Gen(10)

while True:
    try:
        print(g.b3d())
    except StopIteration:
        break