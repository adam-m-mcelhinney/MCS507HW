"""
HW3, #7
L11, #2

Add an exception handler to the function add_point for when the
comma is missing or the coordinates fail to convert to floats.

WRONG!

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
   L = s.split(',')
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

def handle(db,t):
   """
   Given in t a tuple of option letter
   and argument, adds a point, returns
   a value, or prints an error message.
   """
   if t[0] == 'a':
      add_point(db,t[1])
   elif t[0] == 'v':
      value_of_point(db,t[1])
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
