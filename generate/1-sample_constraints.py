import json
import numpy as np
import sympy


import SCR_Benchmarks.SRSDFeynman as srsdf
import SCR_Benchmarks.Constants.StringKeys as sk
import SCR_Benchmarks.base as base
from SCR_Benchmarks import SCRBenchmark

numpyShort = 'np'

# declaring a class
class obj:
    # constructor
    def __init__(self, dict1):
        self.__dict__.update(dict1)
   
def dict2obj(dict1):
    # using json.loads method and passing json.dumps
    # method and custom object hook as arguments
    return json.loads(json.dumps(dict1), object_hook=obj)

dict = []

i = 0

def CalculateEquation(equation_class, text_file):
  print(f"{equation_class}")
  
  scr = SCRBenchmark(equation_class, initialize_datasets_on_creation=False)

  constraints = scr.determine_constraints()

  text_file.write(str( {sk.EQUATION_EQUATION_NAME_KEY:scr.equation.get_eq_name(),
        sk.EQUATION_CONSTRAINTS_CONSTRAINTS_KEY: constraints
          }))
  text_file.write(',')


with open("SCR_Benchmarks/Info/feynman_srsdf_constraint_info.json", "w") as text_file:
  text_file.write('SRSD_EQUATION_CONSTRAINTS = [')
  #iterate over all equations
  for dictEntry in srsdf.AllEquations:
    CalculateEquation(srsdf.AllEquations[dictEntry], text_file)
  text_file.write(']')