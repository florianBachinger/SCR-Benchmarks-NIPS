import numpy as np
import pandas as pd
import sympy as sympy
from SCR_Benchmarks.Constants import StringKeys as sk
import SCR_Benchmarks.SRSDFeynman as srsdf
from SCR_Benchmarks import SCRBenchmark
import copy

ICh6Eq20 = SCRBenchmark(srsdf.FeynmanICh6Eq20)
constraints =  ICh6Eq20.determine_constraints()

assert constraints == ICh6Eq20.get_constraints()