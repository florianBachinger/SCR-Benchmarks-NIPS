"""
    SCRBenchmark
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "SCRBenchmark"
VERSION = "0.5.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "numpy==1.24.3",
  "sympy==1.11.1",
  "pandas==2.0.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Can be used to generate benchmark instance data for instances with known constraints. And can check if provided models adhere to the known constraints.",
    author="Florian Bachinger",
    author_email="florian.bachinger@fh-hagenberg.at",
    url="",
    keywords=["Benchmark","Shape Constrained Regression", "Symbolic Regression", "SymReg"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests","example","examples","generate",]),
    include_package_data=True,
    long_description="""\
    No description provided
    """
)
