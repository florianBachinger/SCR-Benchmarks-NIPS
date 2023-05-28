# flake8: noqa

"""
    SCR_Benchmarks
"""


__version__ = "0.2.0"

# import ApiClient
from SCR_Benchmarks import SRSDFeynman
from SCR_Benchmarks import Constants
from SCR_Benchmarks import Data
from SCR_Benchmarks.base import get_constraint_descriptor
from SCR_Benchmarks.scr_benchmark import SCRBenchmark

from .base import KnownEquation

from SCR_Benchmarks.Constants import StringKeys

from SCR_Benchmarks.Data.feynman_srsdf_constraint_info import SRSD_EQUATION_CONSTRAINTS
from SCR_Benchmarks.Data.feynman_srsd_info import SRSD_EQUATION_CONFIG_DICT

