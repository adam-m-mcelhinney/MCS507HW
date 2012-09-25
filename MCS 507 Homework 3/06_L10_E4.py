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

class SimpIteratorFAST():
    def __init__(self,f,a,b,n):
      """
      Initializes the state of the iterator.
      """
      self.f = f
      self.a = a
      self.b = b
      self.n = n
      self.y= []
      self.i=0
      self.x=[]




    def next(self):
        self.n=(2-self.i)*self.n
        self.h=(float(self.b)-float(self.a))/self.n
        self.xnew=[self.a+self.h*j for j in range(0,self.n-1)]
        self.x=self.x.append(self.xnew)
        self.y=self.f(self.x)
        self.int=simps(self.y,self.x)
        self.i=self.i+1
        
        



def test(i=10):
    """
    Approximates the square root of 2.
    """
    f=lambda z: z**2 - 2.0
    s= SimpIteratorFAST(f,0,5,1)
    for i in range (0,i):
        s.next()
        print s.n
        print s.int
    return s
   
if __name__=="__main__": t=test()
        
        
        
