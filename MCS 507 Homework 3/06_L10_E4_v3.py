"""
HW3, #6
L10, #4

4. Write code for your own composite Simpson rule to be used in an
iterator fashion. Organize the computations so that all previous
function evaluations are recycled.



"""

class Simpsons_Rule(start,f,a,b):
    """
    4. Write code for your own composite Simpson rule to be used in an
    iterator fashion. Organize the computations so that all previous
    function evaluations are recycled.
    """
    def __init__(self,start,f,a,b):
        """
        Store the function, the starting count, the beginning point and the end point
        """

        self.start=start
        self.f=f
        self.a=a
        self.b=b
        self.n=self.start

    def create_coeff(self,n):
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

    def x(self,self.a,self.b):
        """
        Create the list of x values
        """
        self.h=(self.b-self.a)/float(self.n)
        self.x_vals=[self.a+j*self.h for j in range(0,self.n+1)]
        return self.x_vals

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

        
    
def test():
    f=lambda x: x**2
    start=4
    a=0
    b=1
    Simpsons_Rule(start,f,a,b)
    
    
        
    
