# NIPS Benchmark



## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/florianBachinger/NIPS-Benchmarks.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/florianBachinger/NIPS-Benchmarks.git`)

Then import the package:
```python
import SCR_Benchmarks
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import SCR_Benchmarks
```

## Getting Started

```python
import numpy as np
import pandas as pd
import SCR_Benchmarks.SRSDFeynman as srsdf

import time

ICh6Eq20b = srsdf.FeynmanICh6Eq20b()
xs =ICh6Eq20b.create_input_dataset(sample_size = 1_000_000) #providing the sample_size is optional

#prints false as constraint for x2 is violated
print(ICh6Eq20b.check_constraints("x1",xs= xs))
#prints true as no constraint is violated
print(ICh6Eq20b.check_constraints("x2",xs= xs))

#prints false but uses display variable names
print(ICh6Eq20b.check_constraints("theta",xs= xs, use_display_names=True))
#prints true but uses display variable names
print(ICh6Eq20b.check_constraints("sigma",xs= xs, use_display_names=True))
```
# Credit
Reference this work:
```bibtex

```
We enhance the work of Matsubara et al. by determining the _shape constraints_ that describe the expected function shapes of the benchmark formulas. This knowledge can be used to enforce the behavior of trained prediction models and to e.g., improve extrapolation behavior.


Credit to Matsubara et al. for reviewing and adapting the formulas and variable ranges of Udrescu et al. to reasonable sampling values:
```bibtex
  @article{matsubara2022rethinking,
    title={Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery},
    author={Matsubara, Yoshitomo and Chiba, Naoya and Igarashi, Ryo and Tatsunori, Taniai and Ushiku, Yoshitaka},
    journal={arXiv preprint arXiv:2206.10540},
    year={2022}
  }
```

Credit to Udrescu et al. for the initial benchmark set:
```bibtex
  @article{udrescu2020ai,
    title={AI Feynman: A physics-inspired method for symbolic regression},
    author={Udrescu, Silviu-Marian and Tegmark, Max},
    journal={Science Advances},
    volume={6},
    number={16},
    pages={eaay2631},
    year={2020},
    publisher={American Association for the Advancement of Science}
  }
```