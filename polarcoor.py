import math
def recpol(x,y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan(y / x)
    return r,theta

