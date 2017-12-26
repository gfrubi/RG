# -*- coding: utf-8 -*-

from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import odeint, quad

#Aca definimos el sistema de ecuaciones
def dm_dt(m_t, equis):
    #retorna dm, dt
    m = m_t[0]
    t = m_t[1]
    dmdx = equis**2*(sinh(t)- t)
    
    dtdx = (-4.0/(equis*(equis-2.0*m)))*((equis**3/3.0)*(sinh(t) 
                    - 8.0*sinh(t/2.0) + 3.0*t) + m)*((sinh(t) - 2.0*sinh(t/2.0))/(cosh(t)-4.0*cosh(t/2.0)+3.0))
    return (dmdx, dtdx)


te0 = [6.0, 4.0, 3.0, 2.0, 1.0]
equisa = linspace(1.0e-4, 2.0, 1000)

fig, axes = subplots(figsize=(8,6))
colores = ['blue','red','brown','purple','black']
dasheses = [[],[5,2],[5,5],[5,2,2,2],[2,2]]
for c, d, y in zip(colores,dasheses,te0):
    m0_t0 = [0.0, y]
    sol = odeint(dm_dt, m0_t0, equisa)
    axes.plot(equisa[:], sol[:, 0], c, dashes=d, label='$t_0 = %1.1f$'%y, linewidth=1.50)
    axes.legend(loc='best')
    axes.set_xlabel('Radio (adimensional) $x$',fontsize=15)
    axes.set_ylabel('Función de masa (adimensional) $m(x)$',fontsize=15)
    axes.set_xlim([0,2])
    axes.set_ylim([0,0.1])
    axes.grid(linestyle='dotted')
fig.savefig('../fig/fig-fermi-rel-m-x.pdf')


