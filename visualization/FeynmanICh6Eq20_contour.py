
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark

import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=UserWarning)

fig, ax = plt.subplots(1,2, figsize=(5,2))

ICh6Eq20 = Benchmark(srsdf.FeynmanICh6Eq20)

xlist = np.linspace(-10,10, 100) # the valid range of theta for ICh6Eq20 (except for [-0.1,0.1])
ylist = np.linspace(0.1, 10, 100) # the valid range of sigma for ICh6Eq20
X, Y = np.meshgrid(xlist, ylist)

grid_z_pos = ICh6Eq20.equation.calculate((X,Y))

norm = Normalize( vmin=-np.max(grid_z_pos), vmax=np.max(grid_z_pos))
cmap = cm.get_cmap('coolwarm')

ax[0].contourf(X, Y, grid_z_pos, cmap= cmap , norm= norm)
ax[0].set_xlabel('$\\theta$')
ax[0].set_ylabel('$\sigma$')

ax[1].contourf(X, Y, grid_z_pos, cmap= cmap , norm= norm)
ax[1].set_xlabel('$\\theta$')
ax[1].set_xlim([-1,1])
ax[1].set_ylim([0.1,1.5])



plt.subplots_adjust(left=0.1, bottom=0.22, right=0.87, top=0.97, wspace=0.19, hspace=0.1)
cbar_ax = fig.add_axes([.89, .22, .025, .63])
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap),cax = cbar_ax)
plt.savefig('visualization/FeynmanICh6Eq20Contour.png', dpi = 500)
plt.show()