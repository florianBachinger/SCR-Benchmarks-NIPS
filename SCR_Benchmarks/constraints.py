import SCR_Benchmarks.base as base
import sympy
import numpy as np
import copy
import SCR_Benchmarks.Constants.StringKeys as sk


def get_constraint_descriptor(equation, eq, xs):
    f = sympy.lambdify(equation.x, eq,"numpy")
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
          self.datasets = self.initialize_datasets()
        
    def initialize_datasets(self):
      return
      notNone_constraints = [c for c in self.constraints if c[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]!='None']
      if(len(notNone_constraints) == 0):
          raise Warning( f"equation {self.equation._eq_name} has to constraints to be checked. all checks will return true.")

    def check_constraints (self, equation_candidate, use_display_names = False):
      constraints = self.equation.get_constraints()

      notNone_constraints = [c for c in constraints if c[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]!='None']
      if(len(notNone_constraints) == 0):
          return True #no constraints to check
      
      if(self.datasets is None):
          self.initialize_datasets()


      var_name_key = sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY
      local_dict = self.equation.get_sympy_eq_local_dict()
      if(use_display_names):
          var_name_key = sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY
          local_dict = { c[var_name_key] : sympy.Symbol(c[var_name_key]) for c in constraints }

      if( xs is None):
        xs =self.equation.create_input_dataset(sample_size = 1_000_000)

      expr = sympy.parse_expr(equation_candidate, evaluate=False, local_dict= local_dict)
      f_primes = [(sympy.Derivative(expr, local_dict[c[var_name_key]]).doit(),c) 
                 for c
                 in notNone_constraints ]
      violated_constraints = []
      for (derivative,known_constraint) in f_primes:
        descriptor = get_constraint_descriptor(self.equation, derivative,xs)
        if(descriptor != known_constraint[sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY]):
            violated_constraints.append(known_constraint)

      return (len(violated_constraints) == 0, violated_constraints)

    def determine_constraints(self, sample_size = 1_000_000):

      f_prime = [(sympy.Derivative(self.equation.sympy_eq, var).doit(),var, var_display_name) 
                 for (var,var_display_name) 
                 in list(zip(self.equation.x, self.equation.get_var_names()))]

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
        for (derivative, var_name, var_display_name) in f_prime:

          sampling_space = { var.name: str(obj.get_value_range()) for (var, obj) in split_objective}
          print(f'> partial derivative over {var_name} with space {sampling_space}')

          sampling_objectives = [obj for (var, obj) in split_objective]
          xs = self.equation.get_inputs_from_dataset(
                  base.create_dataset_from_sampling_objectives(sampling_objectives, 
                                                          self.equation.sympy_eq, 
                                                          self.equation.eq_func, 
                                                          self.equation.check_if_valid, 
                                                          sample_size,
                                                          patience = sample_size)
                )


          descriptor =  get_constraint_descriptor(self.equation, derivative,xs)
          if(descriptor != sk.EQUATION_CONSTRAINTS_DESCRIPTOR_NO_CONSTRAINT):
            constraints.append({sk.EQUATION_CONSTRAINTS_VAR_NAME_KEY:str(var_name),
              sk.EQUATION_CONSTRAINTS_VAR_DISPLAY_NAME_KEY:var_display_name,
              sk.EQUATION_CONSTRAINTS_ORDER_DERIVATIVE_KEY:1,
              sk.EQUATION_CONSTRAINTS_DESCRIPTOR_KEY: descriptor,
              sk.EQUATION_CONSTRAINTS_DERIVATIVE_KEY: str(derivative),
              sk.EQUATION_CONSTRAINTS_SAMPLE_SPACE_KEY: sampling_space  })
      return constraints