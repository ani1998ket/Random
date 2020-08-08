import random
import numpy as np
import matplotlib.pyplot as plt

sample_count = 10000
inside = 0

xs = []
ys = []
color = []

for _ in range( sample_count ):
    x = random.random()
    y = random.random()
    if( (x-0.5)**2 + (y-0.5)**2 < 0.5**2 ):
        inside += 1
        color.append( "red" )
    else:
        color.append( "blue" )

    xs.append( x )
    ys.append( y )

print( 4 * ( inside / sample_count ) )
plt.scatter(xs, ys, marker='o', s=3, c=color)
plt.axis( 'scaled' )
plt.show()
