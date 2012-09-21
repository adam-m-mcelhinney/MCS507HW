"""
HW 1, Q
Lecture 7, Exercise 1
The function numpy.linspace(a,b,n) returns a list of n
equally spaced points in [a,b]. Write your own function definition
for linspace. You may assume that n is at least 2 and a < b.
"""

def adam_linespace(a,b,n):
    from numpy import array
    # Step size
    s=float(b-a)/float(n-1)
    return array([a+s*i for i in range(0,n)])

s=1
e=1000
n=8
x=adam_linespace(s,e,n)

from numpy import linspace
y=linspace(s,e,n)

print x
print y
print x-y




    
    
    
