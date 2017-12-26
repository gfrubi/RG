# -*- coding: utf-8 -*-
from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import odeint, quad


def dphi(phi, eta, iyo):
    return(phi[1], -2*phi[1]/eta-(phi[0]**2 - iyo**2 )**(1.5)) #notar que este iy0 es el inverso del y0 que debe ir aqui

#Con esta funcion aseguramos continuidad analitica, para que la integracion no se corte
def dphialt(phi, eta, iyo):
    return(phi[1], -2*phi[1]/eta-(abs(phi[0]**2 - iyo**2))**(1.5)) 


#Definiendo las condiciones iniciales, el n,
#y el dominio de integracion

phi0 = [1.0, 0.0] #Las mismas condiciones iniciales que en Lane-Emden
eta = linspace(1.0e-30, 8.0, 1000000)


eta1s = []
eta2Tpx1s = []

yceros = linspace(0.0, 0.993, 1000)

for y in yceros:
    sol = odeint(dphialt, phi0, eta, args=(y,))
    pos = (where(sol[:,0] - y < 0)[0][0])-1
    ddphi = dphi([sol[pos,0], sol[pos,1]], eta[pos], y)[1] #segunda derivada en  la ultima posicion

    #print(ddphi) 
    Deta0 = roots([0.5*ddphi,sol[pos,1],sol[pos,0]-y])
    Deta = sort(Deta0[where(Deta0>0)])[0]
    eta1 = eta[pos]+Deta
    eta1s.append(eta1)
    eta2Tpx1 = -eta1**2*(sol[pos,1] + Deta*ddphi)
    eta2Tpx1s.append(eta2Tpx1)

erreNS = linspace(1.0e-30, 30, 10000)    
emeNS = 3.4518*(10/erreNS)**3 #En masas solares

# Caso ultra relativista, alta densidad.
Mch = 5.7252

# Ec de estado de fermi exacta
radioNS = []
masaNS = []

for i in range(len(eta1s)):
    radNS = 4.18945*eta1s[i]*yceros[i]
    masNS = 2.83673*eta2Tpx1s[i]
    radioNS.append(radNS)
    masaNS.append(masNS)

colores = ['blue','brown','red']
dasheses = [[],[5,2],[5,2,2,2]]
    
figure(figsize=(8,6))
plot(masaNS, radioNS, colores[2], dashes=dasheses[1], linewidth=1.50, label='Fermi $\mu=2$')
plot(emeNS, erreNS, colores[0], dashes=dasheses[0], linewidth=1.50, label='Lane-Emden $\gamma=5/3$')
vlines(Mch,0,30, label='$M_{Ch}/M_{\odot}$', linestyles='dashdot')
xlim(0,6)
ylim(0,30)
xlabel('masa $[M/M_{\odot}]$',fontsize=15)
ylabel('radio $[km]$',fontsize=15)
scatter(1,10, c='black')
grid(linestyle='dotted')
legend()
savefig('../fig/fig-fermineutron-masa-radio.pdf')


