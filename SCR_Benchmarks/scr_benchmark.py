import SCR_Benchmarks.base as base
import sympy
import numpy as np
import pandas as pd
import copy
import SCR_Benchmarks.Constants.StringKeys as sk
from SCR_Benchmarks.Data.feynman_srsdf_constraint_info import SRSD_EQUATION_CONSTRAINTS as SRSDFConstraints


class SCRBenchmark(object):
    _eq_name = None

    def __init__(self, equation, initialize_datasets_on_creation = True):
        super().__init__()
        assert issubclass(equation ,base.KnownEquation)

        self.equation = equation()
        self.constraints = self.get_constraints()

        if(initialize_datasets_on_creation):
          self.datasets = self.initialize_datasets_for_constraint_checking()

    def read_test_dataset(self):
        return pd.read_csv(f'./SCR_Benchmarks/Data/Test/{self.equation.get_eq_name()}.csv')
    
    def create_dataset(self,sample_size,patience = 10, noise_level = 0 ):
        assert (0<=noise_level and noise_level<=1), f'noise_level must be in [0,1]'

        xs = self.equation.create_dataset(sample_size,patience)

        if(noise_level>0):
          std_dev = np.std(xs[:,-1])
          xs[:,-1] = xs[:,-1] + np.random.normal(0,std_dev*np.sqrt(noise_level),len(xs))

        return (xs, self.read_test_dataset())
    
    def create_dataframe(self,sample_size,patience = 10, train_test_split = 0.8, noise_level = 0,use_display_name = False ):
       (train, test) = self.create_dataset(sample_size,patience, train_test_split,noise_level)
       train_df = self.equation.to_dataframe(train,use_display_name = False)
       test_df = self.equation.to_dataframe(test,use_display_name = False)
       return (train_df,test_df)

    def get_constraints (self):
      if(self.equation.get_eq_source() == sk.SRSDF_SOURCE_QUALIFIER):
          return next(x[sk.EQUATION_CONSTRAINTS_CONSTRAINTS_KEY] for x in SRSDFConstraints if x[sk.EQUATION_EQUATION_NAME_KEY] == self.equation.get_eq_name())
          
    def check_constraints (self, equation_candidate, use_display_names = False):
      constraints = self.equation.get_constraints()

      constraints = [c for c in constraints if c[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]!=sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT]
      if(len(constraints) == 0):
          return True #no constraints to check
      
      if(self.datasets is None):
          self.initialize_datasets_for_constraint_checking()

      # replace the sympy local dictionary with the display names of variables if specified
      local_dict = self.equation.get_sympy_eq_local_dict()
      if(use_display_names):
          local_dict = { c : sympy.Symbol(c) for c in self.equation.get_var_names()}

      # parse the provided candidate expression
      # will use display names if specified
      expr = sympy.parse_expr(equation_candidate, evaluate=False, local_dict= local_dict)

      #calculate all first order partial derivatives of the expression 
      f_primes = [(sympy.Derivative(expr, var).doit(),var.name, 1) 
                 for var
                 in local_dict.values()]
      
      #calculate all second order partial derivatives of the expression (every possible combination [Hessian])
      f_prime_mat = [[ (sympy.Derivative(f_prime, var).doit(), f'[{prime_var_name},{var}]', 2 ) 
                        for var
                        in local_dict.values()] 
                     for (f_prime, prime_var_name, _) 
                     in f_primes]
      
      #flatten 2d Hessian to 1d list and combine them 
      f_prime_mat_flattened = [item for sublist in f_prime_mat for item in sublist]
      derviatives = f_primes+f_prime_mat_flattened
      
      
      violated_constraints = []
      #check for all existing constraints if they are met
      for constraint in constraints:
        #every constraint has a specific input range in which they apply
        xs = self.datasets[constraint[sk.EQUATION_CONSTRAINTS_ID_KEY]]

        #the current constraint to be checked matches only one of derivatives (all possible combinations are derived)
        if(use_display_names):
          matches = [ derivative for (derivative, var, _) in derviatives if var == constraint[sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY]]
        else:
          matches = [ derivative for (derivative, var, _) in derviatives if var == constraint[sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY]]

        if(len(matches)>1):
           raise "derivatives are not names uniquely"
        if(len(matches)==0):
           raise "derivative not available"
        derivative = matches[0]

        #does the calculated (sampled) gradient for the current derivative match the constraint description
        descriptor = base.get_constraint_descriptor(derivative, local_dict.keys(), xs)
        if(descriptor != constraint[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]):
            violated_constraints.append(constraint)

      return (len(violated_constraints) == 0, violated_constraints)
