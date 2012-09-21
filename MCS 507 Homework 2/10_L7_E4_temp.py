"""
Lecture 7, Ex 4
The formula T(t) = T1 + (T(0) − T1)e−kt models the
temperature T in function of time t. For k > 0, T(t) declines and
models how an object cools off. Define a Python function that
takes as arguments T(0), T1, k, t and that returns T(t).
"""

def cool_off(T_start, T_inf, k, t):
    from math import exp
    # Break calc into T_inf+A*B
    A=float(T_start-T_inf)
    B=exp(float(-k*t))
    return T_inf+A*B



print cool_off(50, 0, -1, 10)
