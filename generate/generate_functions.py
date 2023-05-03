import pandas as pd
import inspect

lines = []
numpyShort = 'np'
sympyShort = 'sympy'

# read and prepare standard equations 
feynmanEquations = pd.read_csv('generate/src/FeynmanEquations.csv')
# filter to exclude the empty lines in FeynmanEquations.csv
feynmanEquations = feynmanEquations[feynmanEquations['Number']>=1]
feynmanEquations['EquationName'] = [f'Feynman{int(number)}' for number in feynmanEquations['Number']]
feynmanEquations['DescriptiveName'] = [f'Feynman{int(number)}, Lecture {filename}' for number,filename in zip(feynmanEquations['Number'],feynmanEquations['Filename'])]

# read and prepare bonus equations 
bonusEquasions = pd.read_csv('generate/src/BonusEquations.csv')
# filter to exclude the empty lines in FeynmanEquations.csv
bonusEquasions = bonusEquasions[bonusEquasions['Number']>=1]
bonusEquasions['EquationName'] = [f'Bonus{int(number)}' for number in bonusEquasions['Number']]
bonusEquasions['DescriptiveName'] = [f'Bonus{number}, {name}' for name,number in zip(bonusEquasions['Name'], bonusEquasions['Number'])]

#merge both into one dataframe
equations = pd.concat([feynmanEquations,bonusEquasions],ignore_index=True)

# add imports at file-beginning
lines.append("""
\"\"\"
  Code structure and idea adapted from https://github.com/omron-sinicx/srsd-benchmark at April 2023 under MIT licence

  Equations and benchmark set, credited to 
  @article{udrescu2020ai,
    title={AI Feynman: A physics-inspired method for symbolic regression},
    author={Udrescu, Silviu-Marian and Tegmark, Max},
    journal={Science Advances},
    volume={6},
    number={16},
    pages={eaay2631},
    year={2020},
    publisher={American Association for the Advancement of Science}
  }
  Equations and variable ranges copied from https://space.mit.edu/home/tegmark/aifeynman.html 
\"\"\"
from collections import OrderedDict

import numpy as np
import sympy

from SCR_Benchmarks.base import KnownEquation
from SCR_Benchmarks.registry import register_eq_class
from SCR_Benchmarks.sampling import DefaultSampling, IntegerSampling, SimpleSampling

FEYNMAN_EQUATION_CLASS_DICT = OrderedDict()

def register_feynman_eq_class(cls):
    register_eq_class(cls)
    FEYNMAN_EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls

""")


