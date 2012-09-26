"""
HW3, #6
L10, #4

4. Write code for your own composite Simpson rule to be used in an
iterator fashion. Organize the computations so that all previous
function evaluations are recycled.

Question: For composite rule, do we have to chop the area into different intervals?
See wikipedia

Need to fix this

"""
from scipy import linspace
from scipy.integrate import simps

a=0
b=10
x=[]
y=[]
f_x= lambda z: z**2+100
start=6
max_double=5
n=start
##for i in range(0,max_double):
    
h=(b-a)/n
x_new=[a+j*h for j in range(0,n)]
# Evaluate the function for all x's
y_int=[f_x(x_new[i]) for i in range(0,len(x_new))]
# create the coefficient list
def create_coeff(n):
    """
    Creates the coefficient list for composite simpson
    [1,4,2,4,2,4,.....,1]
    """
    coeff=[1]
    for i in range(0,n-2):
        if i%2==0:
            coeff.append(4)
        else:
            coeff.append(2)
    coeff.append(1)
    return coeff

coeff=create_coeff(n)

def x_vals(x,a,h,n):
    """
    Creates the list of new x_values and appends it to the old list
    """
    print 'h:'+str(h)
    for i in range(len(x),n):
        if __name__=="__main__": print 'x val:' + str(i)
        x.append(a+i*h)

    return x


def y_vals(y,x,f):
    """
    Evaluates f at every new value of x and appends to y
    """
    for i in range(len(y),len(x)):
        if __name__=="__main__": print 'y val:'+ str(i)
        y.append(f(x[i]))
    return y


def final(h,y,coeff):
    """
    Calculates the new values of Simpsons rule
    """
    s=0
    for i in range(0,len(y)):
        s=s+coeff[i]*y[i]
        if __name__=="__main__": print 'coeff:' + str(coeff[i])+' y:'\
           +str(y[i])+' s val:'+ str(s)

    s=s*(float(h)/3.0)

    return s
        

def test():
    """
    Real answer is 4000./3=1333.3333333333333
    """

    from scipy.integrate import simps
    n=50
    h=(b-a)/float(n)
    x_total=x_vals([],a,h,n)
    y_tot=y_vals([],x_total,f_x)
    n=100
    h=(b-a)/float(n)
    x_total=x_vals(x_total,a,h,n)
    y_tot=y_vals(y_tot,x_total,f_x)
    coeff=create_coeff(n)
    fin=final(h,y_tot,coeff)
    s_tot=simps(y_tot,x_total)
    print fin
    print s_tot

    return x_total, y_tot, fin, s_tot


if __name__=="__main__": t=test()    
    


##
##class SimpIteratorFAST():
##    def __init__(self,f,a,b,n):
##      """
##      Initializes the state of the iterator.
##      """
##      self.f = f
##      self.a = a
##      self.b = b
##      self.n = n
##      self.y= []
##      self.i=0
##      self.x=[]
##
##
##
##
##    def next(self):
##        self.n=(2-self.i)*self.n
##        self.h=(float(self.b)-float(self.a))/self.n
##        self.xnew=[self.a+self.h*j for j in range(0,self.n-1)]
##        self.x=self.x.append(self.xnew)
##        self.y=self.f(self.x)
##        self.int=simps(self.y,self.x)
##        self.i=self.i+1
##        
##        
##
##
##
##def test(i=10):
##    """
##    Approximates the square root of 2.
##    """
##    f=lambda z: z**2 - 2.0
##    s= SimpIteratorFAST(f,0,5,1)
##    for i in range (0,i):
##        s.next()
##        print s.n
##        print s.int
##    return s
##   
##if __name__=="__main__": t=test()
##        
##        
##        
