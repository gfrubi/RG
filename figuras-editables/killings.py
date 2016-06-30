# -*- coding: UTF-8 -*-

from matplotlib.pyplot import *
from numpy import *

R=linspace(0,4,8)
PHI=linspace(0,2*pi,17)
r,phi=meshgrid(R,PHI)
x=r*cos(phi)
y=r*sin(phi)

f1=figure(figsize=(5,5))
axes(frameon = 0)
xticks([])
yticks([])
quiver(x,y,y,-x,pivot='mid', color='b')
xlim(-5,5)
ylim(-5,5)
f1.savefig('k1.svg')

X=linspace(-4,4,10)
Y=linspace(-4,4,10)
x,y=meshgrid(X,Y)

f2=figure(figsize=(5,5))
axes(frameon = 0)
xticks([])
yticks([])
quiver(x,y,1,0,pivot='mid', color='b')
xlim(-5,5)
ylim(-5,5)
f2.savefig('k2.svg')

f3=figure(figsize=(5,5))
axes(frameon = 0)
xticks([])
yticks([])
quiver(x,y,0,1,pivot='mid', color='b')
xlim(-5,5)
ylim(-5,5)
f3.savefig('k3.svg')
