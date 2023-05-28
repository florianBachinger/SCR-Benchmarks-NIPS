from SCR_Benchmarks.suite import FEYNMAN_SRSD_HARD,HARD_TRAIN_TEST_SPLIT,HARD_NOISE_LEVELS,HARD_SAMPLE_SIZE
from SCR_Benchmarks.suite import SCRBenchmarkSuite
import json

target_folder = './data'

Degrees = [1,2,3,4,5,6,7]
Lambdas = [10**-7,10**-6,10**-5,10**-4,10**-3,10**-2,10**-1,1,10]
Alphas = [0,0.5,1]
MaxInteractions = [2,3,4]

print('generating instances')
#creates one folder per equation under the parent folder
# each equation folder contains the info file as json
# and the data files for each configuration as csv
SCRBenchmarkSuite.create_hard_instances(target_folder = target_folder,
                                        Equations=FEYNMAN_SRSD_HARD,
                                        sample_size=HARD_SAMPLE_SIZE,
                                        train_test_splits=HARD_TRAIN_TEST_SPLIT,
                                        noise_levels=HARD_NOISE_LEVELS)

# for shape-constrained polynomial regression we add
# the algorithm configuration to the generated json files
print('appending info for SCPR')
for equation_name in FEYNMAN_SRSD_HARD:
  print(equation_name)
  equation_folder = f'{target_folder}/{equation_name}'

  with open(f'{equation_folder}/constraint_info.json', "r+") as f:
    data = json.load(f)
    data['Degrees']= Degrees
    data['Lambdas']= Lambdas
    data['Alphas']= Alphas
    data['MaxInteractions']= MaxInteractions
    constraints  = []
    for constraint in data['Constraints']:
      sample_space = []
      for var in constraint['sample_space']:
        space = eval(constraint['sample_space'][var])
        sample_space.append({
          "name" : var,
          "low" : space[0],
          "high": space[1]
        })
      constraint['sample_space'] = sample_space

    f.seek(0)
    f.write(str(data).replace('\'',"\""))
    f.truncate()
    f.close()

    