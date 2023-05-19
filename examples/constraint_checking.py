import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import SCR_Benchmarks.SRSDFeynman as srsdf
from SCR_Benchmarks.constraints import SCRBenchmark

ICh6Eq20 = SCRBenchmark(srsdf.FeynmanICh6Eq20)
# Raw: exp(-(theta / sigma) ** 2 / 2) / (sqrt(2 * pi) * sigma)
# is monotonic increasing over theta in -inf. <= theta <= 0
# is monotonic decreasing over theta in 0 <= theta <= inf.

############################################
#use the short variable names of SRSDFeynman
############################################

#prints true as no constraint is violated
print(ICh6Eq20.check_constraints("-(x0*x0)"))

#prints false as the decreasing constraint for 0 <= theta <= inf. is violated
print(ICh6Eq20.check_constraints("x0"))

#prints false as the increasing constraint for -inf. <= theta <= 0 is violated
print(ICh6Eq20.check_constraints("-x0"))

#prints false as both constraints for x0 (theta) are violated
print(ICh6Eq20.check_constraints("(x0*x0)"))

########################################################################
# test the same function, expect the same outputs, but use display names
########################################################################
#prints true as no constraint is violated
print(ICh6Eq20.check_constraints("-(theta*theta)",use_display_names=True))

#prints false as the decreasing constraint for 0 <= theta <= inf. is violated
print(ICh6Eq20.check_constraints("theta",use_display_names=True))

#prints false as the increasing constraint for -inf. <= theta <= 0 is violated
print(ICh6Eq20.check_constraints("-theta",use_display_names=True))

#prints false as both constraints for x0 (theta) are violated
print(ICh6Eq20.check_constraints("(theta*theta)",use_display_names=True))