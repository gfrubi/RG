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


radiomu2 = []
masamu2 = []
radiomu215 = []
masamu215 = []
rho_exacta2 = []

for i in range(len(eta1s)):
    rad = 3884.9*eta1s[i]*yceros[i]
    mas = 0.72122*eta2Tpx1s[i]
    rho = 1.9478e9 * (1/yceros[i]**2 - 1.0)**(3.0/2.0)
    radiomu2.append(rad)
    masamu2.append(mas)
    rho_exacta2.append(rho)
    
erre = linspace(1.0e-30, 30000, 10000)    
eme = 0.7001*((10**4)/erre)**3

#Relacion masa-densidad para enanas blancas
##################
#Solucion lane-emden
#la relacion masa-densidad es la ecuacion (9.242)
rho_lane = (eme/0.4961)**2*1e9 

##################
#Solucion exacta
#densidad central = B(Y_0^2-1)^(3/2)
#recordar que nuestro vector yceros tiene los inversos de los y_0 de las ecuaciones
# Para enanas blancas, B = B_e = (9.256)
#rho_exacta = 1.9478e9 * (1/yceros^2 - 1.0)^(3.0/2.0)

colores = ['blue','brown','red']
dasheses = [[],[5,2],[5,2,2,2]]

figure(figsize=(8,6))
plot(rho_exacta2, masamu2, colores[2], dashes=dasheses[1], linewidth=1.50, label='Fermi $\mu_e=2$')
plot(rho_lane, eme, colores[0], dashes=dasheses[0], linewidth=1.50, label='Lane-Emden $\gamma=5/3$')
hlines(1.4562,1e6,1e13, label='$M_{Ch}/M_{\odot}$', linestyles='dashdot')
semilogx()
xlim(1e6,1e13)
ylim(0,1.5)
xlabel('densidad central $[kg/m^3]$',fontsize=15)
ylabel('masa $[M/M_{\odot}]$',fontsize=15)
grid(linestyle='dotted')
legend()
savefig('../fig/fig-fermielectron-masa-densidad.pdf')
#show()



