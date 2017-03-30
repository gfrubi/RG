# coding: utf-8
from __future__ import division
from numpy import *
from matplotlib.pyplot import *
style.use('classic')


#Definiendo superficies importantes
def sp(ph):
    return m+sqrt(m**2-(a*cos(ph))**2)
def sm(ph):
    return m-sqrt(m**2-(a*cos(ph))**2)


r = linspace(0,40,10000)
a = 9.
m = 10.
#radios importantes
rp = m+sqrt(m**2-a**2)
rm = m-sqrt(m**2-a**2)
spe = sp(pi/2) # S+ en el ecuador
sme = sm(pi/2) # S- en el ecuador

#Dibujando las superficies
phi = linspace(0,2*pi,10000)

x_sp = sp(phi)*sin(phi)
y_sp = sp(phi)*cos(phi)
x_sm = sm(phi)*sin(phi)
y_sm = sm(phi)*cos(phi)
x_rp = rp*sin(phi)
y_rp = rp*cos(phi)
x_rm = rm*sin(phi)
y_rm = rm*cos(phi)

# superficies de redshift infinito
fig = figure()
plot(x_sp,y_sp,label='$S_+$',lw=2)
plot(x_sm,y_sm,label='$S_-$',lw=2)
plot([-a,a],[0,0],'o',color="green",label='anillo')
xlim(-25,25)
ylim(-25,25)
legend(loc=1,fontsize=14)
xticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$',r'$-s_{+\rm e}$','$-a$','$r_+$','$r_-$',r'$s_{+\rm e}$','$a$'], fontsize=15)
yticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$',r'$-s_{+\rm e}$','$-a$','$r_+$','$r_-$',r'$s_{+\rm e}$','$a$'], fontsize=15)
title(u'Superficies de redshift infinito, plano $(r\\sin\\theta,r\\cos\\theta)$')
grid()
axes().set_aspect('equal', 'datalim')
fig.savefig("../fig/fig-superficies-1.pdf")


# superficies de redshift infinito y horizontes

fig = figure()
plot(x_sp,y_sp,label='$S_+$',lw=2)
plot(x_sm,y_sm,label='$S_-$',lw=2)
plot(x_rp,y_rp,label='$r_+$',lw=2)
plot(x_rm,y_rm,label='$r_-$',lw=2)
plot([-a,a],[0,0],'o',color="green",label='anillo')
xlim(-25,25)
ylim(-25,25)
legend(loc=1,fontsize=14)
xticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$',r'$-s_{+\rm e}$','$-a$','$r_+$','$r_-$',r'$s_{+\rm e}$','$a$'], fontsize=15)
yticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$',r'$-s_{+\rm e}$','$-a$','$r_+$','$r_-$',r'$s_{+\rm e}$','$a$'], fontsize=15)
title(u'Superficies de interés, plano $(r\\sin\\theta,r\\cos\\theta)$')
grid()
axes().set_aspect('equal', 'datalim')
fig.savefig("../fig/fig-superficies-2.pdf")


# horizonte y ergosfera

fig=figure()
fill(x_sp,y_sp,label='Ergosfera')
fill(x_rp,y_rp,label='Interior del Horizonte',color='black')
xlim(-25,25)
ylim(-25,25)
legend(loc=1,fontsize=12)
xticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$',r'$-s_{+\rm e}$','$-a$','$r_+$','$r_-$',r'$s_{+\rm e}$','$a$'], fontsize=15)
yticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$',r'$-s_{+\rm e}$','$-a$','$r_+$','$r_-$',r'$s_{+\rm e}$','$a$'], fontsize=15)
grid()
title(u'Horizonte y Ergosfera, plano $(r\\sin\\theta,r\\cos\\theta)$')
axes().set_aspect('equal', 'datalim')
fig.savefig("../fig/fig-superficies-3.pdf")




