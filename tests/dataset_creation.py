import numpy as np

import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark

ICh6Eq20 = Benchmark(srsdf.FeynmanICh6Eq20)

(training, test) = ICh6Eq20.create_dataset(sample_size=1000,noise_level = 0,seed = 0, patience= 10)
(training_df, test_df) = ICh6Eq20.create_dataframe(sample_size=1000,noise_level = 0,seed = 0, patience= 10)

train_df_to_np = training_df.to_numpy()
test_df_to_np = test_df.to_numpy()

assert((training==train_df_to_np).all())
assert((test==test_df_to_np).all())
