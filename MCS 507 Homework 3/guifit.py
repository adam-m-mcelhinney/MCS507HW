# L-12 MCS 275 Mon 24 Sep 2012 : guifit.py

# A GUI to play with polyfit.

from Tkinter import *
import numpy as np
from mouseptsadd import AddPoints

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
         from_=0,to=5,resolution=1,
         variable=self.degree,command=self.Fit)
      self.fitdeg.grid(row=0,column=1)

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
