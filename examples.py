import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import SCR_Benchmarks.SRSDFeynman as srsdf

import time

ICh6Eq20b = srsdf.FeynmanICh6Eq20b()
xs =ICh6Eq20b.create_input_dataset(sample_size = 1_000_000)
# is monotonic 

#use the short variable names of SRSDFeynman

#prints false as constraint for x2 is violated
print(ICh6Eq20b.check_constraints("x1",xs= xs))
#prints true as no constraint is violated
print(ICh6Eq20b.check_constraints("x2",xs= xs))

# use the self-explained display names

#prints false but uses display variable names
print(ICh6Eq20b.check_constraints("theta",xs= xs, use_display_names=True))
#prints true but uses display variable names
print(ICh6Eq20b.check_constraints("theta1",xs= xs, use_display_names=True))