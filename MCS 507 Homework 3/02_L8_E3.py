"""
HW3, #2
L8, #3
Consider the problem of the previous exercise and explore the
Sage documentation on combinatorics.
Can you solve the previous exercise faster with the tools Sage has
to offer?

"""
n=4
num=[i for i in range(0,n)]
for i in range(1,n+1):
    Arrangements(num,i).list()
