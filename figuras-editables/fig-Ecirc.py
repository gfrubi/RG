from matplotlib.pyplot import *
from numpy import *
style.use('classic')

ra = linspace(1,10,10000)
aa = 0.6

rap = 1+sqrt(1-aa**2) 

Ep = (ra**2-2*ra+aa*sqrt(ra))/(ra*sqrt(ra**2-3*ra+2*aa*sqrt(ra)))
Em = (ra**2-2*ra-aa*sqrt(ra))/(ra*sqrt(ra**2-3*ra-2*aa*sqrt(ra)))

up = sort((roots([1,0,-3,2*aa])))
upp = up[where(up>0)]
rfap = upp[-1]**2
um = sort((roots([1,0,-3,-2*aa])))
ump = um[where(um>0)]
rfam = ump[-1]**2

rllap = 2 - aa + 2*sqrt(1-aa)
rllam = 2 + aa + 2*sqrt(1+aa)

plot(ra,Ep, label='co-rotante', lw=2)
plot(ra,Em, label='contra-rotante', lw=2)
vlines([rap,2,rfap,rfam,rllap,rllam],0,3, linestyle='dotted')
hlines(1,0,10, linestyle='dotted')
xticks([rap,2,rfap,rfam,rllap,rllam], [r'$r_+$',r'$2m$', r'$r^+_{\rm f}$', r'$r_{\rm f}^-$', r'$r_{\rm ll}^+$', r'$r_{\rm ll}^-$'], fontsize=10, rotation=45)

ylabel(r'$E/m_0c^2$', fontsize=15)
xlim(0,6)
ylim(0.,3)
legend()
savefig('../fig/fig-Ecirc.pdf')
