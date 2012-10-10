"""
HW3, #7
L11, #2

Add an exception handler to the function add_point for when the
comma is missing or the coordinates fail to convert to floats.

HW3, #8
L11, #3

3 Modify the code for -v x of storepoints.py so that it returns
the value of a quadratic fit in case the value for the given x is not
stored.
"""

#! /usr/bin/python

# L-12 MCS 507 Fri 21 Sep 2012 : storepoints.py

# This script demonstrates a very simple command line interface
# to an anydbm database file to store points (x,y) in the plane.
# The following operations are supported:
# $ ./storepoints.py db=data -a 1,2
# $ ./storepoints.py db=data -v 1
# $ ./storepoints.py db=data -l
# They respectively add (1,2), lookup the value of 1,
# and list all points stored in the anydbm file data.

import anydbm
import numpy as np

def open_database(L):
   """
   Extracts the database name from the list
   of command line interfaces.
   If the database could be opened, then it
   is returned, otherwise None is returned.
   """
   for e in L:
      K = e.split('=')
      if len(K) == 2:
         try:
            db = anydbm.open(K[1],'c')
            print 'opening', K[1], 'succeeded'
            return db
         except:
            print 'opening', K[1], 'failed'
            return None
   return None

def extract_option(L):
   """
   Returns a tuple with the option letter
   and the data following the option.
   """
   for k in xrange(len(L)):
      e = L[k]
      if e[0] == '-':
         if e[1] == 'L': return ('L',None)
         try:
            return (e[1],L[k+1])
         except:
            print 'no data with option', e[1]
            return None
   return None

def add_point(db,s):
   """
   Adds the point in the string s
   encoded as x,y.
   """
   try:
      
      L = s.split(',')
      float(L[0])
      float(L[1])
   except IndexError:
      print 'The points must be seperated by a comma!'
     
   except ValueError:
      print 'Only numeric values are allowed!'
   else:
      x = L[0]; y = L[1]
      print 'adding', x, y
      db[x] = y

def value_of_point(db,s):
   """
   Prints the value of the point
   with key stored in the string s.
   """
   if db.has_key(s):
      print 'value of', s, 'is', db[s]
   else:
      print s, 'has no value'

def list_points(db):
   """
   Shows the list of points stored in db.
   """
   K = db.keys()
   for k in K:
      print '(' + k + ',' + db[k] + ')'

def fit_points(db, x):
   """
   Returns the quadratic fit in the case that the point is not stored.
   If the point is storeds, simply return the point.
   """
   x_1=str(x)
   x_2=float(x)
   if db.has_key(x_1):
      print 'value of', x_1, 'is', db[x_1]
   else:
      d=2
      X_raw=db.keys()
      X=[float(i) for i in X_raw]
      
      Y_raw=db.values()
      Y=[float(i) for i in Y_raw]
      fit=np.polyfit(X,Y,d)
      y_proj=fit[0]*(x_2**2.)+fit[1]*(x_2**1.)+fit[2]*(x_2**0.)
      print 'The fitted value of '+x_1+' is '+str(y_proj)
   

def handle(db,t):
   """
   Given in t a tuple of option letter
   and argument, adds a point, returns
   a value, or prints an error message.
   """
   if t[0] == 'a':
      add_point(db,t[1])
   elif t[0] == 'v':
      #value_of_point(db,t[1])
      fit_points(db,t[1])
   elif t[0] == 'L':
      list_points(db)
   else:
      print t[0], 'is invalid option'
    
def main():
   """
   Opens database and handles options.
   """
   import sys
   L = sys.argv
   db = open_database(L)
   if db == None:
      print 'opening of database failed'
   else:
      option = extract_option(L)
      if option == None:
         print 'no valid option found'
      else:
         handle(db,option)

if __name__=="__main__": main()


import anydbm
db = anydbm.open('test','c')
db.clear();db['1']='1';db['2']='2';db['3']='2.5'

