"""
HW3, #9 and #10
L12, #1 and #5

#1. Add buttons random and clear to the GUI to add points with
mouse clicks. When pressed, the button random adds a random
point to the list and shows it, while the clear button clears the
canvas and clears the list of stored points.

#5. Add a button and an entry widget to the guifit.py. Pressing the
button generates as many random points as the value of the entry
widget. Consider the fitting polynomial for increasing degrees, i.e.:
explore what happens if the degree of the scale is set higher.



"""

from Tkinter import *
import numpy as np
from mouseptsadd import AddPoints
import random

class FitPoints(AddPoints):
   """
   Visualizing polyfit.
   """
   def __init__(self,wdw,r,c,output=False):
      """
      We instantiate the AddPoints GUI
      and add a scale for the degree of
      the polynomial that fits the points.
      """
      self.addpts = AddPoints(wdw,r,c,output)
      wdw.title("visualizing polyfit")
      # define the scale next to the canvas
      self.degree = IntVar()
      self.fitdeg = Scale(wdw,orient='vertical',
         length=r*self.addpts.mag,label='degree',
         from_=0,to=10,resolution=1,
         variable=self.degree,command=self.Fit)
      self.fitdeg.grid(row=0,column=1)

      ## Add  button to clear all points
      self.cl = Button(wdw,text="Clear All Points"\
                      , command=self.clear_points)
      self.cl.grid(row=3,column=1)

      ## Add random points to plot
      self.f = Entry(wdw)
      self.f.grid(row=1,column=1)
      self.b = Button(wdw,text="Add # Random Points Points"\
                      , command=self.rand_points)
      self.b.grid(row=2,column=1)
      self.rows=r
      self.cols=c

   def clear_points(self):
      """
      Clears the points by "drawing" the points again
      """
      ap=self.addpts
      L= ap.points
      print L
      m=len(L)
      x=[L[j][0]*ap.mag for j in range(0,m)]
      y=[L[j][1]*ap.mag for j in range(0,m)]
      for i in range(0,m):
         print 'Points left: '+ str(ap.points)
         ap.DrawCircle(x[i],y[i])

         

   def rand_points(self):
      n=self.f.get()
      n=int(eval(n))
      #print n
      ap=self.addpts
      #print self.rows
      #col=c
      for i in range (1,n):
         i=random.randint(1, self.rows*ap.mag)
         j=random.randint(1, self.cols*ap.mag)
         ap.DrawCircle(i,j)
         #print i
         #print j

      
   def ShowFit(self,p,d):
      """
      Displays the fitting polynomial p
      of degree d.
      """
      ap = self.addpts
      name = 'fit' + str(d) + "-"
      for i in xrange(0,ap.rows*ap.mag):
         x = float(i)/ap.mag
         y = np.polyval(p,x)
         j = y*ap.mag
         name = name + str(i)
         ap.c.delete(name)
         ap.c.create_oval(i-1,j-1,i+1,j+1,
            fill="red",tags=name)

   def DeleteFit(self,d):
      """
      Deletes the fitting polynomial p
      of degree d.
      """
      ap = self.addpts
      name = 'fit' + str(d) + "-"
      for i in xrange(0,ap.rows*ap.mag):
         name = name + str(i)
         ap.c.delete(name)

   def Fit(self,v):
      """
      Calls polyfit and displays
      the fitting polynomial.
      """
      ap = self.addpts
      d = self.degree.get()
      L = ap.points
      if ap.output:
         print 'the points :', L
         print 'the degree :', d
      for i in xrange(len(L),5):
         self.DeleteFit(i)
      if(len(L) > d):
         A = np.array([x for (x,y) in L])
         B = np.array([y for (x,y) in L])
         p = np.polyfit(A,B,d)
         if ap.output:
            print 'fitting polynomial = '
            print p
         self.ShowFit(p,d)

def main():
   top = Tk()
   # r = input('Give #rows : ')
   # c = input('Give #columns : ')
   r = 50; c = 50
   show = FitPoints(top,r,c,True)
   top.mainloop()

if __name__ == "__main__": main()
