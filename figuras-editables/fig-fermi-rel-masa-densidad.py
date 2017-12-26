# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import odeint, quad

def dm_dt(m_t, equis):
    #retorna dm, dt
    m = m_t[0]
    t = m_t[1]
    dmdx = equis**2*(sinh(t)- t)
    
    dtdx = (-4.0/(equis*(equis-2.0*m)))*((equis**3/3.0)*(sinh(t) 
                    - 8.0*sinh(t/2.0) + 3.0*t) + m)*((sinh(t) - 2.0*sinh(t/2.0))/(cosh(t)-4.0*cosh(t/2.0)+3.0))
    #print(unoportres)
    return (dmdx, dtdx)

####################################################################
####### Parte relativista ##########################################
####################################################################
te_0b = linspace(0.1,10.5,1200)
equis = linspace(1.0e-6, 15.0, 1000)

x1s = []
m1s = []


for t in te_0b:
    m0_t0 = [0.0, t]
    sol = odeint(dm_dt, m0_t0, equis)
    if len(where(sol[:,0]<0)[0]) is not 0:
        pos = (where(sol[:,0] < 0)[0][0])-1#tiene algunos nan, por eso se cae
    elif len(where(isnan(sol[:,0])==True)[0]) is not 0:
        pos = where(isnan(sol[:,0])==True)[0][0]-1 #Es para la solucion de t   XXXXXXXXXXXXXXXXXX
    dte = dm_dt([sol[pos,0], sol[pos,1]], equis[pos])[1] #el valor de dt en la pos
    #aqui solo podemos hacer una extrapolacion lineal (una recta), pues no tenemos la segunda derivada
    x1 = equis[pos] - sol[pos,1] / dte   
    x1s.append(x1)
    dme = dm_dt([sol[pos,0], sol[pos,1]], equis[pos])[0] #el vamos de dm en la pos
    m1 = dme * (x1 - equis[pos]) + sol[pos,0] #esto es m(x1)
    m1s.append(m1) 

densidad = 5.725e17*(sinh(te_0b) - te_0b) #  kg/m^3
radio = 13.683*array(x1s) # km
masa = 9.2648*array(m1s) #en masas solares

def dphialt(phi, eta, iyo):
    return(phi[1], -2.0*phi[1]/eta-(abs(phi[0]**2 - iyo**2))**(1.5)) 
def dphi(phi, eta, iyo):
    return(phi[1], -2.0*phi[1]/eta-(phi[0]**2 - iyo**2 )**(1.5)) 

####################################################################
####### Parte newtoniana ###########################################
####################################################################
phi0 = [1.0, 0.0] #Las mismas condiciones iniciales que en Lane-Emden
eta = linspace(1.0e-30, 40.0, 1000)

eta1s = []
eta2Tpx1s = []
rhoNS = []
radioNS = []
masaNS = []

yceros = linspace(0.0, 0.9997, 1000)

for y in yceros:
    sol = odeint(dphialt, phi0, eta, args=(y,))
    pos = (where(sol[:,0] - y < 0)[0][0])-1
    ddphi = dphi([sol[pos,0], sol[pos,1]], eta[pos], y)[1] #segunda derivada en  la ultima posicion

    #print(ddphi) 
    Deta0 = roots([0.5*ddphi,sol[pos,1],sol[pos,0]-y])
    Deta = sort(Deta0[where(Deta0>0)])[0]
    eta1 = eta[pos]+Deta
    eta1s.append(eta1)
    eta2Tpx1 = -eta1**2.0*(sol[pos,1] + Deta*ddphi)
    eta2Tpx1s.append(eta2Tpx1)

radioNS = 4.18945*array(eta1s)*yceros
masaNS = 2.83673*array(eta2Tpx1s)
rhoNS = 6.10656e18 * (yceros**(-2.0) - 1.0)**(3.0/2)
    
  
erreNS = linspace(1.0e-30, 30, 10000)    
emeNS = 3.4518*(10.0/erreNS)**3 #En masas solares

# Caso ultra relativista, alta densidad.
Mch = 5.7252

colores = ['blue','brown','red', 'purple']
dasheses = [[],[5,2],[5,2,2,2],[2,2]]

masita = linspace(0,6,10000)
radio_s = 2.953699653*masita  #radio de Schwarzschild



fig, axes = subplots(figsize=(8,6))
axes.plot(densidad, masa,  colores[3], dashes=dasheses[3], linewidth=1.50, label='RG')
axes.plot(rhoNS, masaNS, colores[2], dashes=dasheses[1], linewidth=1.50, label='Newton')
axes.legend(loc='best')
axes.set_xlabel('Densidad central $[kg/m^3]$',fontsize=15)
axes.set_ylabel('Masa $[M/M_{\odot}]$',fontsize=15)
axes.set_xlim([1e15,1e21])
axes.set_ylim([0,1])
axes.semilogx() 
axes.grid(linestyle='dotted')
fig.savefig('../fig/fig-fermi-rel-masa-densidad.pdf')
#fig.show()

