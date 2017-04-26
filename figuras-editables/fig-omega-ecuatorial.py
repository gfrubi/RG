from numpy import *
from matplotlib.pyplot import *
style.use('classic')

#Definiendo superficies importantes
def sp(ph):
    return m+sqrt(m**2-(a*cos(ph))**2)
def sm(ph):
    return m-sqrt(m**2-(a*cos(ph))**2)

#Calculo de frecuencias
def g_00(r,th):
    return (r**2-2.*m*r+a**2*(cos(th))**2)/(r**2+a**2*(cos(th))**2)
def g_0ph(r,th):
    return ((2.*m*r*a*(sin(th))**2)/(r**2+a**2*(cos(th))**2))
def g_phph(r,th):
    return -(((sin(th))**2)/(r**2+a**2*(cos(th))**2))*(2.*m*r*a**2*(sin(th))**2+(r**2+a**2)*(r**2+a**2*(cos(th))**2))
def omegap(r,th):
    return (-g_0ph(r,th)-sqrt((g_0ph(r,th))**2-g_phph(r,th)*g_00(r,th)))/(g_phph(r,th))
def omegam(r,th):
    return (-g_0ph(r,th)+sqrt((g_0ph(r,th))**2-g_phph(r,th)*g_00(r,th)))/(g_phph(r,th))

# parametros
a = 9.
m = 10.

#radios importantes
rp = m+sqrt(m**2-a**2)
rm = m-sqrt(m**2-a**2)
spe = sp(pi/2) # S+ en el ecuador
sme = sm(pi/2) # S- en el ecuador


r = linspace(rp,50,10000)

#Calculo de frecuencias en el ecuador
omegape = omegap(r,pi/2)
omegame = omegam(r,pi/2)


#Grafico de frecuencias en el ecuador
figure(figsize=(7,5))
plot(r,omegape,color="red",label=r'$\Omega_+$', lw=2)
plot(r,omegame,color="#1155dd",label=r'$\Omega_-$',lw=2)
vlines(rp,-1,1, linestyles='dotted')
vlines(rm,-1,1, linestyles='dotted')
vlines(spe,-1,1, linestyles='dotted')
vlines(sme,-1,1, linestyles='dotted')
xlim(0,50)
ylim(-0.1,0.2)
xlabel('$r$', fontsize=15)
ylabel('$\Omega/c$', fontsize=15)
xticks([0,rp,rm,spe],['0','$r_+$','$r_-$',r'$s_{+\rm e}$'])
title('Velocidades angulares (ecuatoriales)')
legend(loc=1)
grid()
#show() 
savefig("../fig/fig-omega-ecuatorial.pdf")
