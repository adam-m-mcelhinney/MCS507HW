##Determine experimentally the precision to calculate r in
##x = d2π + r so that cos(r ) is accurate within the usual precision of
##hardware floats.


#from sympy import *
from sympy.mpmath import *

print mp
mp.dps = 15
print mp

y=2*pi*10**5
z=2*pi*10**5+1
print cos(y)
print cos(z)

mp.dps = 1000
print mp

def comp_cos(x):
    d=0
    # Compute d
    while ((d+1.)*2.*pi<x):
        d=d+1
        #print d
    # Compute r
    r=x-d*2.*pi
    #print r
    return cos(r)
	
	
x=comp_cos(2.*pi*10.**5.)
print x

y=comp_cos(2.*pi*10.**5+1.)

print y
# This difference must be less than 16 decimal places
diff=cos(z)-y
print diff
diff_trunc="%.16f" % diff
print "%.16f" % diff
# mp.dps=52
    
    
        
