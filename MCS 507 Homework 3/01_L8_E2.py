"""
HW3, #1
L8, #2
Write a script that prompts the user for a number n and that then
prints all sublists of range(n).


"""
import itertools

n=input('Enter the largest value to perumte:')

x=[i for i in range(n)]
for i in range(1,len(x)+1):
    print list(itertools.permutations(x,i))
    