for index, row in equations.iterrows():
  #iterate over the CSV rows
  no_of_variables = int(row['# variables'])
  output = row['Output']
  formula = row['Formula']
  formula_raw = formula

  fileName = row['Filename']
  equationIdentifyer = row['Filename']
  equationName = row['EquationName']
  equationNumber= row['Number']
  descriptiveName = row['DescriptiveName']

  parts = fileName.split('.')
  if(len(parts) == 3):
    className = f'Feynman{parts[0]}Ch{parts[1]}Eq{parts[2]}'
  else:
     className= f'Feynman{equationName}'
  print(parts)
  
  print(f'{equationName}, {descriptiveName}')



  #placeholders for 10 variables were added to the CSV
  #parsing each (even if the are empty) and adding them to a list
  variables = [
    ( row['v1_name'],row['v1_low'],row['v1_high'] ),
    ( row['v2_name'],row['v2_low'],row['v2_high'] ),
    ( row['v3_name'],row['v3_low'],row['v3_high'] ),
    ( row['v4_name'],row['v4_low'],row['v4_high'] ),
    ( row['v5_name'],row['v5_low'],row['v5_high'] ),
    ( row['v6_name'],row['v6_low'],row['v6_high'] ),
    ( row['v7_name'],row['v7_low'],row['v7_high'] ),
    ( row['v8_name'],row['v8_low'],row['v8_high'] ),
    ( row['v9_name'],row['v9_low'],row['v9_high'] ),
    ( row['v10_name'],row['v10_low'],row['v10_high'] ),
  ]
  #keeping only the number of variables used per row
  variables = variables[:no_of_variables]

  arguments = []
  names_string_commaSeparated = []
  variable_names = [name for (name, low, high) in variables ]
  variable_names_commaSeparated = []
  uniform_ranges = []
  variables_and_ranges = []

  variable_order = dict( zip(variable_names, range(0, len(variables))))

  for name in sorted(variable_names, key=len, reverse=True):
    i = variable_order[name]
    formula = formula.replace(f'{name}_', f'?1')
    formula = formula.replace(f'{name}1', f'?2')
    formula = formula.replace(f'x[', f'?3')
    formula = formula.replace(f'sqrt', f'?4')
    formula = formula.replace(f'exp', f'?5')
    formula = formula.replace(f'arccos', f'?6')
    formula = formula.replace(f'arcsin', f'?7')
    formula = formula.replace(f'cos', f'?8')
    formula = formula.replace(f'sin', f'?9')
    formula = formula.replace(name, f'x[{i}]')
    formula = formula.replace(f'?1', f'{name}_')
    formula = formula.replace(f'?2', f'{name}1')
    formula = formula.replace(f'?3', f'x[')
    formula = formula.replace(f'?4', f'sqrt')
    formula = formula.replace(f'?5', f'exp')
    formula = formula.replace(f'?6', f'arccos')
    formula = formula.replace(f'?7', f'arcsin')
    formula = formula.replace(f'?8', f'cos')
    formula = formula.replace(f'?9', f'sin')

  i = 0
  for (name, low, high) in variables:
    #used for the function docstring
    arguments.append(f'        - x[{i}]: {name} (float, default range ({low},{high}))')
    uniform_ranges.append(f'              SimpleSampling({low},{high}, uses_negative=False)')
    #all variables and functions are also added to a dictionary to improve generic programmability
    variables_and_ranges.append({"name":name, "low":low , "high":high})
    #used for the dataframe definitions
    names_string_commaSeparated.append(f"'{name}'")
    #used for e.g. function parameters
    variable_names.append(name)
    i = i+1

  #add the resulting output variable name 
  names_string_commaSeparated.append(f"'{output}'")

  arguments = "\n".join(arguments)
  uniform_ranges = ",\n".join(uniform_ranges)
  variable_index_access = [f"{v} = X[{idx}]" for v, idx  in zip(variable_names, range(0,len(variable_names)))]
  variable_index_access =  "\n      ".join(variable_index_access)
  names_string_commaSeparated = ",".join(names_string_commaSeparated)
  variable_names_commaSeparated = ",".join(variable_names)
  number_of_variables = len(variables)
  
    #format csv formulas to be numpy compatible
  formula_numpy_formatted = formula
  formula_numpy_formatted = formula_numpy_formatted.replace('arcsin',f'placeholder1')
  formula_numpy_formatted = formula_numpy_formatted.replace('arccos',f'placeholder2')

  formula_numpy_formatted = formula_numpy_formatted.replace('sqrt',f'{numpyShort}.sqrt')
  formula_numpy_formatted = formula_numpy_formatted.replace('exp',f'{numpyShort}.exp')
  formula_numpy_formatted = formula_numpy_formatted.replace('pi',f'{numpyShort}.pi')
  formula_numpy_formatted = formula_numpy_formatted.replace('sin',f'{numpyShort}.sin')
  formula_numpy_formatted = formula_numpy_formatted.replace('cos',f'{numpyShort}.cos')
  formula_numpy_formatted = formula_numpy_formatted.replace('tanh',f'{numpyShort}.tanh')
  formula_numpy_formatted = formula_numpy_formatted.replace('ln',f'{numpyShort}.log') #log in numpy is ln

  formula_numpy_formatted = formula_numpy_formatted.replace('placeholder1',f'{numpyShort}.arcsin')
  formula_numpy_formatted = formula_numpy_formatted.replace('placeholder2',f'{numpyShort}.arccos')

  formula_sympy_formatted = formula
  formula_sympy_formatted = formula_sympy_formatted.replace('arcsin',f'placeholder1')
  formula_sympy_formatted = formula_sympy_formatted.replace('arccos',f'placeholder2')

  formula_sympy_formatted = formula_sympy_formatted.replace('sqrt',f'{sympyShort}.sqrt')
  formula_sympy_formatted = formula_sympy_formatted.replace('exp',f'{sympyShort}.exp')
  formula_sympy_formatted = formula_sympy_formatted.replace('pi',f'{sympyShort}.pi')
  formula_sympy_formatted = formula_sympy_formatted.replace('sin',f'{sympyShort}.sin')
  formula_sympy_formatted = formula_sympy_formatted.replace('cos',f'{sympyShort}.cos')
  formula_sympy_formatted = formula_sympy_formatted.replace('tanh',f'{sympyShort}.tanh')
  formula_sympy_formatted = formula_sympy_formatted.replace('ln',f'{sympyShort}.log') #log in sympy is ln

  formula_sympy_formatted = formula_sympy_formatted.replace('placeholder1',f'{sympyShort}.asin')
  formula_sympy_formatted = formula_sympy_formatted.replace('placeholder2',f'{sympyShort}.acos')


  # multiline code-template used to generate the actual python code
  # first function only includes the formula itself and is resused by the 
  # data generation function returning a dataframe with inputs and target
  lines.append(f'''
@register_feynman_eq_class
class {className}(KnownEquation):
    """
    - Equation: {equationIdentifyer}
    - Raw: {formula_raw}
    - Num. Vars: {number_of_variables}
    - Vars:
{arguments}
    """
    _eq_name = 'feynman-{equationIdentifyer.lower()}'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
{uniform_ranges}
            ]

        super().__init__(num_vars={number_of_variables}, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = {formula_sympy_formatted}

    def eq_func(self, x):
        return {formula_numpy_formatted}
  '''.format(className,
            equationIdentifyer,
            equationName,
            descriptiveName,
            names_string_commaSeparated,
            uniform_ranges,
            variable_names_commaSeparated,
            arguments,
            formula,
            formula_numpy_formatted)
  )



#write to file
with open("SCR_Benchmarks/AIFeynman/feynman.py", "w") as text_file:
    text_file.write("\n".join(lines))