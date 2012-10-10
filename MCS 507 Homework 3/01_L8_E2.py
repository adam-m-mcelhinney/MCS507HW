"""
HW3, #1
L8, #2
Write a script that prompts the user for a number n and that then
prints all sublists of range(n).


Ignore order
should have 2**n subset
need to include empty set

"""
import itertools

n=input('Enter the largest value to generate combinations:')

x=[i for i in range(n)]
for i in range(0,len(x)+1):
    print list(itertools.combinations(x,i))

    


