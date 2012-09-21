##Consider r = 1.2599210498948732. Apply the PSLQ
##algorithm to find the algebraic number that is closest to r.

from sympy.mpmath import pslq
r = 1.2599210498948732
print pslq([r**n for n in xrange(5)])

# [0, 2, 0, 0, -1]
# This shows that r is a root of 0+2*x+0*x**2+0*x**3-1x**4
# =2*x-x**4=x(2-x^3)
# The algebraic number corresponding to r is 2**(1/3.0)

print 2**(1/3.0)
