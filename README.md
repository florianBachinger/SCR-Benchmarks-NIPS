# NIPS Benchmark



## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started


# Credit
Reference this work:
```bibtex

```
Our contribution combines the work of the following two publications into one convenient package.
We enhance their work by adding knowledge about the expected function shapes of the benchmark formulas. 

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

Credit to Matsubara et al. for reviewing and adapting the formulas and variable ranges to reasonable sampling values:
```bibtex
  @article{matsubara2022rethinking,
    title={Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery},
    author={Matsubara, Yoshitomo and Chiba, Naoya and Igarashi, Ryo and Tatsunori, Taniai and Ushiku, Yoshitaka},
    journal={arXiv preprint arXiv:2206.10540},
    year={2022}
  }
```