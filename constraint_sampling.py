import numpy as np
import pandas as pd
import sympy as sympy
from SCR_Benchmarks.Constants import StringKeys as sk
from SCR_Benchmarks.base import get_constraint_descriptor
from SCR_Benchmarks.base import create_dataset_from_sampling_objectives
import SCR_Benchmarks.SRSDFeynman as srsdf
import copy
f = srsdf.FeynmanICh6Eq20()

print (f.determine_constraints())