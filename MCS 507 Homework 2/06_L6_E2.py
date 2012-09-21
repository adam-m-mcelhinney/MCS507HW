"""
Make a dictionary D for the ASCII code of the upper case letters,
for ’A’ to ’Z’, e.g.: D[’R’] == 82.
"""

start=ord('A')
end=ord('Z')+1
a=[chr(i) for i in range(start,end)]
b=[ord(i) for i in a]

D=dict(zip(tuple(a),tuple(b)))

