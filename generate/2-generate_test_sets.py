import json
import numpy as np
import sympy


import SCR_Benchmarks.SRSDFeynman as srsdf
import SCR_Benchmarks.Constants.StringKeys as sk
import SCR_Benchmarks.base as base
from SCR_Benchmarks import SCRBenchmark

sample_size = 100_000

for equation_name in srsdf.AllEquations:
  equation = srsdf.AllEquations[equation_name]()
  
  objectives=[obj.to_uniform_sampling() for obj in equation.sampling_objs]
  data=base.create_dataset_from_sampling_objectives(objectives, 
                                                      equation.sympy_eq, 
                                                      equation.eq_func, 
                                                      equation.check_if_valid, 
                                                      sample_size,
                                                      patience = sample_size)
  df=equation.to_dataframe(data)
  # df=equation.to_dataframe(data, use_display_names) consider adding support for readable names in datasets
  df.to_csv(f'./SCR_Benchmarks/Data/Test/{equation.get_eq_name()}.csv',index=False)
