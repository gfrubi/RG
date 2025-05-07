import numpy as np
import matplotlib.pyplot as plt
plt.style.use('bmh')

# lista de puntos iniciales r0 > 2 (en unidades de m)
r0s_in = range(1,20,2)
r0s_out = [2.01, 2.1,2.8,4,6,8,10]
r0s_out2 = [0.5,0.9,1.3,1.6,1.8,1.9,1.99]

plt.figure(figsize=(7, 6))

for r0 in r0s_in:
    # — geodésica entrante (línea negra): t = r0 - r
    r_black = np.linspace(0, r0, 500)
    t_black = r0 - r_black
    plt.plot(r_black, t_black, color='black', lw=2)

for r0 in r0s_out:
    # — geodésica saliente (curva roja): t = r - r0 + 4 ln((r-2)/(r0-2))
    r_red = np.linspace(r0, 10, 500)
    t_red = r_red - r0 + 4 * np.log(np.abs((r_red - 2) / (r0 - 2)))
    plt.plot(r_red, t_red, color='red', lw=2)

for r0 in r0s_out2:
    # — geodésica saliente (curva roja): t = r - r0 + 4 ln((r-2)/(r0-2))
    r_red = np.linspace(0,r0, 500)
    t_red = r_red - r0 + 4 * np.log(np.abs((r_red - 2) / (r0 - 2)))
    plt.plot(r_red, t_red, color='red', lw=2)

# etiquetas y título
plt.xlabel('$r/m$', fontsize=15)
plt.ylabel('$(c/m)\,\\bar{t}$', fontsize=15)
plt.title('Curvas radiales nulas')

# límites y malla de ticks
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(0, 11, 2))

# extras
plt.vlines(2,0,10, color='red')
plt.annotate('entrantes',
            xy=(4, 3), xytext=(4.5, 5),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.7))
plt.annotate('salientes', 
            xy=(8, 8.3), xytext=(8.2, 7),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.7))

plt.grid(False)
plt.savefig('fig-nullrays-cEF.pdf')
#plt.show()
