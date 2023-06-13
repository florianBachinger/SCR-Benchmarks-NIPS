from .benchmark import Benchmark
from .SRSDFeynman import AllEquations
import pandas as pd
import os
import SCRBenchmark.Constants.StringKeys as sk
from .seeds import SEEDS

SAMPLING_PATIENCE = 10
HARD_SAMPLE_SIZES = [100,1000]
HARD_NOISE_LEVELS = [0,0.05,0.1,0.15,0.2]

FEYNMAN_SRSD_HARD = [
'FeynmanICh6Eq20a'
,'FeynmanICh6Eq20'
,'FeynmanICh6Eq20b'
,'FeynmanICh9Eq18'
,'FeynmanICh15Eq3t'
,'FeynmanICh15Eq3x'
,'FeynmanICh29Eq16'
,'FeynmanICh30Eq3'
,'FeynmanICh32Eq17'
,'FeynmanICh34Eq14'
,'FeynmanICh37Eq4'
,'FeynmanICh39Eq22'
,'FeynmanICh40Eq1'
,'FeynmanICh41Eq16'
,'FeynmanICh44Eq4' 
,'FeynmanICh50Eq26'
,'FeynmanIICh6Eq15a'
,'FeynmanIICh6Eq15b'
,'FeynmanIICh11Eq17'
,'FeynmanIICh11Eq20'
,'FeynmanIICh11Eq27'
,'FeynmanIICh11Eq28'
,'FeynmanIICh13Eq23'
,'FeynmanIICh13Eq34'
,'FeynmanIICh24Eq17'
,'FeynmanIICh35Eq18'
,'FeynmanIICh35Eq21'
,'FeynmanIICh36Eq38'
,'FeynmanIIICh4Eq33'
,'FeynmanIIICh9Eq52'
,'FeynmanIIICh10Eq19'
,'FeynmanIIICh21Eq20'
,'FeynmanBonus1'
,'FeynmanBonus2'
,'FeynmanBonus3'
,'FeynmanBonus4'
,'FeynmanBonus5'
,'FeynmanBonus6'
,'FeynmanBonus7'
,'FeynmanBonus9'
,'FeynmanBonus10'
,'FeynmanBonus11'
,'FeynmanBonus12'
,'FeynmanBonus13'
,'FeynmanBonus14'
,'FeynmanBonus15'
,'FeynmanBonus16'
,'FeynmanBonus17'
,'FeynmanBonus19'
,'FeynmanBonus20'
]

class BenchmarkSuite(object):
    _eq_name = None

    def __init__(self):
      super().__init__()

    def create_hard_instances( target_folder = './data',
                              Equations = FEYNMAN_SRSD_HARD,
                              sample_sizes = HARD_SAMPLE_SIZES,
                              noise_levels = HARD_NOISE_LEVELS,
                              repetitions = None):
      if repetitions > len(SEEDS):
        raise ValueError(f"Only {len(SEEDS)} seeds are predefined. If you change local settings, please report on this fact in your publication and publish the updated seeds in e.g. your repository.")   

      if not os.path.exists(target_folder):
        os.makedirs(target_folder)
      for equation_name in Equations:
        print(equation_name)
        benchmark = Benchmark(AllEquations[equation_name],initialize_constraint_checking_datasets=False)
        equation_folder = f'{target_folder}/{equation_name}'

        if not os.path.exists(equation_folder):
          os.makedirs(equation_folder)

        with open(f'{equation_folder}/constraint_info.json', "w") as text_file:
          text_file.write("{")
          text_file.write('"EquationName" : "')
          text_file.write(equation_name)
          text_file.write('", "TargetVariable" : "')
          text_file.write(str(benchmark.equation.get_output_name()).replace('\'',"\""))
          text_file.write('", "InputVariableRanges" : [')
          text_file.write( ",".join([ str(r) for r in  benchmark.equation.get_domain_ranges()]).replace('\'',"\"") )
          text_file.write('] , "Constraints" : ')
          text_file.write(str(benchmark.get_constraints()).replace('\'',"\""))
          text_file.write("}")
          
        for sample_size in sample_sizes:
          for noise_level in noise_levels:
              if(repetitions is None):
                if(not BenchmarkSuite.create_individual_dataset(target_folder,
                                                      benchmark,
                                                      equation_folder,
                                                      noise_level,
                                                      sample_size,
                                                      seed = SEEDS[0],
                                                      sampling_patience = 40,
                                                      )):
                  raise Warning(f"could not generate dataset for {equation_name} and sample_size {sample_size} noise_level {noise_level}")
              
              else:
                 for repetition in range(0,repetitions):
                   
                   if(not BenchmarkSuite.create_individual_dataset(target_folder,
                                                      benchmark,
                                                      equation_folder,
                                                      noise_level,
                                                      sample_size,
                                                      seed = SEEDS[repetition],
                                                      sampling_patience = 40,
                                                      file_prefix='',
                                                      file_suffix = f'_repetition{repetition}'
                                                      )):
                      raise Warning(f"could not generate dataset for {equation_name} and sample_size {sample_size} noise_level {noise_level}")   
         

    def create_individual_dataset(target_folder,
                                    benchmark,
                                    equation_folder, 
                                    noise_level,
                                    sample_size, 
                                    seed,
                                    sampling_patience = 40,
                                    file_prefix = '',
                                    file_suffix = ''):
        equation_name = benchmark._eq_name
        target_file = f'{equation_folder}/{file_prefix}{equation_name}_sample_size{sample_size}_noise_level{noise_level}{file_suffix}.csv'
        if os.path.exists(target_file):
           return True
        
        for i in range(1, sampling_patience):
          try:
            (training, test) = benchmark.create_dataframe(sample_size=sample_size,
                                                                  noise_level=noise_level,
                                                                  seed = seed,
                                                                  patience = sampling_patience,
                                                                  use_display_name = False)
            training['split'] = ['training'] * len(training)
            test['split'] = ['test'] * len(test)
            combined = pd.concat([training,test])
            combined.to_csv(target_file, index = False)
            return True
          except:
              print(f'error in {equation_name} with try {i}/{sampling_patience}')

        return False

         

        