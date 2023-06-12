import numpy as np
import shutil
import filecmp
import os
import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import BenchmarkSuite, FEYNMAN_SRSD_HARD, HARD_NOISE_LEVELS,HARD_SAMPLE_SIZES

folder1 = './tests/Run1'
folder2 = './tests/Run2'
try:
    shutil.rmtree(folder1)
    shutil.rmtree(folder2)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))

BenchmarkSuite.create_hard_instances(target_folder=folder1
                                     , Equations=FEYNMAN_SRSD_HARD
                                     , sample_sizes= HARD_SAMPLE_SIZES
                                     , noise_levels=HARD_NOISE_LEVELS
                                     , repetitions= 2 )

BenchmarkSuite.create_hard_instances(target_folder=folder2
                                     , Equations=FEYNMAN_SRSD_HARD
                                     , sample_sizes= HARD_SAMPLE_SIZES
                                     , noise_levels=HARD_NOISE_LEVELS
                                     , repetitions= 2 )

rootdir = 'C:/Users/sid/Desktop/test'

for subdir, dirs, files in os.walk(folder1):
  for file in files:
    folder2Subdir = subdir.replace(folder1,folder2)
    assert filecmp.cmp(os.path.join(subdir, file), 
                       os.path.join(folder2Subdir, file),
                       shallow=False)