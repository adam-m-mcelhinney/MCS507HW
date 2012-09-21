# L-4 MCS 507 Wed 5 Sep 2012 : comptraprule.py

from scitools.StringFunction \
import StringFunction

formula = raw_input('give a function in x : ')
f = StringFunction(formula)
a = input(' what is left end of [a,b] ? ')
b = input('what is right end of [a,b] ? ')
n = input('give number of evaluations : ')
h = (b-a)/float(n)
s = (f(a) + f(b))/2
for i in range(1,n):
   s = s + f(a+i*h)
s = s*h
print 'approximate integral :', s
