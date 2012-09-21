"""
MCS 507, HW2
A plateau in a list is the longest sequence of the same elements
that occur in the list.
Write a Python script that reads a list and prints the start and end
index of a plateau in a given list.
"""
#from numpy import *

#A=[1,2,2,2,2,3,3,4,5]
#A=[1,2,2,2,2,3,3,4,5,5,5,5,5,5,5,4]
A=[1,2,2,2,2,3,3,4,5,5,5,5,5,5,5]
#A=[1,1,1,1,2,3,3,3]
#A=[i for i in range(1,5)]

start='';end=''
max_count=0
final_start=0
final_end=0
j=0
i=0
for i in range(0,len(A)-1):
    if A[i]==A[i+1]:
        start=i
        j=i
        count=1
        while(A[j]==A[j+1]):
            count=count+1
            j=j+1
            if (j+1)>len(A)-1:
                break
        # For ties, use the first plateau
        if count>max_count:
            max_count=count
            final_start=i
            final_end=i+count-1
            
            
        
if (final_start==0 and final_end==0):
    print 'No plateaus found! '
else:
    print 'The plateau starts at '+str(final_start)+' and ends at '+str(final_end) \
      + ' with the elements ' + str(A[final_start:final_end+1])



       
        
