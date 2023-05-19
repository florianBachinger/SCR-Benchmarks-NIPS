import SCR_Benchmarks.base as base
import sympy
import numpy as np
import copy
import SCR_Benchmarks.Constants.StringKeys as sk

SAMPLE_SIZE = 1_000_000

def get_constraint_descriptor( eq, local_dict, xs):
    f = sympy.lambdify(local_dict, eq,"numpy")
    #calculate gradient per data point
    # gradients = np.array([ f(*row) for row in xs ])
    # speedup of 5:
    f_v = np.vectorize(f)
    gradients = f_v(*(xs.T))

    unique_gradient_signs = set(np.unique(np.sign(gradients)))

    if((unique_gradient_signs ==  set([-1])) or (unique_gradient_signs ==  set([-1, 0]))):
      descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_MONOTONIC_DECREASING_CONSTRAINT
    elif ((unique_gradient_signs ==  set([1])) or (unique_gradient_signs ==  set([0, 1]))):
        descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_MONOTONIC_INCREASING_CONSTRAINT
    elif ((unique_gradient_signs ==  set([-1, 1])) or (unique_gradient_signs ==  set([-1, 0, 1]))):
        descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT
    elif (unique_gradient_signs ==  set([0])):
        descriptor = sk.EQUATION_CONSTRAINTS_DESCRIPTOR_CONSTANT_CONSTRAINT
    else:
      raise "Unforseen sign values!"
    return descriptor

class SCRBenchmark(object):
    _eq_name = None

    def __init__(self, equation, initialize_datasets_on_creation = True):
        super().__init__()
        assert issubclass(equation ,base.KnownEquation)

        self.equation = equation()
        self.constraints = self.equation.get_constraints()

        if(initialize_datasets_on_creation):
          self.datasets = self.initialize_datasets_for_constraint_checking()
        
    def initialize_datasets_for_constraint_checking(self):
      constraints = [c for c in self.constraints if c[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]!=sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT]
      self.datasets = {}
      if(len(constraints) == 0):
          raise Warning( f"equation {self.equation._eq_name} has to constraints to be checked. all checks will return true.")
      for constraint in constraints:
         self.datasets[constraint[sk.EQUATION_CONSTRAINTS_ID_KEY]] = np.random.uniform(
              [low for (low, _) in [ eval(var_range) for var_range in constraint[sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY].values()]],
              [high for (_, high) in [ eval(var_range) for var_range in constraint[sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY].values()]],
              (SAMPLE_SIZE,self.equation.get_var_count())
            )

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
        descriptor = get_constraint_descriptor(derivative, local_dict.keys(), xs)
        if(descriptor != constraint[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]):
            violated_constraints.append(constraint)

      return (len(violated_constraints) == 0, violated_constraints)

    def determine_constraints(self, sample_size = SAMPLE_SIZE):

      f_primes = [(sympy.Derivative(self.equation.sympy_eq, var).doit(),var.name, var_display_name, 1) 
                 for (var,var_display_name) 
                 in list(zip(self.equation.x, self.equation.get_var_names()))]
      
      f_prime_mat = [[ (sympy.Derivative(f_prime, var).doit(), f'[{prime_var_name},{var}]', f'[{prime_var_display_name},{var_display_name}]', 2 ) 
                        for (var,var_display_name)  
                        in list(zip(self.equation.x, self.equation.get_var_names()))] 
                     for (f_prime, prime_var_name, prime_var_display_name, _) 
                     in f_primes]
      f_prime_mat_flattened = [item for sublist in f_prime_mat for item in sublist]
      derviatives = f_primes+f_prime_mat_flattened

      split_objectives = []
      constraints = []

      objectives= list(
         zip(
          self.equation.x,
          [obj.to_uniform_sampling() for obj in self.equation.sampling_objs]
         ))

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
        for (derivative, var_name, var_display_name, order_derivative) in derviatives:
          sampling_space = { var.name: str(obj.get_value_range()) for (var, obj) in split_objective}

          sampling_objectives = [obj for (var, obj) in split_objective]
          xs = self.equation.get_inputs_from_dataset(
                  base.create_dataset_from_sampling_objectives(sampling_objectives, 
                                                          self.equation.sympy_eq, 
                                                          self.equation.eq_func, 
                                                          self.equation.check_if_valid, 
                                                          sample_size,
                                                          patience = sample_size)
                )

          descriptor =  get_constraint_descriptor(derivative, self.equation.x, xs)
          print(f'> partial derivative over ({var_name}) with space {sampling_space} with constraint ({descriptor})')
          if(descriptor != sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT):
            constraints.append({sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY:str(var_name),
              sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY:var_display_name,
              sk.EQUATION_CONSTRAINTS_ORDER_DERIVATIVE_KEY:order_derivative,
              sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY: descriptor,
              sk.EQUATION_CONSTRAINTS_DERIVATIVE_KEY: str(derivative),
              sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY: sampling_space  })
      return constraints