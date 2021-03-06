﻿"""
HW3, #3
L9, #3
To integrate f (x) = e**(−x**2)* sin(x) over [0, 1], romberg is clearly
superior over simps. Do help(quad) after from
scipy.integrate import quad and compare the
performance of this general-purpose function to romberg and
simps.

Real value= 0.29469818224912168146428093242928607188017366595729098069622884224309840761100363423064556328570738571


Call quad with full output and look at number of function evaluations

"""
from scipy.integrate import quad
from scipy import exp, sin
from math import pi
from scipy.integrate import romberg
from scipy.integrate import simps
from scipy import linspace

help(quad)
# Romberg
f_x=lambda x: exp(-x**2.0)*sin(x)
r = romberg(f_x,0,1,show=True)
print r
# 33 function evaluations

# Simpson
x=linspace(0,1,30)
y=f_x(x)
s=simps(y,x)
print s
#30 function evaluations

# Quad
y_values,err, d=quad(f_x,0,1, full_output=1)
print y_values
print err
print d
# 21 function evaluations

real=0.29469818224912168146428093242928607188017366595729098069622884224309840761100363423064556328570738571
print 'Romberg error: '+ str(abs(r-real))
print 'Simpson error: '+ str(abs(s-real))
print 'Quad error: '+ str(abs(y_values-real))

