"""
HW3, #5
L10, #3

Make an iterator for the composite Simpson rule, using
scipy.integrate.simps. In each step of the iterator, the total
number of function evaluations doubles.

Question: For composite rule, do we have to chop the area into different intervals?
See wikipedia

"""
from scipy import linspace
from scipy.integrate import simps

class SimpIterator():
    def __init__(self,f,a,b,n):
      """
      Initializes the state of the iterator.
      """
      self.f = f
      self.a = a
      self.b = b
      self.n = n
      self.y= 0
      self.x= 0
      self.x=linspace(self.a,self.b,self.n)




    def next(self):
        
        self.x=linspace(self.a,self.b,self.n)
        self.y=self.f(self.x)
        self.int=simps(self.y,self.x)
        self.n=2.0*self.n
        



def test(i=10):
    """
    Approximates the square root of 2.
    """
    f=lambda x: x**2 - 2.0
    s= SimpIterator(f,0,5,1)
    for i in range (0,i):
        s.next()
        print s.n
        print s.int
    return s
   
if __name__=="__main__": t=test()
        
        
        
