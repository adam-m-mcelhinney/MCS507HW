# L-5 MCS 507 Fri 7 Sep 2012 : mtbf.py

# We simulate the Mean Time Between Failures (MTBF) problem.
# The MTBF problem asks for the expected life span of a product
# made out of several components.  The multi-component product
# fails as soon as one of its components fails.
# For every component we assume that the life span follows 
# a certain normal distribution,
# determined by a mean and a standard deviation.
# In the example below we consider three components with respective
# means 11, 12, 13 and corresponding standard deviations 1, 2, 3.
# Given these means and standard deviations, what is the average
# life span of the composite product?  We run 10,000 simulations,
# using the function gauss of the random module and list comprehensions.

from random import gauss
from math import sqrt

mu1 = 11; sigma1 = 1
mu2 = 12; sigma2 = 2
mu3 = 13; sigma3 = 3
n = 10000
L1 = [gauss(mu1,sigma1) for i in xrange(n)]
L2 = [gauss(mu2,sigma2) for i in xrange(n)]
L3 = [gauss(mu3,sigma3) for i in xrange(n)]
L = [min(x,y,z) for x, y, z in zip(L1,L2,L3)]
a = sum(L)/n
S = [(e - a)**2 for e in L]
s = sqrt(sum(S)/n)
print 'average of samples : ', a
print 'standard deviation : ', s
