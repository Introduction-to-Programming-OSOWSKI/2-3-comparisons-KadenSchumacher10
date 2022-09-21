from tkinter import TRUE


def greaterThan(a,b):
    if a > b:
        return True
    else:
        return  False
def lessThan(c, d):
    if c < d:
        return True
    else:
        return False
def equalTo(e, f):
    if e == f:
        return True
    else:
        return False
def greaterOrEqual(g, h):
    if g >= h:
        return True
    else:
        return False
def lessOrEqual(i, j):
    if i <= j:
        return True
    else:
        return False

print(greaterThan(6, 10))
print(lessThan(99, 100))
print(equalTo(23, 23))
print(greaterOrEqual(101, 100))
print(lessOrEqual(100, 100))