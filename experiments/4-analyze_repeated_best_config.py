from SCRBenchmark import Benchmark
from SCRBenchmark.SRSDFeynman import FeynmanICh6Eq20a
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
import numpy as np

summary = pd.read_csv('./experiments/repeated_best_config_results/summary.csv')

summary = summary[ ((summary['EquationName'] == 'FeynmanICh6Eq20') |
                  (summary['EquationName'] == 'FeynmanICh6Eq20b') |
                  (summary['EquationName'] == 'FeynmanICh6Eq20a')) ]

summary['SampleSize'] = [ filename.split('sample_size')[1].split('_')[0] for filename in summary['DataSourceFile']]
summary['NoiseLevel'] = [ filename.split('noise_level')[1].split('_')[0] for filename in summary['DataSourceFile']]

performance = summary[['EquationName','Runtime']]
performance = performance.groupby('EquationName').mean()
print(f"runtime average")
print(performance)

print(summary.groupby('EquationName').count())


sns.set_theme(style="ticks", palette="husl")
f, ax = plt.subplots(2,5, figsize=(10, 4), sharex=True, sharey=True)
plt.subplots_adjust(left=0.11, bottom=0.1, right=0.98, top=0.90, wspace=0.1, hspace=0.1)


print("data for")
print(np.unique(summary['EquationName']))
print(np.unique(summary['SampleSize']))
print(np.unique(summary['NoiseLevel']))

row = 0
max_row_idx = len(np.unique(summary['SampleSize']))-1
unique_euqations = np.unique(summary['EquationName'])

for sampleSize in np.unique(summary['SampleSize']):
  col = 0
  for noiseLevel in np.unique(summary['NoiseLevel']):
    df = summary[ ((summary['SampleSize'] == sampleSize) |
                      (summary['NoiseLevel'] == noiseLevel)) ]
    bx = sns.boxplot(y="RMSE_Test",
          x="EquationName", 
          hue = "EquationName",
          data=df,
          ax = ax[row,col] )
    
    bx.set(xticklabels=[])

    # ax[row,col].set_yscale("log")

    if(row == max_row_idx):
      ax[row,col].set_xlabel(f'noise level = {noiseLevel}')
    else:
      ax[row,col].set_xlabel(f'')
    if(col == 0):
      ax[row,col].set_ylabel(f'sample_size = {sampleSize}\nRMSE validation')
    else:
      ax[row,col].set_ylabel(f'')

    col = col+1

  row = row+1

lines_labels = [ax.get_legend_handles_labels() for ax in f.axes]
lines, labels = [sum(total, []) for total in zip(*lines_labels)]
lines = lines[:len(unique_euqations)]
labels = labels[:len(unique_euqations)]
for ax in f.axes:
  ax.get_legend().remove()

f.legend(lines,labels,
            loc='upper center', ncol=3)
plt.savefig('./experiments/summary.png',dpi = 500)
plt.show()

# summary = summary[['EquationName','Degree','Lambda','Alpha','MaxInteractions','RMSE_Training','RMSE_Test','RMSE_Full']]
# configuration = summary.groupby(['EquationName','Degree','Lambda','Alpha','MaxInteractions']).mean()

# configuration = configuration.reset_index()
# print(configuration.groupby(['EquationName']).min())

# best_configuration = configuration.iloc[configuration.groupby(['EquationName']).idxmin()['RMSE_Test'].values]
# print(best_configuration)
# best_configuration = best_configuration[['EquationName','Degree','Lambda','Alpha','MaxInteractions']]
# best_configuration.to_csv('./experiments/best_configruations.csv', index = False)

