from contextlib import contextmanager

@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()