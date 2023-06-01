from SCRBenchmark import FEYNMAN_SRSD_HARD,HARD_NOISE_LEVELS,HARD_SAMPLE_SIZES
from SCRBenchmark import BenchmarkSuite
import json
import numpy as np
import pandas as pd

target_folder = './experiments/repeated_best_config_data'

best_configurations = pd.read_csv('./experiments/best_configurations.csv')
# instances = FEYNMAN_SRSD_HARD
instances = ['FeynmanICh6Eq20','FeynmanICh6Eq20a','FeynmanICh6Eq20b']

print('generating instances')
#creates one folder per equation under the parent folder
# each equation folder contains the info file as json
# and the data files for each configuration as csv
BenchmarkSuite.create_hard_instances(target_folder = target_folder,
                                        Equations= instances,
                                        sample_sizes=HARD_SAMPLE_SIZES,
                                        noise_levels=HARD_NOISE_LEVELS,
                                        repetitions = 10
                                        )

# for shape-constrained polynomial regression we add
# the algorithm configuration to the generated json files
print('appending info for SCPR')
for equation_name in instances:
  print(equation_name)
  equation_folder = f'{target_folder}/{equation_name}'
  best_configuration = best_configurations[best_configurations['EquationName'] == equation_name].iloc[0]
  with open(f'{equation_folder}/constraint_info.json', "r+") as f:
    data = json.load(f)
    data['Degrees']= [best_configuration['Degree']]
    data['Lambdas']= [best_configuration['Lambda']]
    data['Alphas']= [best_configuration['Alpha']]
    data['MaxInteractions']= [best_configuration['MaxInteractions']]

    supportedConstraints = []
    for constraint in data['Constraints']:
      if constraint['order_derivative'] == 2:
        variables = np.unique(constraint['var_name'])
        variables_display = np.unique(constraint['var_display_name'])
        if(len(variables) == 1):
          constraint['var_name'] = variables[0]
          constraint['var_display_name'] = variables_display[0]
          supportedConstraints.append(constraint)
      else: 
        supportedConstraints.append(constraint)
    data['Constraints'] = supportedConstraints
    
    f.seek(0)
    f.write(str(data).replace('\'',"\""))
    f.truncate()
    f.close()

    