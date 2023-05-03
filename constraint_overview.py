import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import SCR_Benchmarks.SRSDFeynman as srsdf
import SCR_Benchmarks.AIFeynman as aif

for name in srsdf.AllEquations:
    eq = srsdf.AllEquations[name]()
    
    constraint_shorts = []
    for constraint in eq.get_constraints():
        shorthand = 'None'
        if(constraint['descriptor'] == 'monotonic decreasing'):
          shorthand = '<=0'
        if(constraint['descriptor'] == 'monotonic increasing'):
          shorthand = '>=0'
        constraint_shorts.append(f"{constraint['var_display_name']}:{shorthand}")

    print(f"{eq.get_eq_name()} {','.join(constraint_shorts)}")