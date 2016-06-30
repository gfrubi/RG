from mpl_toolkits.mplot3d import axes3d
from matplotlib.pyplot import * # requiere version 1.4 !!
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from numpy import *

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

from scipy.stats import cosine


#theta,phi=meshgrid(linspace(0,pi,20),linspace(0,2*pi,30))

theta,phi=meshgrid(arccos(linspace(1,-1,20)),linspace(0,2*pi,30))

x=sin(theta)*cos(phi)
y=sin(theta)*sin(phi)
z=cos(theta)

thetas,phis=meshgrid(linspace(0,pi,100),linspace(0,2*pi,100))
xs=sin(thetas)*cos(phis)
ys=sin(thetas)*sin(phis)
zs=cos(thetas)

def decorado():
    ax.set_axis_off()
    a = Arrow3D([0, 1.3], [0,0], [0,0], mutation_scale=15, lw=2, arrowstyle="->", color="k")
    ax.add_artist(a)
    a = Arrow3D([0, 0], [0,1.3], [0,0], mutation_scale=15, lw=2, arrowstyle="->", color="k")
    ax.add_artist(a)
    a = Arrow3D([0, 0], [0,0], [0,1.3], mutation_scale=15, lw=2, arrowstyle="->", color="k")
    ax.add_artist(a)
    ax.text(1.35,0,0,'$x$',size=20)
    ax.text(0,1.35,0,'$y$',size=20)
    ax.text(0,0,1.35,'$z$',size=20)

f1 = figure(figsize=(10,10))
ax = f1.gca(projection='3d')

u = 0
v = -z
w = y

ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, color='y',linewidth=0)
ax.quiver(x, y, z, u, v, w,length=.09,arrow_length_ratio=0.5)

decorado()


# In[38]:

f2 = figure(figsize=(10,10))
ax = f2.gca(projection='3d')

u = z
v = 0
w = -x

ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, color='y',linewidth=0)
ax.quiver(x, y, z, u, v, w,length=.09,arrow_length_ratio=0.5)
decorado()


# In[39]:

f3 = figure(figsize=(10,10))
ax = f3.gca(projection='3d')

u = -y
v = x
w = 0

ax.plot_surface(xs, ys, zs, rstride=1, cstride=1, color='y',linewidth=0)
ax.quiver(x, y, z, u, v, w,length=.09,arrow_length_ratio=0.5)
decorado()


# In[44]:

f1.savefig('KS2x.svg')
f2.savefig('KS2y.svg')
f3.savefig('KS2z.svg')

