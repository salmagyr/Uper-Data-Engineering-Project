def fun(F):

    def wrapper(*args, **kwargs):
        print('Started')
        F(*args, **kwargs)
        print('Ended')

    return wrapper

def fun1(F):

    def wrapper():
        print('Started')
        F()
        print('Ended')

    return F

@fun
def ko(p):
    print(f'KOSHARII :? {p}')

@fun
def eo():
    print(f'shorbaa :?')

ko(3)
eo()