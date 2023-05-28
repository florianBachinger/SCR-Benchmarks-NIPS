import json
import numpy as np
import sympy


import SCR_Benchmarks.SRSDFeynman as srsdf
import SCR_Benchmarks.Constants.StringKeys as sk
import SCR_Benchmarks.base as base
from SCR_Benchmarks import SCRBenchmark

CONSTRAINT_SAMPLING_SIZE = 1_000_000

for equation_name in srsdf.AllEquations:
  scr = SCRBenchmark(srsdf.AllEquations[equation_name])

  constraints = [c for c in scr.constraints if c[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]!=sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT]
  if(len(constraints) == 0):
      raise Warning( f"equation {scr.equation._eq_name} has to have constraints to be checked. all checks will return true.")
  datasets = {}
  for constraint in constraints:
      data = np.random.uniform(
           [ low for (name,low,high) in constraint[sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY].values()],
           [ high for (name,low,high) in constraint[sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY].values()],
          (CONSTRAINT_SAMPLING_SIZE,scr.equation.get_var_count())
        )
      # df.to_csv(f'./SCR_Benchmarks/Data/ConstraintChecking/{equation}.csv', index =False)
