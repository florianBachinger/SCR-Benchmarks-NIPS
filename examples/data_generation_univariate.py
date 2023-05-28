import numpy as np
import pandas as pd
import sympy as sympy

import seaborn as sns
import matplotlib.pyplot as plt

from SCR_Benchmarks.Constants import StringKeys as sk
import SCR_Benchmarks.SRSDFeynman as srsdf
from SCR_Benchmarks import SCRBenchmark

ICh6Eq20 = SCRBenchmark(srsdf.FeynmanICh6Eq20a)
ICh6Eq20 = SCRBenchmark(srsdf.FeynmanICh6Eq20a)

np.random.seed(0)
(training, test) = ICh6Eq20.create_dataset(sample_size=1000, patience= 10, train_test_split = 0.8)
np.random.seed(0)
(training_df, test_df) = ICh6Eq20.create_dataframe(sample_size=1000, patience= 10,  train_test_split = 0.8)

train_df_to_np = training_df.to_numpy()

print((training==train_df_to_np).all())