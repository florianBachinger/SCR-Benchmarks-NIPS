import numpy as np

import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark

ICh6Eq20 = Benchmark(srsdf.FeynmanICh6Eq20)

np.random.seed(0)
(training, test) = ICh6Eq20.create_dataset(sample_size=1000, patience= 10, noise_level = 0)
np.random.seed(0)
(training_df, test_df) = ICh6Eq20.create_dataframe(sample_size=1000, patience= 10, noise_level = 0)

train_df_to_np = training_df.to_numpy()
test_df_to_np = test_df.to_numpy()

print((training==train_df_to_np).all())
print((test==test_df_to_np).all())