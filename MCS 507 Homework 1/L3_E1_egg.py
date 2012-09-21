from math import *
from string import *
from datetime import *

# Store all constants  here
# Verify data types with prof
M_small=47.0
M_large=67.0
Rho=1.038
c=3.7
K=5.4e-3


egg_size=raw_input('Type whether the egg is "small" or "large" ')

try:
    Temp_Water=input('Enter the temperature of the boiling water ')
    Start_Temp=input('Enter the starting temperature of the egg ')
    Target_Temp=input('Enter the target temp of the yolk ')

except:
    print 'Error: You must enter a number! Exiting program. '
    exit()


if lower(egg_size)=='small':
    M=float(M_small)
elif lower(egg_size)=='large':
    M=float(M_large)
else:
    print 'Valid egg size not entered! You must type "small", or "large". ' \
          'Exiting program.'
    exit()


# Break formula into (A/B)*C
    
A= M**(2.0/3.0)*c*Rho**(1.0/3.0)
B=K*pi**2.0*(4.0*pi/3.0)**(2.0/3.0)
C=log(.76* (float(Start_Temp- Temp_Water)/float(Target_Temp- Temp_Water)))

t=(A/B)*C

print 'Your '+egg_size+ ' egg, placed into '+ str(Temp_Water)+ ' degree water,' \
      + 'will cook from ' + str(Start_Temp) + ' degrees C to ' + str(Target_Temp) + 'degrees C' \
      + ' in ' + str(t) + ' seconds.'

