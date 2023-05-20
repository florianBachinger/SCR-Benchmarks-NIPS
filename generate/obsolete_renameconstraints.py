import json
import numpy as np
import sympy


import SCR_Benchmarks.SRSDFeynman as srsdf
import SCR_Benchmarks.Constants.StringKeys as sk
import SCR_Benchmarks.base as base
from SCR_Benchmarks import SCRBenchmark
from SCR_Benchmarks.Info.feynman_srsdf_constraint_info import SRSD_EQUATION_CONSTRAINTS


with open("SCR_Benchmarks/Info/feynman_srsdf_constraint_info.json", "w") as text_file:
  text_file.write('SRSD_EQUATION_CONSTRAINTS = [')
  #iterate over all equations
  for constraint_info in SRSD_EQUATION_CONSTRAINTS:
    print(constraint_info)
    i = 1
    for constraint in constraint_info['Constraints']:
      constraint['id'] = i
      i = i+1
    
    text_file.write(str(constraint_info))
    text_file.write(',')

  text_file.write(']')