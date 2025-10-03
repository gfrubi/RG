# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')


#Definiendo superficies importantes
def sp(ph):
    return m+np.sqrt(m**2-(a*np.cos(ph))**2)
def sm(ph):
    return m-np.sqrt(m**2-(a*np.cos(ph))**2)


r = np.linspace(0,40,10000)
a = 9
m = 10
#radios importantes
rp = m+np.sqrt(m**2-a**2)
rm = m-np.sqrt(m**2-a**2)
spe = sp(np.pi/2) # S+ en el ecuador
sme = sm(np.pi/2) # S- en el ecuador

#Dibujando las superficies
phi = np.linspace(0,2*np.pi,10000)

x_sp = sp(phi)*np.sin(phi)
y_sp = sp(phi)*np.cos(phi)
x_sm = sm(phi)*np.sin(phi)
y_sm = sm(phi)*np.cos(phi)
x_rp = rp*np.sin(phi)
y_rp = rp*np.cos(phi)
x_rm = rm*np.sin(phi)
y_rm = rm*np.cos(phi)

# superficies de redshift infinito
plt.figure()
plt.plot(x_sp,y_sp,label='$S_+$',lw=2)
plt.plot(x_sm,y_sm,label='$S_-$',lw=2)
#plt.plot([-a,a],[0,0],'o',color="green",label='anillo')
plt.xlim(-25,25)
plt.ylim(-25,25)
plt.legend(loc=1)
plt.xticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$','$-r_{S+}$','$-a$','$r_+$','$r_-$','$r_{S+}$','$a$'], fontsize=15)
plt.yticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$','$-r_{S+}$','$-a$','$r_+$','$r_-$','$r_{S+}$','$a$'], fontsize=15)
plt.title('Superficies de redshift infinito, plano $(r\\sin\\theta,r\\cos\\theta)$')
plt.grid(True)
plt.axis('equal')
plt.savefig("../fig/fig-superficies-1.pdf")


# superficies de redshift infinito y horizontes

plt.figure()
plt.plot(x_sp,y_sp,label='$S_+$',lw=2)
plt.plot(x_sm,y_sm,label='$S_-$',lw=2)
plt.plot(x_rp,y_rp,label='$r_+$',lw=2)
plt.plot(x_rm,y_rm,label='$r_-$',lw=2)
#plt.plot([-a,a],[0,0],'o',color="green",label='anillo')
plt.xlim(-25,25)
plt.ylim(-25,25)
plt.legend(loc=1)
plt.xticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$','$-r_{S+}$','$-a$','$r_+$','$r_-$','$r_{S+}$','$a$'], fontsize=15)
plt.yticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$','$-r_{S+}$','$-a$','$r_+$','$r_-$','$r_{S+}$','$a$'], fontsize=15)
plt.title(u'Superficies de interés, plano $(r\\sin\\theta,r\\cos\\theta)$')
plt.grid(True)
plt.axis('equal')
plt.savefig("../fig/fig-superficies-2.pdf")


# horizonte y ergosfera

plt.figure()
plt.fill(x_sp,y_sp,label='Ergosfera')
plt.fill(x_rp,y_rp,label='Interior del Horizonte',color='black')
plt.xlim(-25,25)
plt.ylim(-25,25)
plt.legend(loc=1)
plt.xticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$','$-r_{S+}$','$-a$','$r_+$','$r_-$','$r_{S+}$','$a$'], fontsize=15)
plt.yticks([0,-rp,-rm,-spe,-a,rp,rm,spe,a],[0,'$-r_+$','$-r_-$','$-r_{S+}$','$-a$','$r_+$','$r_-$','$r_{S+}$','$a$'], fontsize=15)
plt.grid(False)
plt.title('Horizonte y Ergosfera, plano $(r\\sin\\theta,r\\cos\\theta)$')
plt.axis('equal')
plt.savefig("../fig/fig-superficies-3.pdf")




