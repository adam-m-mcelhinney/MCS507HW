"""
MCS H2, L7 E2
Compute the length of a path in the plane given by a list of
coordinates (as tuples), see Exercise 3.4.

Exercise 3.4. Compute the length of a path.
Some object is moving along a path in the plane. At n points of
time we have recorded the corresponding (x, y) positions of the object:
(x0, y0), (x1, y2), . . ., (xn−1, yn−1). The total length L of the path from
(x0, y0) to (xn−1, yn−1) is the sum of all the individual line segments
((xi−1, yi−1) to (xi, yi), i = 1, . . . , n − 1):
L =
nX−1
i=1
p
(xi − xi−1)2 + (yi − yi−1)2 . (3.9)
Make a function pathlength(x, y) for computing L according to
the formula. The arguments x and y hold all the x0, . . . , xn−1 and
y0, . . . , yn−1 coordinates, respectively. Test the function on a triangular
triangular
path with the four points (1, 1), (2, 1), (1, 2), and (1, 1). Name of
program file: pathlength.py.
"""


def path_length(c):
    """Compute the length of a path in the plane given by a list of
    coordinates (as tuples)
    """
    from math import sqrt
    # Break problem into the sum of the x coordinates
    # and the sum of the y coordinates

    # Extract list of all the x and y coordinates
    x_coord=[c[i][0] for i in range(0,len(c))]
    y_coord=[c[i][1] for i in range(0,len(c))]

    # Compute x length and y length
    x=0;y=0
    for i in range(1,len(c)):
        x=x+(x_coord[i]-x_coord[i-1])**2
        y=y+(y_coord[i]-y_coord[i-1])**2

    total_len=sqrt(x+y)
    return total_len

#c=[(1,1),(2,1),(1,2),(1,1)]
#c=[(4,1),(20,1),(1,23),(1,11)]
#c=[(1,4),(4,6)]
print path_length(c)

