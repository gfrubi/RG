# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import odeint, quad

#Con esta funcion aseguramos continuidad analitica, para que la integracion no se corte
def dphialt(phi, eta, iyo):
    return(phi[1], -2*phi[1]/eta-(abs(phi[0]**2 - iyo**2))**(1.5)) 

phi0 = [1.0, 0.0] #Las mismas condiciones iniciales que en Lane-Emden
eta = linspace(1.0e-30, 8.0, 1000000)
yceros = [0.0, 0.3, 0.6, 0.8, 0.9]

fig, axes = subplots(figsize=(8,6))
colores = ['blue','red','brown','purple','black']
dasheses = [[],[5,2],[5,5],[5,2,2,2],[2,2]]
for c, d, y in zip(colores,dasheses,yceros):
    sol = odeint(dphialt, phi0, eta, args=(y,))
    pos = (where(sol[:,0] - y < 0)[0][0])-1
    axes.plot(eta[:pos], sol[:pos, 0], c, dashes=d, label='$1/y_0 = %1.1f$'%y, linewidth=1.50)
    axes.legend(loc='best')
    axes.set_xlabel('Radio (adimensional) $\eta$',fontsize=15)
    axes.set_ylabel('$\phi(\eta)$',fontsize=15)
    axes.set_xlim([0,8])
    axes.set_ylim([0,1])
    axes.grid(linestyle='dotted')

fig.savefig('../fig/fig-fermi-soluciones.pdf')
#fig.show()




