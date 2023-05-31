import numpy as np
import pandas as pd
import sympy as sympy

import seaborn as sns
import matplotlib.pyplot as plt

from SCRBenchmark.Constants import StringKeys as sk
import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark

from SCRBenchmark import FEYNMAN_SRSD_HARD,HARD_NOISE_LEVELS,HARD_SAMPLE_SIZES
from SCRBenchmark import BenchmarkSuite


import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=UserWarning)

ICh6Eq20 = Benchmark(srsdf.FeynmanICh6Eq20)
(training_df, test_df) = ICh6Eq20.create_dataframe(sample_size=1000, patience= 10, noise_level = 0, use_display_name = True)


fig, ax = plt.subplots(1,1, figsize=(5,3))
plt.subplots_adjust(left=0.1, bottom=0.15, right=0.98, top=0.99, wspace=0.1, hspace=0.1)

fig = sns.scatterplot(x='theta', y='sigma', data=training_df, c = 'b', s = 15,  marker='+', label = 'training')
fig = sns.scatterplot(ax = fig, x='theta', y='sigma', data=test_df, c = 'r', s = 10,alpha=0.08,  marker='x', label="validation")

fig.set_xlabel('$\\theta$')
fig.set_ylabel('$\sigma$')

plt.legend(facecolor='white', framealpha=1)
leg = plt.legend()
for lh in leg.legendHandles: 
    lh.set_alpha(1)
    lh.set_linewidth(1.5)
    lh.set_sizes([16.0])
plt.savefig('visualization/FeynmanICh6Eq20Sampling.png', dpi = 500)
plt.show()

