# L3, Q3 
# Make a sound composed of two frequencies, e.g.: one at 440 Hz
# and the other at 300 Hz, where the first has twice the amplitude of
# the other, lasting for ten seconds.

import numpy as np
# Define the sampling rate
r = 44100;
# Define the frequencies
f_1 = 440;
f_2 = 300;
# Number of seconds
m = 10; 
# Amplitude
A_1 = 1
A_2= 2*A_1
t = np.linspace(0,m,m*r);
s_1 = A_1*np.sin(2*np.pi*f_1*t)
s_2 = A_2*np.sin(2*np.pi*f_2*t)

# Can you just sum two sounds like this?
sound = np.array(s_1+s_2)

max_amplitude = 2**15-1
sound = max_amplitude*sound
sound = sound.astype(np.int16)

import scitools.sound
scitools.sound.write(sound,'atone2.wav')
scitools.sound.play('atone2.wav')
