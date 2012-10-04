"""
HW3, #10
L12, #5

Add a button and an entry widget to the guifit.py. Pressing the
button generates as many random points as the value of the entry
widget. Consider the fitting polynomial for increasing degrees, i.e.:
explore what happens if the degree of the scale is set higher.


Need to combine this with GUI fit!!!!!

"""
from Tkinter import *
import numpy as np
from mouseptsadd import AddPoints


import random

class RandPoints(AddPoints):
   def __init__(self,wdw,r,c,output=False):
      
      self.addpts = AddPoints(wdw,r,c,output)
      wdw.title("visualizing polyfit")
      self.f = Entry(wdw)
      self.f.grid(row=1,column=1)
      self.b = Button(wdw,text="Add # Random Points Points"\
                      , command=self.rand_points)
      self.b.grid(row=2,column=1)
      self.rows=r
      self.cols=c
      # Adjust the size of the random dots
      self.size=10

   
   def rand_points(self):
      n=self.f.get()
      n=int(eval(n))
      #print n
      ap=self.addpts
      #print self.rows
      #col=c
      for i in range (1,n):
         i=random.randint(1, self.rows)
         j=random.randint(1, self.cols)
         x0=i*self.size-self.size/2; x1=x0+self.size;
         y0=j*self.size-self.size/2; y1=y0+self.size;
         ap.c.create_oval(x0,y0,x1,y1,fill="red")
         #print i
         #print j


def main():
   top = Tk()
   r = 50; c = 50
   show = RandPoints(top,r,c,True)
   top.mainloop()

if __name__ == "__main__": main()
