import numpy as np
import pandas as pd
import sympy as sympy
from SCR_Benchmarks.Constants import StringKeys as sk
import SCR_Benchmarks.SRSDFeynman as srsdf
from SCR_Benchmarks.constraints import SCRBenchmark
import copy

ICh6Eq20 = SCRBenchmark(srsdf.FeynmanICh6Eq20)

for constraint in ICh6Eq20.determine_constraints(): 
  print (f'> {constraint}')