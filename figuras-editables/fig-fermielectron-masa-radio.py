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

for i in range(len(eta1s)):
    rad = 3884.9*eta1s[i]*yceros[i]
    mas = 0.72122*eta2Tpx1s[i]
    radiomu2.append(rad)
    masamu2.append(mas)
    
for i in range(len(eta1s)):
    rad = 3884.9*2/2.15*eta1s[i]*yceros[i]
    mas = 0.72122*(2/2.15)**2*eta2Tpx1s[i]
    radiomu215.append(rad)
    masamu215.append(mas)
    
erre = linspace(1.0e-30, 30000, 10000)    
eme = 0.7001*((10**4)/erre)**3

figure(figsize=(8,6))
colores = ['blue','brown','red']
dasheses = [[],[5,2],[5,2,2,2]]
plot(masamu2, radiomu2, colores[2], dashes=dasheses[1], linewidth=1.50, label='Fermi $\mu_e=2$')
plot(masamu215, radiomu215, colores[1], dashes=dasheses[2], linewidth=1.20, label='Fermi $\mu_e=2.5$')
plot(eme, erre, colores[0], dashes=dasheses[0], linewidth=1.50, label='Lane-Emden $\gamma=5/3$')
vlines(1.4562,0,30000, label='$M_{Ch}/M_{\odot}$', linestyles='dashdot')
xlim(0,1.5)
ylim(0,30000)
xlabel('masa $[M/M_{\odot}]$',fontsize=15)
ylabel('radio $[km]$',fontsize=15)

nombres = genfromtxt('enanas.txt', skip_header=2,  usecols=(0), dtype=str, delimiter="\t")
data = genfromtxt('enanas.txt', delimiter="\t", skip_header=2,  usecols=(3,4,5,6))
nombres[4] = ' '

M = data[:,0]
eM = data[:,1]
R = data[:,2]*695700
eR = data[:,3]*695700

errorbar(M,R,xerr=eM,yerr=eR, fmt='o', ecolor='black', c='black')
text(M[0]-0.08,R[0]-1200,nombres[0]) #SirioB
text(M[1]-0.22,R[1]-1200,nombres[1]) #Stein
text(M[2]-0.16,R[2]+300,nombres[2]) #40eriB
text(M[3]-0.10,R[3]-1200,nombres[3]) #ProcyonB
text(0.62,(0.011+0.0012)*695700,'Van Maannen\'s Star')
grid(linestyle='dotted')
legend()
savefig('../fig/fig-fermielectron-masa-radio.pdf')
#show()



