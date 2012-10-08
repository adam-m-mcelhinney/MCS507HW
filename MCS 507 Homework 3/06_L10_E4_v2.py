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


def x_vals(a,b,n):
    """
    Creates the list of new x_values and appends it to the old list
    """
    h=(b-a)/float(n)
    x_val=[a+j*h for j in range(0,n+1)]
    

    return x_val, h

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
            #print y_vals[key]

print y_vals


def final(y_vals,x,coeff,h):
    """
    Calculates the new values of Simpsons rule
    """
    s=0
    for i in range(0,len(x)):
        print y_vals[x[i]]
        s=s+coeff[i]*y_vals[x[i]]
        #print coeff[i]*y_vals[x[i]]
        
    s=s*(h/3.0)
    return s
    
            

###def test():
##a=0
##b=1
##x=[]
##y=[]
##f= lambda z: z**5
##f_x=f
##start=4
##max_double=3
##n=start
####for i in range(0,max_double):
##h=(b-a)/float(n)
##x_new=x_vals(a,b,n)
##y_calc(x_new,f_x)
##c=create_coeff(n)
##print c
##t=final(y_vals,x_new,c)




def test():
    a=0
    b=1
    f= lambda z: z**5
    start=4
    n=start
    c=create_coeff(n)
    print 'coeffs: '+ str(c)
    x, h=x_vals(a,b,n)
    print 'x vals: '+str(x)
    y=y_calc(x,f)
    print 'y vals: '+str(y)
    t=final(y_vals,x,c,h)
    print t
    return c,x,y,t



if __name__=="__main__": t=test()
