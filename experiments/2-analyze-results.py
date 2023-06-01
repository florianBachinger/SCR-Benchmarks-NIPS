from SCRBenchmark import Benchmark
from SCRBenchmark.SRSDFeynman import FeynmanICh6Eq20a
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd
import numpy as np

summary = pd.read_csv('./experiments/gridsearch_results/summary.csv')

summary = summary[ ((summary['EquationName'] == 'FeynmanICh6Eq20') |
                  (summary['EquationName'] == 'FeynmanICh6Eq20b') |
                  (summary['EquationName'] == 'FeynmanICh6Eq20a')) ]

summary = summary[['EquationName','Degree','Lambda','Alpha','MaxInteractions','RMSE_Training','RMSE_Test','RMSE_Full']]
configuration = summary.groupby(['EquationName','Degree','Lambda','Alpha','MaxInteractions']).mean()

configuration = configuration.reset_index()
print(configuration.groupby(['EquationName']).min())

best_configuration = configuration.iloc[configuration.groupby(['EquationName']).idxmin()['RMSE_Test'].values]
print(best_configuration)
best_configuration = best_configuration[['EquationName','Degree','Lambda','Alpha','MaxInteractions']]
best_configuration.to_csv('./experiments/best_configurations.csv', index = False)

