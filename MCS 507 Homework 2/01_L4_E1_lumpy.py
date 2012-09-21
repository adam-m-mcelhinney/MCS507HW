"""
Lecture 4, Exercise 1
Type L = [3, 9]; K = L; K[1] = 6 in an interactive Python
session. Sketch (or use Lumpy) the relations between K and L.
"""
from scitools.Lumpy import Lumpy
lumpy = Lumpy()
lumpy.make_reference()

L=[3,9]; K=L; K[1]=6

lumpy.object_diagram()
