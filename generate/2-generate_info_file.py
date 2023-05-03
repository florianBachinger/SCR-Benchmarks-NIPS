import pandas as pd
import inspect
import SCR_Benchmarks.Constants.StringKeys as sk
import SCR_Benchmarks.SRSDFeynman.feynman as srsd

aif_lines = []
srsd_lines = []
numpyShort = 'np'
sympyShort = 'sympy'

CURLY_OPEN = "{{"
CURLY_CLOSED = "}}"

# read and prepare standard equations 
feynmanEquations = pd.read_csv('generate/src/FeynmanEquations.csv')
# filter to exclude the empty lines in FeynmanEquations.csv
feynmanEquations = feynmanEquations[feynmanEquations['Number']>=1]
feynmanEquations[sk.EQUATION_EQUATION_NAME_KEY] = [f'Feynman{int(number)}' for number in feynmanEquations['Number']]
feynmanEquations[sk.EQUATION_EQUATION_DESCRIPTIVE_NAME_KEY] = [f'Feynman{int(number)}, Lecture {filename}' for number,filename in zip(feynmanEquations['Number'],feynmanEquations['Filename'])]

# read and prepare bonus equations 
bonusEquasions = pd.read_csv('generate/src/BonusEquations.csv')
# filter to exclude the empty lines in FeynmanEquations.csv
bonusEquasions = bonusEquasions[bonusEquasions['Number']>=1]
bonusEquasions[sk.EQUATION_EQUATION_NAME_KEY] = [f'Bonus{int(number)}' for number in bonusEquasions['Number']]
bonusEquasions[sk.EQUATION_EQUATION_DESCRIPTIVE_NAME_KEY] = [f'Bonus{number}, {name}' for name,number in zip(bonusEquasions['Name'], bonusEquasions['Number'])]

#merge both into one dataframe
equations = pd.concat([feynmanEquations,bonusEquasions],ignore_index=True)

file_aif_start = """
\"\"\"

\"\"\"

AIF_EQUATION_CONFIG_DICT = {
"""

file_srsd_start = """
\"\"\"

\"\"\"

SRSD_EQUATION_CONFIG_DICT = {
"""

def formatEntry(className,
            curlyO, 
            formula,
            variable_names_strings_commaSeparated,
            output,
            curlyC):
  return f'''
    "{className}": {curlyO}
        "{sk.EQUATION_CONFIG_DICT_RAW_EXPRESSION_KEY}" : "{formula}",
        "{sk.EQUATION_CONFIG_DICT_VARIABLE_KEY}" : [{variable_names_strings_commaSeparated}],
        "{sk.EQUATION_CONFIG_DICT_OUTPUT_KEY}" : "{output}"
    {curlyC},
  '''.format(className,
            curlyO, 
            formula,
            variable_names_strings_commaSeparated,
            output,
            curlyC,
           )
# add imports at file-beginning
aif_lines.append(file_aif_start)
srsd_lines.append(file_srsd_start)



for index, row in equations.iterrows():
  #iterate over the CSV rows
  no_of_variables = int(row['# variables'])
  output = row['Output']
  formula = row['Formula']

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
  variable_names_strings =  [f'"{name}"' for name in variable_names ]
  uniform_ranges = []
  variables_and_ranges = []

  variable_names_commaSeparated = ",".join(variable_names)
  variable_names_strings_commaSeparated = ",".join(variable_names_strings)
  number_of_variables = len(variables)


  # multiline code-template used to generate the actual python code
  # first function only includes the formula itself and is resused by the 
  # data generation function returning a dataframe with inputs and target
  aif_lines.append(formatEntry(className,
            CURLY_OPEN, 
            formula,
            variable_names_strings_commaSeparated,
            output,
            CURLY_CLOSED,))
  

  equation = srsd.FEYNMAN_EQUATION_CLASS_DICT[className]()  
  doclines = equation.__doc__.splitlines()

  index_vars = next(i for i, x in enumerate(doclines) if '- Vars:' in x)
  index_constraints = next(i for i, x in enumerate(doclines) if '- Constraints:' in x)
  var_doc_lines = doclines[index_vars+1:index_constraints]
  var_names = [f'"{var.replace("        - ","").split(" ")[1]}"' for var in var_doc_lines]
  variable_names_strings_commaSeparated = ",".join(var_names)
  srsd_lines.append(formatEntry(className,
          CURLY_OPEN, 
          next(match for match in doclines if '- Raw' in match).split('- Raw: ')[1],
          variable_names_strings_commaSeparated,
          output,
          CURLY_CLOSED,))


aif_lines.append("}")
#write to file
with open("SCR_Benchmarks/Info/feynman_aif_info.py", "w") as text_file:
    text_file.write("".join(aif_lines))

srsd_lines.append('}')
#write to file
with open("SCR_Benchmarks/Info/feynman_srsd_info.py", "w") as text_file:
    text_file.write("".join(srsd_lines))

