# L-12 MCS 275 Mon 24 Sep 2012 : mouseptsadd.py

# To illustrate the binding of mouse events to canvas,
# we add the coordinates of points marked on canvas via the mouse.

from Tkinter import *

class AddPoints():
   """
   Adding points on canvas with mouse clicks.
   """
   def BindMouseEvents(self):
      """
      Binds mouse events to the canvas,
      called at the initialization of the GUI.
      """
      self.c.bind("<Button-1>",self.ButtonPressed)
      self.c.bind("<ButtonRelease-1>",
         self.ButtonReleased)
      self.c.bind("<Enter>",self.EnteredWindow)
      self.c.bind("<Leave>",self.ExitedWindow)
      self.c.bind("<B1-Motion>",self.MouseDragged)

   def __init__(self,wdw,r,c,output=False):
      """
      The window has one column, two rows:
      + row 1: a canvas to draw points
      + row 2: a label to display coordinates
               and messages to the user.
      """
      wdw.title("adding points with mouse")
      self.mag = 10   # magnification factor
      self.rows = r   # number of rows on canvas
      self.cols = c   # number of columns on canvas
      self.c = Canvas(wdw,width=self.mag*self.cols,
         height=self.mag*self.rows,bg='white')
      self.c.grid(row=0,column=0)
      # to display mouse position :
      self.MousePosition = StringVar()
      self.MousePosition.set\
         ("put mouse inside box to add points")
      self.PositionLabel = Label(wdw,
         textvariable = self.MousePosition)
      self.PositionLabel.grid(row=1,column=0)
      # bind mouse events
      self.BindMouseEvents()
      self.points = []
      self.output = output

   def MapPixel(self,p):
      """
      Maps pixel p working mod self.mag.
      If self.mag equals 10, then
      MapPixel(248) returns 25,
      MapPixel(141) returns 14.
      """
      m = self.mag
      (x,r) = divmod(p,m)
      return (x+1 if r > m/2 else x)

   def DrawCircle(self,i,j):
      """
      Draws a blue circle on canvas with
      coordinates given at (i,j) by mouse
      and adds or removes coordinates to
      the list of points.
      """
      if self.output: print 'getting i =', i, 'j =', j
      (x,y) = (self.MapPixel(i),self.MapPixel(j))
      i0 = x*self.mag-self.mag/2; i1 = i0 + self.mag
      j0 = y*self.mag-self.mag/2; j1 = j0 + self.mag
      name = '('+str(x)+','+str(y)+')'
      if not (x,y) in self.points:
         self.c.create_oval(i0,j0,i1,j1,fill="blue",tags=name)
         self.points.append((x,y))
      else:
         self.c.delete(name)
         self.points.remove((x,y))
      if self.output: print 'list of points :', self.points

   def ButtonPressed(self,event):
      """
      Displays coordinates of button pressed.
      """
      self.MousePosition.set("currently at [ " + \
         str(event.x) + ", " + str(event.y) + " ]" + \
         " release to fill, or drag")

   def ButtonReleased(self,event):
      """
      Displays coordinates of button released.
      """
      self.MousePosition.set("drawn at [ " + \
         str(event.x) + ", " + str(event.y) + " ]" + \
         " redo to clear")
      self.DrawCircle(event.x,event.y)

   def EnteredWindow(self,event):
      """
      Displays message that mouse entered window.
      """
      self.MousePosition.set("press mouse to give coordinates")

   def ExitedWindow(self,event):
      """
      Displays message that mouse exited window.
      """
      self.MousePosition.set\
         ("put mouse inside box to add points")

   def MouseDragged(self,event):
      """
      Displays coordinates of moving mouse.
      """
      self.MousePosition.set("dragging at [ " + \
         str(event.x) + ", " + str(event.y) + " ]" + \
         " release to draw")

def main():
   top = Tk()
   # r = input('Give #rows : ')
   # c = input('Give #columns : ')
   r = 40; c = 60; o = False
   import sys
   if(len(sys.argv) > 1):
      if sys.argv[1] == 'output': o = True
   show = AddPoints(top,r,c,o)
   top.mainloop()

if __name__ == "__main__": main()
