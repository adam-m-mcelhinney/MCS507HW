"""
HW3, #6
L10, #4

4. Write code for your own composite Simpson rule to be used in an
iterator fashion. Organize the computations so that all previous
function evaluations are recycled.

Question: For composite rule, do we have to chop the area into different intervals?
See wikipedia

WRONG!

"""

from scipy import linspace
from scipy.integrate import simps



# Evaluate the function for all x's
#y_int=[f_x(x_new[i]) for i in range(0,len(x_new))]
# create the coefficient list
def create_coeff(n):
    """
    Creates the coefficient list for composite simpson
    [1,4,2,4,2,4,.....,1]
    """
    coeff=[1]
    for i in range(0,n-1):
        if i%2==0:
            coeff.append(4)
        else:
            coeff.append(2)
    coeff.append(1)
    return coeff


def x_vals(x,a,h,n):
    """
    Creates the list of new x_values and appends it to the old list
    """
    print 'h:'+str(h)
    for i in range(len(x),n+1):
        if __name__=="__main__": print 'x val:' + str(i)
        x.append(a+i*h)

    return x

y_vals={}

def y_calc(x,f):
    """
    Evaluates f at every new value of x and append to y_vals
    """
    for i in range(0,len(x)):
        try:
            y_vals[x[i]]
        except KeyError:
            key=x[i]
            y_vals[key]=f(x[i])
            print y_vals[key]

print y_vals


def final(h,y,x,coeff):
    """
    Calculates the new values of Simpsons rule
    """
    s=0
    for i in range(0,len(y)):
        s=s+coeff[i]*y[x[i]]
        
        if __name__=="__main__": print 'coeff:' + str(coeff[i])+' y:' + str(y[x[i]])


    s=s*(float(h)/3.0)

    return s
    
            

#def test():
a=0
b=1
x=[]
y=[]
f= lambda z: z**5
f_x=f
start=4
max_double=3
n=start
##for i in range(0,max_double):
h=(b-a)/float(n)
x_new=[a+j*h for j in range(0,n+1)]
y_calc(x_new,f_x)
c=create_coeff(n)
print c
t=final(h,y_vals,x_new,c)
print t

s=0
for i in range(0,len(y_vals)):
    print y_vals[x_new[i]]
    s=s+c[i]*y_vals[x_new[i]]
    print c[i]*y_vals[x_new[i]]

s=s*(h/3.0)


#if __name__=="__main__": t=test()    


