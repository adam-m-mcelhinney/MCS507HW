##Compute 5 consecutive rational approximations of the constant e,
##e = exp(1), starting at 11/4 (a 5-digit approximation) and of
##increasing accuracy.
##Verify the accuracy of the computed approximations.


from math import *
from sympy import *

# Method 1: Using the python value of e and nsimplify
print 'Method 1: \n \n \n'
for i in range(1,6):
        #print i
        tol=.05**i
        #print tol
        e_value_1=nsimplify(exp(1.0).evalf(15), tolerance=tol)
        print "The rational approximation for e is " + \
        str(e_value_1)
        dif=exp(1.0)-float(e_value_1)
        #print float(e_value_1)
        print 'This approximation is '+str(dif) + ' away from the math module value.'
         





# Method 2: using the infinite sum to calculate e

print '\n \n \nMethod 2: \n \n \n'

# exp(1)=sum from n=0 to inf of 1/n!

e_func=lambda x, y: x+(1.0/factorial(y))


e_value=0;
for i in range(0,9):
	e_value=e_func(e_value,i)
	if e_value>=2.7:
			dif=exp(1.0)-e_value
			print "The decimal approximation of e on the " + \
                        str(i)+'th iteration is '+ str(e_value)
			print 'The fractional approximation is '+ \
                        str(nsimplify(e_value, tolerance=.0001))
			print 'This approximation is '+str(dif) + ' away from the math module value.'
