from SCR_Benchmarks.suite import FEYNMAN_SRSD_HARD,HARD_TRAIN_TEST_SPLIT,HARD_NOISE_LEVELS,HARD_SAMPLE_SIZE
from SCR_Benchmarks.suite import SCRBenchmarkSuite
from SCR_Benchmarks.scr_benchmark import SCRBenchmark
from SCR_Benchmarks.SRSDFeynman import FeynmanICh6Eq20a
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import pandas as pd

benchmark = SCRBenchmark(FeynmanICh6Eq20a)

# checking all the csv files in the 
# specified path
summary = pd.read_csv('./results/summary.csv')
summary = summary[summary['EquationName'] == 'FeynmanICh6Eq20a']
summary = summary.sort_values(['RMSE_Test'], ascending=True)
summary = summary.head(3)
for (index,row) in summary.iterrows():
    data = pd.read_csv(row['DataTargetFile'])
    data = data.sort_values(['x0'], ascending=True)
    training = data[data['split'] == 'training']
    test = data[data['split'] == 'test']
    plt.scatter(training['x0'], training['f'], color = 'blue', label= 'target_training', s=4)
    plt.scatter(test['x0'], test['f'], color = 'green', label= 'target_test', s=4)
    plt.scatter(data['x0'], data['Predicted'], color = 'red', label= 'prediction', s=4, alpha=0.5)

    eq = eval(f"lambda x0: {row['EquationString'].replace(',','.')}")
    y = eq(data['x0'])
    plt.scatter(data['x0'], y, color = 'purple', label= 'prediction', s=4, alpha=0.5)


    plt.show()
    plt.savefig(f'./results/visualization/FeynmanICh6Eq20a/{row["RMSE_Test"]}_{index}.png')
    plt.clf()
