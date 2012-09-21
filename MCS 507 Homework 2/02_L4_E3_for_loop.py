"""
Lecture 4, Exercise 3
Replace the for loop in comptraprule.py by an equivalent
while loop.
"""


from scitools.StringFunction \
import StringFunction

# Modified
formula = raw_input('give a function in x : ')
f = StringFunction(formula)
a = input(' what is left end of [a,b] ? ')
b = input('what is right end of [a,b] ? ')
n = input('give number of evaluations : ')
h = (b-a)/float(n)
s = (f(a) + f(b))/2
i=1
while(i<n):
#for i in range(1,n):
   #print i
   s = s + f(a+i*h)
   i=i+1
s = s*h
print 'approximate integral :', s



# Original
formula = raw_input('give a function in x : ')
f = StringFunction(formula)
a = input(' what is left end of [a,b] ? ')
b = input('what is right end of [a,b] ? ')
n = input('give number of evaluations : ')
h = (b-a)/float(n)
s = (f(a) + f(b))/2
for i in range(1,n):
   #print i
   s = s + f(a+i*h)
s = s*h
print 'approximate integral :', s
