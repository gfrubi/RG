from matplotlib.pyplot import *
from numpy import *
style.use('classic')

ra = linspace(1,10,10000)
aa = 0.3

Ep = (ra**2-2*ra+aa*sqrt(ra))/(ra*sqrt(ra**2-3*ra+2*aa*sqrt(ra)))
Em = (ra**2-2*ra-aa*sqrt(ra))/(ra*sqrt(ra**2-3*ra-2*aa*sqrt(ra)))

up = sort((roots([1,0,-3,2*aa])))
upp = up[where(up>0)]
rfap = upp[-1]**2
um = sort((roots([1,0,-3,-2*aa])))
ump = um[where(um>0)]
rfam = ump[-1]**2

plot(ra,Ep, label='co-rotante', lw=2)
plot(ra,Em, label='contra-rotante', lw=2)
vlines(rfap,-20,20, linestyle='dashed')
vlines(rfam,-20,20, linestyle='dashed')
xticks([1,2,rfap,rfam], [r'$m$',r'$2m$', r'$r_{\rm f+}$', r'$r_{\rm f-}$'])
ylabel(r'$E/m_0c^2$')
grid()
xlim(0,10)
ylim(0.,3)
legend()
savefig('../fig/fig-Ecirc.pdf')
