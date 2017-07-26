# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import odeint, quad
import matplotlib.pyplot as plt
style.use('classic')

def dtheta(theta, x, n):
    if modf(n)[0] == 0.0:
        return(theta[1], -2*theta[1]/x-(theta[0])**n)
    else:
        if theta[0] < 0.0 :
            return(theta[1], -2*theta[1]/x+(abs(theta[0]))**n)
        else:
            return(theta[1], -2*theta[1]/x-(theta[0])**n)

theta0 = [1.0, 0.0]
x = linspace(1.0e-30, 35.0, 1000000)
enes = [0.,1.,1.5,3.,5.]
Thetas = []
#raices=zeros(len(enes))

for i in range(len(enes)):
	sol = odeint(dtheta, theta0, x, args=(enes[i],))
	if len(where(sol[:,0]<0)[0]) is not 0:
		pos = (where(sol[:,0] < 0)[0][0])-1 #tiene algunos nan, por eso se cae
	elif len(where(isnan(sol[:,0])==True)[0]) is not 0:
		pos = where(isnan(sol[:,0])==True)[0][0]-1 
	else:
		pos = len(x)
#    thetapp=dtheta([sol[pos,0], sol[pos,1]],x[pos+1],enes[i])[1]  #Segunda derivada en la ultima posicion
#    x1 = x[pos] - sol[pos,1]/thetapp - sqrt(sol[pos,1]**2-2*sol[pos,0]*thetapp)/thetapp
#    raices[i]=x1
	Thetas.append(sol[:pos,0])  


colores=['blue','red','brown','purple','black']
dasheses=[[],[5,2],[5,5],[5,2,2,2],[2,2]]

fig, axes = plt.subplots(figsize=(8,6))
for i in range(len(enes)):
	axes.plot(x[:len(Thetas[i])], Thetas[i], colores[i], dashes=dasheses[i], label='$n = %1.1f$'%enes[i], linewidth=1.50)
axes.legend(loc='best')
#axes.set_title(u'Funciones de Lane-Emden para distintos valores de $n$')
axes.set_xlabel('$x$', fontsize=15)
axes.set_ylabel('$\Theta(x)$', fontsize=15)
axes.set_xlim(0,8)
axes.set_ylim(0,1)
axes.grid()
fig.savefig('../fig/fig-Lane-Emden.pdf')
#fig.show()



