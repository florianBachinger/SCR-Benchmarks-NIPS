from SCR_Benchmarks.scr_benchmark import SCRBenchmark
from SCR_Benchmarks.SRSDFeynman import FeynmanICh6Eq20a
import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np

benchmark = SCRBenchmark(FeynmanICh6Eq20a)

# checking all the csv files in the 
# specified path
folder= f'./scpr_experiments/results/visualization/FeynmanICh6Eq20a/'
if not os.path.exists(folder):
          os.makedirs(folder)

summary = pd.read_csv('./scpr_experiments/results/summary.csv')
summary = summary[summary['EquationName'] == 'FeynmanICh6Eq20a']
summary = summary[summary['DataSourceFile'] == 'D:\\src\\NIPS-Benchmarks\\scpr_experiments\\data\\FeynmanICh6Eq20a\\FeynmanICh6Eq20a_sample_size100_noise_level0.csv' ]
print(f"Degree {np.unique(summary['Degree'])}")
summary = summary.sort_values(['RMSE_Test'], ascending=True)
summary = summary.head(10)
summary.to_csv("./scpr_experiments/results/FeynmanICh6Eq20a_summary.csv")
print(summary)
for (index,row) in summary.iterrows():
    data = pd.read_csv(row['DataSourceFile'])
    data = data.sort_values(['x0'], ascending=True)
    training = data[data['split'] == 'training']
    test = data[data['split'] == 'test']
    plt.scatter(training['x0'], training['f'], color = 'blue', label= 'target_training', s=4)
    plt.scatter(test['x0'], test['f'], color = 'green', label= 'target_test', s=4)

    eq = eval(f"lambda x0: {row['EquationString'].replace(',','.')}")
    y = eq(data['x0'])
    plt.scatter(data['x0'], y, color = 'purple', label= 'prediction', s=4, alpha=0.5)


    plt.savefig(f'{folder}{row["RMSE_Test"]}_{index}.png')
    plt.clf()
    plt.close()
