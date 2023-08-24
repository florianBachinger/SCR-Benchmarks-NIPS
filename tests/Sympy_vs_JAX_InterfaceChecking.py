import jax.numpy as jnp

import SCRBenchmark.SRSDFeynman as srsdf
from SCRBenchmark import Benchmark

################ ICh6Eq20 ################
ICh6Eq20 = Benchmark(srsdf.FeynmanICh6Eq20)

def f(x):
  return jnp.exp(-(x[0] / x[1]) ** 2 / 2) / (jnp.sqrt(2 * jnp.pi) * x[1])

print("JAX ICh6Eq20 Test:")
print(ICh6Eq20.check_constraints(f, Library = "JAX"))

print("SymPy ICh6Eq20 Test:")
print(ICh6Eq20.check_constraints("exp(-(x0 / x1) ** 2 / 2) / (sqrt(2 * pi) * x1)"))


################ ICh9Eq18 ################
ICh9Eq18 = Benchmark(srsdf.FeynmanICh9Eq18)

def g(x):
  return srsdf.feynman.GRAVITATIONAL_CONSTANT * x[0] * x[1] / ((x[2] - x[3]) ** 2 + (x[4] - x[5]) ** 2 + (x[6] - x[7]) ** 2)

print("JAX ICh9Eq18 Test:")
print(ICh9Eq18.check_constraints(g, Library = "JAX"))

print("SymPy ICh9Eq18 Test:")
print(ICh9Eq18.check_constraints('6.67430e-11 * x0 * x1 / ((x2 - x3) ** 2 + (x4 - x5) ** 2 + (x6 - x7) ** 2)'))