
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import seaborn as sns

import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark

import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=UserWarning)

fig, ax = plt.subplots(1,3, figsize=(10,3), sharex=False, sharey=False)
plt.subplots_adjust(left=0.052, bottom=0.15, right=0.92, top=0.98, wspace=0.15, hspace=0.1)


ICh6Eq20 = Benchmark(srsdf.FeynmanICh6Eq20)
(training_df, test_df) = ICh6Eq20.create_dataframe(sample_size=1000, patience= 10, noise_level = 0, use_display_name = True)



sns.scatterplot(ax = ax[0],x='theta', y='sigma', data=training_df, c = 'b', s = 15,  marker='+', label = 'training')
sns.scatterplot(ax = ax[0], x='theta', y='sigma', data=test_df, c = 'r', s = 10,alpha=0.08,  marker='x', label="validation")

ax[0].set_xlabel('$\\theta$')
ax[0].set_ylabel('$\sigma$')
ax[0].set_xlim([-10,10])
ax[0].set_ylim([0,10])

leg = ax[0].legend(facecolor='white', framealpha=1, loc='upper left', bbox_to_anchor=(0.55, 0.99))
# leg = plt.legend(loc='lower right', bbox_to_anchor=(0.1, 0.1))
for lh in leg.legendHandles: 
    lh.set_alpha(1)
    lh.set_linewidth(1.5)
    lh.set_sizes([16.0])


xlist = np.linspace(-10,10, 100) # the valid range of theta for ICh6Eq20 (except for [-0.1,0.1])
ylist = np.linspace(0.1, 10, 100) # the valid range of sigma for ICh6Eq20
X, Y = np.meshgrid(xlist, ylist)

grid_z_pos = ICh6Eq20.equation.calculate((X,Y))

norm = Normalize( vmin=-np.max(grid_z_pos), vmax=np.max(grid_z_pos))
cmap = cm.get_cmap('coolwarm')

ax[1].contourf(X, Y, grid_z_pos, cmap= cmap , norm= norm)
ax[1].set_xlabel('$\\theta$')
ax[1].set_xlim([-10,10])
ax[1].set_ylim([0,10])
# ax[1].set_ylabel('$\sigma$')

ax[2].contourf(X, Y, grid_z_pos, cmap= cmap , norm= norm)
ax[2].set_xlabel('$\\theta$')
ax[2].set_xlim([-1,1])
ax[2].set_ylim([0.1,1.5])



cbar_ax = fig.add_axes([.948, .22, .015, .63])
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap),cax = cbar_ax)

plt.savefig('visualization/FeynmanICh6Eq20Combined.png', dpi = 500)
plt.savefig('visualization/FeynmanICh6Eq20Combined.pdf', dpi = 500)
plt.show()