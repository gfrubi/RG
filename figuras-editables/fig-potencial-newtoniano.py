from numpy import *
from matplotlib.pyplot import *

r=linspace(0.5,200,10000)
V=r**(-2.)-r**(-1.)
vmin=-1/4.
rc=1
rmin=2

figure(figsize=(8,5))
semilogx(r,V,linewidth=2)
ylim(-0.5,1)
xlim(0,200)
xticks([rc,rmin],[r"$r_{\rm c}$",r"$r_{\rm min}$"],fontsize=15)
yticks([0,vmin],['0',r'$V_{\rm ef,min}$'],fontsize=15)
vlines(rc,-0.5,0,color='black',linestyles='dotted')
hlines(0,0.5,200,color='black',linestyles='dotted')
hlines(vmin,0.5,rmin,color='black',linestyles='dotted')
vlines(rmin,-0.5,vmin,color='black',linestyles='dotted')
xlabel("Coordenada radial $r$",fontsize=15)
ylabel(r"Potencial Efectivo $V_{\rm ef}(r)$",fontsize=15)
savefig("fig-potencial-newtoniano.pdf")


