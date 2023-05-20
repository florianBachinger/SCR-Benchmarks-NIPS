import numpy as np
import pandas as pd
import inspect 
import SCR_Benchmarks.SRSDFeynman as srsdf

def formatEquation(equation, function):
      for (index, name) in zip(range(0,len(equation.get_var_names())), equation.get_var_names()):
            function = function.replace(f'x[{index}]',name)

      function = function.replace('GRAVITATIONAL_CONSTANT', '6.67430e-11')
      function = function.replace('GRAVITATIONAL_ACCELERATION', '9.80665')
      function = function.replace('SPEED_OF_LIGHT', '2.99792458e8')
      function = function.replace('ELECTRIC_CONSTANT', '8.854e-12')
      function = function.replace('PLANCK_CONSTANT', '6.626e-34')
      function = function.replace('BOLTZMANN_CONSTANT', '1.380649e-23')
      function = function.replace('BOHR_MAGNETON', '9.2740100783e-24')
      function = function.replace('DIRAC_CONSTANT', '1.054571817e-34')
      function = function.replace('ELECTRON_MASS', '9.10938356e-31')
      function = function.replace('FINE_STRUCTURE_CONSTANT', '7.2973525693e-3')
      function = function.replace('\\', '')
      function = function.replace('ln', 'log') #for sympy and numpy log is base 2
      return function
      

for name in srsdf.AllEquations:
      eq = srsdf.AllEquations[name]()
      raw = eq.get_eq_raw() 


      npFunc = eq.eq_func
      npFunc = inspect.getsource(npFunc).split('return ')[1]
      npFunc = npFunc.replace('\n','')
      npFunc = npFunc.replace('np.','')
      npFuncForm =formatEquation(eq,npFunc)

      raw = raw.replace(' ','')
      raw = raw.replace('ln','log')
      npFuncForm = npFuncForm.replace(' ','')

      assert raw == npFuncForm
