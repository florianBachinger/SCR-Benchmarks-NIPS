import numpy as np
import pandas as pd
import sympy as sympy
from SCR_Benchmarks.Constants import StringKeys as sk
from SCR_Benchmarks.base import get_constraint_descriptor
from SCR_Benchmarks.base import create_dataset_from_sampling_objectives
import SCR_Benchmarks.SRSDFeynman as srsdf
import SCR_Benchmarks.AIFeynman as aif
import copy 
f = srsdf.FeynmanICh6Eq20()

sample_size = 1_000_000
f_prime = [(sympy.Derivative(f.sympy_eq, var).doit(),var, var_display_name) for (var,var_display_name) in list(zip(f.x, f.get_var_names()))]

constraints = []
xs = f.create_input_dataset(sample_size)

split_objectives = []
objectives= list(zip(f.x, f.sampling_objs))

split_objectives.append(objectives)

for (var_name,objective ) in objectives:

  if(objective.uses_positive and objective.uses_negative):
    positive_copy = copy.deepcopy(split_objectives)
    negative_copy = copy.deepcopy(split_objectives)
    
    for objs in positive_copy:
      for (var, obj) in objs:
        if(var == var_name):
          obj.uses_negative = False
    for objs in negative_copy:
      for (var, obj) in objs:
        if(var == var_name):
          obj.uses_positive = False
    split_objectives = positive_copy + negative_copy


for split_objective in split_objectives:
  for (derivative, var_name, var_display_name) in f_prime:
    sampling_objectives = [obj for (var, obj) in split_objective]
    xs = f.get_inputs_from_dataset(
            create_dataset_from_sampling_objectives(sampling_objectives, 
                                                    f.sympy_eq, 
                                                    f.eq_func, 
                                                    f.check_if_valid, 
                                                    sample_size)
          )

    sampling_space = { var.name: obj.get_value_range() for (var, obj) in split_objective}

    descriptor =  get_constraint_descriptor(f, derivative,xs)
    if(descriptor != sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT):
      constraints.append({sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY:str(var_name),
        sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY:var_display_name,
        sk.EQUATION_CONSTRAINTS_ORDER_DERIVATIVE_KEY:1,
        sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY: descriptor,
        sk.EQUATION_CONSTRAINTS_DERIVATIVE_KEY: str(derivative),
        sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY: str(sampling_space)  })

for constraint in constraints:
  print (constraint)