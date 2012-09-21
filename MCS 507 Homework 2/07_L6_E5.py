"""
Give Python commands to use anydbm to store antiderivation
rules for common trigonometric functions.

"""

import anydbm

libdb = anydbm.open('library','c')
# Store the derivatives
d = {'sin':'cos', 'cos':'-sin', 'tan':'1/cos'}
# Store the order of the derivatives
o = {'sin':1, 'cos':1, 'tan':2}

print type(d)
print type(o)

# Verify value of secant (1/cos)**2

def deriv(f,x):
    from math import *
    #from mpmath import sec
    g=d[f]
    order=o[f]
    return eval(str(g)+'('+str(float(x))+')')**order


print deriv('tan',2.0)
from math import pi
print deriv('sin',pi)
print deriv('cos',pi)
print deriv('tan',pi)
