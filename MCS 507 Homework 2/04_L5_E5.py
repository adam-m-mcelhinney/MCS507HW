"""
Lecture 5, Exercise 5
Extend mtbf.py so that it works for any number of components,
prompting the user for a list of means and a list of corresponding
standard deviations.
"""
from random import gauss
from math import sqrt

mu=input('Enter a list of means ')
sigma=input('Enter a list of standard deviations whose positions \
correspond with the list of means already input ')
n = 10000

fail_time=[]
for j in range(0,n):
    
    failure=[]
    for i in range(0,len(mu)):
        failure.append(gauss(mu[i],sigma[i]))
    fail_time.append(min(failure))

a = sum(fail_time)/n
S = [(e - a)**2 for e in fail_time]
s = sqrt(sum(S)/n)
print 'average of samples : ', a
print 'standard deviation : ', s

##
##mu1 = 11; sigma1 = 1
##mu2 = 12; sigma2 = 2
##mu3 = 13; sigma3 = 3
##
##L1 = [gauss(mu1,sigma1) for i in xrange(n)]
##L2 = [gauss(mu2,sigma2) for i in xrange(n)]
##L3 = [gauss(mu3,sigma3) for i in xrange(n)]
##L = [min(x,y,z) for x, y, z in zip(L1,L2,L3)]
##a = sum(L)/n
##S = [(e - a)**2 for e in L]
##s = sqrt(sum(S)/n)
##print 'average of samples : ', a
##print 'standard deviation : ', s
