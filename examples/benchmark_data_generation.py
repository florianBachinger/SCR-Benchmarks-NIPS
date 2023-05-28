from SCR_Benchmarks.suite import FEYNMAN_SRSD_HARD,HARD_TRAIN_TEST_SPLIT,HARD_NOISE_LEVELS,HARD_SAMPLE_SIZE
from SCR_Benchmarks.suite import SCRBenchmarkSuite

#creates one folder per equation under the parent folder
# each equation folder contains the info file as json
# and the data files for each configuration as csv
SCRBenchmarkSuite.create_hard_instances(target_folder = './data',
                                        Equations=FEYNMAN_SRSD_HARD,
                                        sample_size=HARD_SAMPLE_SIZE,
                                        train_test_splits=HARD_TRAIN_TEST_SPLIT,
                                        noise_levels=HARD_NOISE_LEVELS)

# or simply 
# SCRBenchmarkSuite.create_hard_instances() which uses the same values as default