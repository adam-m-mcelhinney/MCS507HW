"""
HW3, #4
L9, #5
Adjust the sympy script to compute an integration rule that
integrates all cubics exactly.


ASK PROF!!!

Take two points in middle and average
a+ (b-a)/3
and
a + (2/3)(b-a)

solve for weights, will have four equations and four unknowns



"""

from sympy import *
var('a,b,wa,wm,wb')
rule = lambda f: wa*f(a) + wm*f((a+b)/2) + wb*f(b)
var('f')
print 'making the rule', rule(f)
# the basic functions are 1, x, and x**2
b0 = lambda x: 1
b1 = lambda x: x
b2 = lambda x: x**2
# require that b0, b1, b2 are integrated exactly
var('x')
e0 = rule(b0) - integrate(b0(x),(x,a,b))
e1 = rule(b1) - integrate(b1(x),(x,a,b))
e2 = rule(b2) - integrate(b2(x),(x,a,b))
# for the user, we print the equations
print 'solving 3 equations :'
print e0,'== 0'
print e1,'== 0'
print e2,'== 0'
# the equations are easy to solve:
R = solve((e0,e1,e2),(wa,wm,wb))
print R
v = rule(f)
s = Subs(v,(wa,wm,wb),(R[wa],R[wm],R[wb])).doit()
formula = factor(s)
print 'Simpson formula :', formula
r = lambda f: (b-a)*(f(a) + 4*f((a+b)/2) + f(b))/6
# verifying if every quadric is integrated exactly
var('c0,c1,c2')
q = lambda x: c0 + c1*x + c2*x**2
vr = simplify(r(q))
print 'approximation :', vr
er = integrate(q(x),(x,a,b))
print '  exact value :', er
print '    the error :', vr - er


# verifying cubics
var('c0,c1,c2,c3')
q = lambda x: c0 + c1*x + c2*x**2+c3*x**3
vr= simplify(r(q))
er = integrate(q(x),(x,a,b))
vr-er



### Verify
from scipy.integrate import simps
from scipy import linspace

f = lambda x1: 4*x1**3+100
x1=linspace(.5,1.5,3000)
y=f(x1)
s1=simps(y,x1)
print s1
simplify(r(f))
print -.5**4 - 100*.5 + 1.5**4 + 100*1.5

