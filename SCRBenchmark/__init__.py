# flake8: noqa

"""
    SCRBenchmark
"""


__version__ = "0.5.0"

# import ApiClient
from SCRBenchmark import SRSDFeynman
from SCRBenchmark import Constants
from SCRBenchmark import Data

from .base import get_constraint_descriptor
from .base import create_dataset_from_sampling_objectives
from .base import KnownEquation
from .benchmark import Benchmark
from .suite import BenchmarkSuite
from .seeds import SEEDS
from .suite import HARD_NOISE_LEVELS, HARD_SAMPLE_SIZES,FEYNMAN_SRSD_HARD



from SCRBenchmark.Constants import StringKeys

from SCRBenchmark.Data.feynman_srsdf_constraint_info import SRSD_EQUATION_CONSTRAINTS
from SCRBenchmark.Data.feynman_srsd_info import SRSD_EQUATION_CONFIG_DICT

