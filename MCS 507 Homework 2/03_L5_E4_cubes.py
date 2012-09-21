"""
Lecture 5, Exercise 4
Generate a sequence of cubes x 3, for x ranging over all natural
numbers between 1 and 70. To determine which cubes are
squares of natural numbers, take the square root of those cubes
and select those numbers which have a natural number as their
square root.
"""
from math import sqrt

n=70

cubes=[i**3 for i in range(1,n+1)]
squares=[sqrt(i) for i in cubes]

natural=[]

for i in range(0,len(squares)):
    if squares[i]==int(squares[i]):
        natural.append(squares[i])
