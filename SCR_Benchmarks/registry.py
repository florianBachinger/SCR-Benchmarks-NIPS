"""
  Copied April 2023 from https://github.com/omron-sinicx/srsd-benchmark under MIT licence
  Credit Matsubara et al.:
  @article{matsubara2022rethinking,
    title={Rethinking Symbolic Regression Datasets and Benchmarks for Scientific Discovery},
    author={Matsubara, Yoshitomo and Chiba, Naoya and Igarashi, Ryo and Tatsunori, Taniai and Ushiku, Yoshitaka},
    journal={arXiv preprint arXiv:2206.10540},
    year={2022}
  }
"""

from collections import OrderedDict

SAMPLING_FUNC_DICT = OrderedDict()
SAMPLING_CLASS_DICT = OrderedDict()
EQUATION_CLASS_DICT = OrderedDict()


def register_sampling_func(func):
    SAMPLING_FUNC_DICT[func.__name__] = func
    return func


def register_sampling_class(cls):
    SAMPLING_CLASS_DICT[cls.__name__] = cls
    return cls


def register_eq_class(cls):
    EQUATION_CLASS_DICT[cls.__name__] = cls
    return cls


def get_sampling_obj(key, **kwargs):
    if key in SAMPLING_FUNC_DICT:
        return SAMPLING_FUNC_DICT[key]
    elif key in SAMPLING_CLASS_DICT:
        return SAMPLING_CLASS_DICT[key](**kwargs)
    raise KeyError(f'`{key}` is not expected as a sampling object key')


def get_eq_obj(key, **kwargs):
    if key in EQUATION_CLASS_DICT:
        return EQUATION_CLASS_DICT[key](**kwargs)
    raise KeyError(f'`{key}` is not expected as a equation object key')
