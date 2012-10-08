"""
HW3, #6
L10, #4

4. Write code for your own composite Simpson rule to be used in an
iterator fashion. Organize the computations so that all previous
function evaluations are recycled.



"""

class Simpsons_Rule:
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
        self.y_vals={}

    def create_coeff(self):
        """
        Creates the coefficient list for composite simpson
        [1,4,2,4,2,4,.....,1]
        """
        self.coeff=[1]
        for i in range(0,self.n-1):
            if i%2==0:
                self.coeff.append(4)         
            else:
                self.coeff.append(2)
        self.coeff.append(1)
        return self.coeff

    def x(self):
        """
        Create the list of x values
        """
        self.h=(self.b-self.a)/float(self.n)
        self.x_vals=[self.a+j*self.h for j in range(0,self.n+1)]
        return self.x_vals

    def y_calc(self):
        """
        Evaluates f at every new value of x and append to y_vals
        """
        for i in range(0,len(self.x_vals)):
            try:
                self.y_vals[self.x_vals[i]]
            except KeyError:
                key=self.x_vals[i]
                self.y_vals[key]=self.f(self.x_vals[i])
                print 'Computing values for x=' +str(key)
                #print self.y_vals[key]
        return self.y_vals

    def final(self):
        """
        Calculates the new values of Simpsons rule
        """
        self.s=0
        for i in range(0,len(self.y_vals)):
            self.s=self.s+self.coeff[i]*self.y_vals[self.x_vals[i]]
            #if __name__=="__main__": print 'coeff:' + str(self.coeff[i])+' y:' + str(self.y_vals[self.x_vals[i]])
        self.s=self.s*(float(self.h)/3.0)
        return self.s

    def next(self):
        """
        Doubles the value of n and recalculates approximation
        """
        self.n=int(2*self.n)
        self.create_coeff()
        self.x()
        self.y_calc()
        self.final()
        
        return self.n

        
if __name__=="__main__":   

    from math import exp, sin, cos, pi
    #f=lambda x: sin(x)
    f=lambda x: x*2
    start=4
    a=0
    #b=pi
    b=1
    t=Simpsons_Rule(start,f,a,b)
    print t.create_coeff()
    print t.x()
    print t.y_calc()
    print t.final()

    print t.next()
    print t.coeff
    print t.x_vals
    print t.y_vals
    print t.s

    print t.next()
    print t.coeff
    print t.x_vals
    print t.y_vals
    print t.s
    #print t.x(0,1)
    #print t.y_calc(t.x_vals,f)

    from scipy import linspace
    from scipy.integrate import simps
    y=[t.y_vals[t.x_vals[i]] for i in range(0,len(t.y_vals))]
    x=t.x_vals
    simps(y,x)


    
    
        
    
