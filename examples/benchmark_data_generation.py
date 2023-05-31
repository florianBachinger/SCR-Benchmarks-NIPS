from SCRBenchmark import FEYNMAN_SRSD_HARD,HARD_NOISE_LEVELS,HARD_SAMPLE_SIZES
from SCRBenchmark import BenchmarkSuite

#creates one folder per equation under the parent folder
# each equation folder contains the info file as json
# and the data files for each configuration as csv
BenchmarkSuite.create_hard_instances(target_folder = './data',
                                        Equations=FEYNMAN_SRSD_HARD,
                                        sample_sizes=HARD_SAMPLE_SIZES,
                                        noise_levels=HARD_NOISE_LEVELS)

# or simply 
BenchmarkSuite.create_hard_instances() #which uses the same values as default