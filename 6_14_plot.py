import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.cm as cm


fig = plt.figure()
ax=fig.add_subplot(111,aspect='equal')


N=2
Mmax=2
Mmin=1

def is_element_of_U_1(x,y):
    for n in range(1,N):
        for i in range(0,n):
            if((  2/(2*n+1) < x < 1/n )and( (1 - n*x + i*x) < y < (i+1)*x - (1- n*x) ) ):
                return(1)
    return(0)

def is_element_of_U(x,y,m):
    if( all( is_element_of_U_1(x/m,(y+i)/m) for i in range(0,m) ) ):
        return(1)
    return(0)

xs=np.arange(0.0,1.0,0.005)
ys=np.arange(0.0,1.0,0.005)
colors='rbgcmyk'

for m in range(Mmin,Mmax):
    for x in xs:
        for y in ys:        
            if is_element_of_U(x,y,m):
                ax.scatter(x,y,marker='o',s=0.2,c=colors[m-1],alpha=0.5)
            
plt.show()
    