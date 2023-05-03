
"""
  Code structure and idea adapted from https://github.com/omron-sinicx/srsd-benchmark at April 2023 under MIT licence

  Equations and benchmark set, credited to 
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
  Equations and variable ranges copied from https://space.mit.edu/home/tegmark/aifeynman.html but with chapter/equation naming corrections from Udrescu et al.
"""
from collections import OrderedDict

import numpy as np
import sympy

from SCR_Benchmarks.base import KnownEquation
import SCR_Benchmarks.Constants.StringKeys as sk
from SCR_Benchmarks.registry import register_eq_class
from SCR_Benchmarks.sampling import DefaultSampling, IntegerSampling, SimpleSampling

FEYNMAN_EQUATION_CLASS_DICT = OrderedDict()

def register_feynman_eq_class(cls):
    register_eq_class(cls)
    FEYNMAN_EQUATION_CLASS_DICT[cls.__name__] = cls
    cls._eq_source = sk.AIF_SOURCE_QUALIFIER
    return cls



@register_feynman_eq_class
class FeynmanICh6Eq20a(KnownEquation):
    """
    - Equation: I.6.20a
    - Raw: exp(-theta**2/2)/sqrt(2*pi)
    - Num. Vars: 1
    - Vars:
        - x[0]: theta (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-i.6.20a'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=1, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.exp(-x[0]**2/2)/sympy.sqrt(2*sympy.pi)

    def eq_func(self, x):
        return np.exp(-x[0]**2/2)/np.sqrt(2*np.pi)
  

@register_feynman_eq_class
class FeynmanICh6Eq20(KnownEquation):
    """
    - Equation: I.6.20
    - Raw: exp(-(theta/sigma)**2/2)/(sqrt(2*pi)*sigma)
    - Num. Vars: 2
    - Vars:
        - x[0]: sigma (float, default range (1.0,3.0))
        - x[1]: theta (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-i.6.20'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.exp(-(x[1]/x[0])**2/2)/(sympy.sqrt(2*sympy.pi)*x[0])

    def eq_func(self, x):
        return np.exp(-(x[1]/x[0])**2/2)/(np.sqrt(2*np.pi)*x[0])
  

@register_feynman_eq_class
class FeynmanICh6Eq20b(KnownEquation):
    """
    - Equation: I.6.20b
    - Raw: exp(-((theta-theta1)/sigma)**2/2)/(sqrt(2*pi)*sigma)
    - Num. Vars: 3
    - Vars:
        - x[0]: sigma (float, default range (1.0,3.0))
        - x[1]: theta (float, default range (1.0,3.0))
        - x[2]: theta1 (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-i.6.20b'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.exp(-((x[1]-x[2])/x[0])**2/2)/(sympy.sqrt(2*sympy.pi)*x[0])

    def eq_func(self, x):
        return np.exp(-((x[1]-x[2])/x[0])**2/2)/(np.sqrt(2*np.pi)*x[0])
  

@register_feynman_eq_class
class FeynmanICh8Eq14(KnownEquation):
    """
    - Equation: I.8.14
    - Raw: sqrt((x2-x1)**2+(y2-y1)**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: x1 (float, default range (1.0,5.0))
        - x[1]: x2 (float, default range (1.0,5.0))
        - x[2]: y1 (float, default range (1.0,5.0))
        - x[3]: y2 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.8.14'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt((x[1]-x[0])**2+(x[3]-x[2])**2)

    def eq_func(self, x):
        return np.sqrt((x[1]-x[0])**2+(x[3]-x[2])**2)
  

@register_feynman_eq_class
class FeynmanICh9Eq18(KnownEquation):
    """
    - Equation: I.9.18
    - Raw: G*m1*m2/((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    - Num. Vars: 9
    - Vars:
        - x[0]: m1 (float, default range (1.0,2.0))
        - x[1]: m2 (float, default range (1.0,2.0))
        - x[2]: G (float, default range (1.0,2.0))
        - x[3]: x1 (float, default range (3.0,4.0))
        - x[4]: x2 (float, default range (1.0,2.0))
        - x[5]: y1 (float, default range (3.0,4.0))
        - x[6]: y2 (float, default range (1.0,2.0))
        - x[7]: z1 (float, default range (3.0,4.0))
        - x[8]: z2 (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-i.9.18'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,4.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,4.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,4.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=9, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[2]*x[0]*x[1]/((x[4]-x[3])**2+(x[6]-x[5])**2+(x[8]-x[7])**2)

    def eq_func(self, x):
        return x[2]*x[0]*x[1]/((x[4]-x[3])**2+(x[6]-x[5])**2+(x[8]-x[7])**2)
  

@register_feynman_eq_class
class FeynmanICh10Eq7(KnownEquation):
    """
    - Equation: I.10.7
    - Raw: m_0/sqrt(1-v**2/c**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: m_0 (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: c (float, default range (3.0,10.0))
    """
    _eq_name = 'feynman-i.10.7'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/sympy.sqrt(1-x[1]**2/x[2]**2)

    def eq_func(self, x):
        return x[0]/np.sqrt(1-x[1]**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanICh11Eq19(KnownEquation):
    """
    - Equation: I.11.19
    - Raw: x1*y1+x2*y2+x3*y3
    - Num. Vars: 6
    - Vars:
        - x[0]: x1 (float, default range (1.0,5.0))
        - x[1]: x2 (float, default range (1.0,5.0))
        - x[2]: x3 (float, default range (1.0,5.0))
        - x[3]: y1 (float, default range (1.0,5.0))
        - x[4]: y2 (float, default range (1.0,5.0))
        - x[5]: y3 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.11.19'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[3]+x[1]*x[4]+x[2]*x[5]

    def eq_func(self, x):
        return x[0]*x[3]+x[1]*x[4]+x[2]*x[5]
  

@register_feynman_eq_class
class FeynmanICh12Eq1(KnownEquation):
    """
    - Equation: I.12.1
    - Raw: mu*Nn
    - Num. Vars: 2
    - Vars:
        - x[0]: mu (float, default range (1.0,5.0))
        - x[1]: Nn (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.12.1'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]

    def eq_func(self, x):
        return x[0]*x[1]
  

@register_feynman_eq_class
class FeynmanICh12Eq2(KnownEquation):
    """
    - Equation: I.12.2
    - Raw: q1*q2*r/(4*pi*epsilon*r**3)
    - Num. Vars: 4
    - Vars:
        - x[0]: q1 (float, default range (1.0,5.0))
        - x[1]: q2 (float, default range (1.0,5.0))
        - x[2]: epsilon (float, default range (1.0,5.0))
        - x[3]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.12.2'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[3]/(4*sympy.pi*x[2]*x[3]**3)

    def eq_func(self, x):
        return x[0]*x[1]*x[3]/(4*np.pi*x[2]*x[3]**3)
  

@register_feynman_eq_class
class FeynmanICh12Eq4(KnownEquation):
    """
    - Equation: I.12.4
    - Raw: q1*r/(4*pi*epsilon*r**3)
    - Num. Vars: 3
    - Vars:
        - x[0]: q1 (float, default range (1.0,5.0))
        - x[1]: epsilon (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.12.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[2]/(4*sympy.pi*x[1]*x[2]**3)

    def eq_func(self, x):
        return x[0]*x[2]/(4*np.pi*x[1]*x[2]**3)
  

@register_feynman_eq_class
class FeynmanICh12Eq5(KnownEquation):
    """
    - Equation: I.12.5
    - Raw: q2*Ef
    - Num. Vars: 2
    - Vars:
        - x[0]: q2 (float, default range (1.0,5.0))
        - x[1]: Ef (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.12.5'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]

    def eq_func(self, x):
        return x[0]*x[1]
  

@register_feynman_eq_class
class FeynmanICh12Eq11(KnownEquation):
    """
    - Equation: I.12.11
    - Raw: q*(Ef+B*v*sin(theta))
    - Num. Vars: 5
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: Ef (float, default range (1.0,5.0))
        - x[2]: B (float, default range (1.0,5.0))
        - x[3]: v (float, default range (1.0,5.0))
        - x[4]: theta (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.12.11'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(x[1]+x[2]*x[3]*sympy.sin(x[4]))

    def eq_func(self, x):
        return x[0]*(x[1]+x[2]*x[3]*np.sin(x[4]))
  

@register_feynman_eq_class
class FeynmanICh13Eq4(KnownEquation):
    """
    - Equation: I.13.4
    - Raw: 1/2*m*(v**2+u**2+w**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,5.0))
        - x[2]: u (float, default range (1.0,5.0))
        - x[3]: w (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.13.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/2*x[0]*(x[1]**2+x[2]**2+x[3]**2)

    def eq_func(self, x):
        return 1/2*x[0]*(x[1]**2+x[2]**2+x[3]**2)
  

@register_feynman_eq_class
class FeynmanICh13Eq12(KnownEquation):
    """
    - Equation: I.13.12
    - Raw: G*m1*m2*(1/r2-1/r1)
    - Num. Vars: 5
    - Vars:
        - x[0]: m1 (float, default range (1.0,5.0))
        - x[1]: m2 (float, default range (1.0,5.0))
        - x[2]: r1 (float, default range (1.0,5.0))
        - x[3]: r2 (float, default range (1.0,5.0))
        - x[4]: G (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.13.12'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[4]*x[0]*x[1]*(1/x[3]-1/x[2])

    def eq_func(self, x):
        return x[4]*x[0]*x[1]*(1/x[3]-1/x[2])
  

@register_feynman_eq_class
class FeynmanICh14Eq3(KnownEquation):
    """
    - Equation: I.14.3
    - Raw: m*g*z
    - Num. Vars: 3
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: g (float, default range (1.0,5.0))
        - x[2]: z (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.14.3'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]

    def eq_func(self, x):
        return x[0]*x[1]*x[2]
  

@register_feynman_eq_class
class FeynmanICh14Eq4(KnownEquation):
    """
    - Equation: I.14.4
    - Raw: 1/2*k_spring*x**2
    - Num. Vars: 2
    - Vars:
        - x[0]: k_spring (float, default range (1.0,5.0))
        - x[1]: x (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.14.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/2*x[0]*x[1]**2

    def eq_func(self, x):
        return 1/2*x[0]*x[1]**2
  

@register_feynman_eq_class
class FeynmanICh15Eq3x(KnownEquation):
    """
    - Equation: I.15.3x
    - Raw: (x-u*t)/sqrt(1-u**2/c**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: x (float, default range (5.0,10.0))
        - x[1]: u (float, default range (1.0,2.0))
        - x[2]: c (float, default range (3.0,20.0))
        - x[3]: t (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-i.15.3x'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(5.0,10.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,20.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[0]-x[1]*x[3])/sympy.sqrt(1-x[1]**2/x[2]**2)

    def eq_func(self, x):
        return (x[0]-x[1]*x[3])/np.sqrt(1-x[1]**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanICh15Eq3t(KnownEquation):
    """
    - Equation: I.15.3t
    - Raw: (t-u*x/c**2)/sqrt(1-u**2/c**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: x (float, default range (1.0,5.0))
        - x[1]: c (float, default range (3.0,10.0))
        - x[2]: u (float, default range (1.0,2.0))
        - x[3]: t (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.15.3t'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[3]-x[2]*x[0]/x[1]**2)/sympy.sqrt(1-x[2]**2/x[1]**2)

    def eq_func(self, x):
        return (x[3]-x[2]*x[0]/x[1]**2)/np.sqrt(1-x[2]**2/x[1]**2)
  

@register_feynman_eq_class
class FeynmanICh15Eq10(KnownEquation):
    """
    - Equation: I.15.10
    - Raw: m_0*v/sqrt(1-v**2/c**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: m_0 (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: c (float, default range (3.0,10.0))
    """
    _eq_name = 'feynman-i.15.10'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/sympy.sqrt(1-x[1]**2/x[2]**2)

    def eq_func(self, x):
        return x[0]*x[1]/np.sqrt(1-x[1]**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanICh16Eq6(KnownEquation):
    """
    - Equation: I.16.6
    - Raw: (u+v)/(1+u*v/c**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: c (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,5.0))
        - x[2]: u (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.16.6'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[2]+x[1])/(1+x[2]*x[1]/x[0]**2)

    def eq_func(self, x):
        return (x[2]+x[1])/(1+x[2]*x[1]/x[0]**2)
  

@register_feynman_eq_class
class FeynmanICh18Eq4(KnownEquation):
    """
    - Equation: I.18.4
    - Raw: (m1*r1+m2*r2)/(m1+m2)
    - Num. Vars: 4
    - Vars:
        - x[0]: m1 (float, default range (1.0,5.0))
        - x[1]: m2 (float, default range (1.0,5.0))
        - x[2]: r1 (float, default range (1.0,5.0))
        - x[3]: r2 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.18.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[0]*x[2]+x[1]*x[3])/(x[0]+x[1])

    def eq_func(self, x):
        return (x[0]*x[2]+x[1]*x[3])/(x[0]+x[1])
  

@register_feynman_eq_class
class FeynmanICh18Eq12(KnownEquation):
    """
    - Equation: I.18.12
    - Raw: r*F*sin(theta)
    - Num. Vars: 3
    - Vars:
        - x[0]: r (float, default range (1.0,5.0))
        - x[1]: F (float, default range (1.0,5.0))
        - x[2]: theta (float, default range (0.0,5.0))
    """
    _eq_name = 'feynman-i.18.12'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(0.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*sympy.sin(x[2])

    def eq_func(self, x):
        return x[0]*x[1]*np.sin(x[2])
  

@register_feynman_eq_class
class FeynmanICh18Eq16(KnownEquation):
    """
    - Equation: I.18.16
    - Raw: m*r*v*sin(theta)
    - Num. Vars: 4
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: r (float, default range (1.0,5.0))
        - x[2]: v (float, default range (1.0,5.0))
        - x[3]: theta (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.18.16'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]*sympy.sin(x[3])

    def eq_func(self, x):
        return x[0]*x[1]*x[2]*np.sin(x[3])
  

@register_feynman_eq_class
class FeynmanICh24Eq6(KnownEquation):
    """
    - Equation: I.24.6
    - Raw: 1/2*m*(omega**2+omega_0**2)*1/2*x**2
    - Num. Vars: 4
    - Vars:
        - x[0]: m (float, default range (1.0,3.0))
        - x[1]: omega (float, default range (1.0,3.0))
        - x[2]: omega_0 (float, default range (1.0,3.0))
        - x[3]: x (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-i.24.6'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/2*x[0]*(x[1]**2+x[2]**2)*1/2*x[3]**2

    def eq_func(self, x):
        return 1/2*x[0]*(x[1]**2+x[2]**2)*1/2*x[3]**2
  

@register_feynman_eq_class
class FeynmanICh25Eq13(KnownEquation):
    """
    - Equation: I.25.13
    - Raw: q/C
    - Num. Vars: 2
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: C (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.25.13'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/x[1]

    def eq_func(self, x):
        return x[0]/x[1]
  

@register_feynman_eq_class
class FeynmanICh26Eq2(KnownEquation):
    """
    - Equation: I.26.2
    - Raw: arcsin(n*sin(theta2))
    - Num. Vars: 2
    - Vars:
        - x[0]: n (float, default range (0.0,1.0))
        - x[1]: theta2 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.26.2'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(0.0,1.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.asin(x[0]*sympy.sin(x[1]))

    def eq_func(self, x):
        return np.arcsin(x[0]*np.sin(x[1]))
  

@register_feynman_eq_class
class FeynmanICh27Eq6(KnownEquation):
    """
    - Equation: I.27.6
    - Raw: 1/(1/d1+n/d2)
    - Num. Vars: 3
    - Vars:
        - x[0]: d1 (float, default range (1.0,5.0))
        - x[1]: d2 (float, default range (1.0,5.0))
        - x[2]: n (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.27.6'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(1/x[0]+x[2]/x[1])

    def eq_func(self, x):
        return 1/(1/x[0]+x[2]/x[1])
  

@register_feynman_eq_class
class FeynmanICh29Eq4(KnownEquation):
    """
    - Equation: I.29.4
    - Raw: omega/c
    - Num. Vars: 2
    - Vars:
        - x[0]: omega (float, default range (1.0,10.0))
        - x[1]: c (float, default range (1.0,10.0))
    """
    _eq_name = 'feynman-i.29.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,10.0, uses_negative=False),
              SimpleSampling(1.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/x[1]

    def eq_func(self, x):
        return x[0]/x[1]
  

@register_feynman_eq_class
class FeynmanICh29Eq16(KnownEquation):
    """
    - Equation: I.29.16
    - Raw: sqrt(x1**2+x2**2-2*x1*x2*cos(theta1-theta2))
    - Num. Vars: 4
    - Vars:
        - x[0]: x1 (float, default range (1.0,5.0))
        - x[1]: x2 (float, default range (1.0,5.0))
        - x[2]: theta1 (float, default range (1.0,5.0))
        - x[3]: theta2 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.29.16'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0]**2+x[1]**2-2*x[0]*x[1]*sympy.cos(x[2]-x[3]))

    def eq_func(self, x):
        return np.sqrt(x[0]**2+x[1]**2-2*x[0]*x[1]*np.cos(x[2]-x[3]))
  

@register_feynman_eq_class
class FeynmanICh30Eq3(KnownEquation):
    """
    - Equation: I.30.3
    - Raw: Int_0*sin(n*theta/2)**2/sin(theta/2)**2
    - Num. Vars: 3
    - Vars:
        - x[0]: Int_0 (float, default range (1.0,5.0))
        - x[1]: theta (float, default range (1.0,5.0))
        - x[2]: n (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.30.3'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*sympy.sin(x[2]*x[1]/2)**2/sympy.sin(x[1]/2)**2

    def eq_func(self, x):
        return x[0]*np.sin(x[2]*x[1]/2)**2/np.sin(x[1]/2)**2
  

@register_feynman_eq_class
class FeynmanICh30Eq5(KnownEquation):
    """
    - Equation: I.30.5
    - Raw: arcsin(lambd/(n*d))
    - Num. Vars: 3
    - Vars:
        - x[0]: lambd (float, default range (1.0,2.0))
        - x[1]: d (float, default range (2.0,5.0))
        - x[2]: n (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.30.5'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(2.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.asin(x[0]/(x[2]*x[1]))

    def eq_func(self, x):
        return np.arcsin(x[0]/(x[2]*x[1]))
  

@register_feynman_eq_class
class FeynmanICh32Eq5(KnownEquation):
    """
    - Equation: I.32.5
    - Raw: q**2*a**2/(6*pi*epsilon*c**3)
    - Num. Vars: 4
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: a (float, default range (1.0,5.0))
        - x[2]: epsilon (float, default range (1.0,5.0))
        - x[3]: c (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.32.5'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]**2*x[1]**2/(6*sympy.pi*x[2]*x[3]**3)

    def eq_func(self, x):
        return x[0]**2*x[1]**2/(6*np.pi*x[2]*x[3]**3)
  

@register_feynman_eq_class
class FeynmanICh32Eq17(KnownEquation):
    """
    - Equation: I.32.17
    - Raw: (1/2*epsilon*c*Ef**2)*(8*pi*r**2/3)*(omega**4/(omega**2-omega_0**2)**2)
    - Num. Vars: 6
    - Vars:
        - x[0]: epsilon (float, default range (1.0,2.0))
        - x[1]: c (float, default range (1.0,2.0))
        - x[2]: Ef (float, default range (1.0,2.0))
        - x[3]: r (float, default range (1.0,2.0))
        - x[4]: omega (float, default range (1.0,2.0))
        - x[5]: omega_0 (float, default range (3.0,5.0))
    """
    _eq_name = 'feynman-i.32.17'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (1/2*x[0]*x[1]*x[2]**2)*(8*sympy.pi*x[3]**2/3)*(x[4]**4/(x[4]**2-x[5]**2)**2)

    def eq_func(self, x):
        return (1/2*x[0]*x[1]*x[2]**2)*(8*np.pi*x[3]**2/3)*(x[4]**4/(x[4]**2-x[5]**2)**2)
  

@register_feynman_eq_class
class FeynmanICh34Eq8(KnownEquation):
    """
    - Equation: I.34.8
    - Raw: q*v*B/p
    - Num. Vars: 4
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,5.0))
        - x[2]: B (float, default range (1.0,5.0))
        - x[3]: p (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.34.8'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]/x[3]

    def eq_func(self, x):
        return x[0]*x[1]*x[2]/x[3]
  

@register_feynman_eq_class
class FeynmanICh34Eq10(KnownEquation):
    """
    - Equation: I.34.10
    - Raw: omega_0/(1-v/c)
    - Num. Vars: 3
    - Vars:
        - x[0]: c (float, default range (3.0,10.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: omega_0 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.34.10'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(3.0,10.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[2]/(1-x[1]/x[0])

    def eq_func(self, x):
        return x[2]/(1-x[1]/x[0])
  

@register_feynman_eq_class
class FeynmanICh34Eq14(KnownEquation):
    """
    - Equation: I.34.14
    - Raw: (1+v/c)/sqrt(1-v**2/c**2)*omega_0
    - Num. Vars: 3
    - Vars:
        - x[0]: c (float, default range (3.0,10.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: omega_0 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.34.14'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(3.0,10.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (1+x[1]/x[0])/sympy.sqrt(1-x[1]**2/x[0]**2)*x[2]

    def eq_func(self, x):
        return (1+x[1]/x[0])/np.sqrt(1-x[1]**2/x[0]**2)*x[2]
  

@register_feynman_eq_class
class FeynmanICh34Eq27(KnownEquation):
    """
    - Equation: I.34.27
    - Raw: (h/(2*pi))*omega
    - Num. Vars: 2
    - Vars:
        - x[0]: omega (float, default range (1.0,5.0))
        - x[1]: h (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.34.27'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[1]/(2*sympy.pi))*x[0]

    def eq_func(self, x):
        return (x[1]/(2*np.pi))*x[0]
  

@register_feynman_eq_class
class FeynmanICh37Eq4(KnownEquation):
    """
    - Equation: I.37.4
    - Raw: I1+I2+2*sqrt(I1*I2)*cos(delta)
    - Num. Vars: 3
    - Vars:
        - x[0]: I1 (float, default range (1.0,5.0))
        - x[1]: I2 (float, default range (1.0,5.0))
        - x[2]: delta (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.37.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]+x[1]+2*sympy.sqrt(x[0]*x[1])*sympy.cos(x[2])

    def eq_func(self, x):
        return x[0]+x[1]+2*np.sqrt(x[0]*x[1])*np.cos(x[2])
  

@register_feynman_eq_class
class FeynmanICh38Eq12(KnownEquation):
    """
    - Equation: I.38.12
    - Raw: 4*pi*epsilon*(h/(2*pi))**2/(m*q**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: q (float, default range (1.0,5.0))
        - x[2]: h (float, default range (1.0,5.0))
        - x[3]: epsilon (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.38.12'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 4*sympy.pi*x[3]*(x[2]/(2*sympy.pi))**2/(x[0]*x[1]**2)

    def eq_func(self, x):
        return 4*np.pi*x[3]*(x[2]/(2*np.pi))**2/(x[0]*x[1]**2)
  

@register_feynman_eq_class
class FeynmanICh39Eq10(KnownEquation):
    """
    - Equation: I.39.10
    - Raw: 3/2*pr*V
    - Num. Vars: 2
    - Vars:
        - x[0]: pr (float, default range (1.0,5.0))
        - x[1]: V (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.39.10'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 3/2*x[0]*x[1]

    def eq_func(self, x):
        return 3/2*x[0]*x[1]
  

@register_feynman_eq_class
class FeynmanICh39Eq11(KnownEquation):
    """
    - Equation: I.39.11
    - Raw: 1/(gamma-1)*pr*V
    - Num. Vars: 3
    - Vars:
        - x[0]: gamma (float, default range (2.0,5.0))
        - x[1]: pr (float, default range (1.0,5.0))
        - x[2]: V (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.39.11'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(2.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(x[0]-1)*x[1]*x[2]

    def eq_func(self, x):
        return 1/(x[0]-1)*x[1]*x[2]
  

@register_feynman_eq_class
class FeynmanICh39Eq22(KnownEquation):
    """
    - Equation: I.39.22
    - Raw: n*kb*T/V
    - Num. Vars: 4
    - Vars:
        - x[0]: n (float, default range (1.0,5.0))
        - x[1]: T (float, default range (1.0,5.0))
        - x[2]: V (float, default range (1.0,5.0))
        - x[3]: kb (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.39.22'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[3]*x[1]/x[2]

    def eq_func(self, x):
        return x[0]*x[3]*x[1]/x[2]
  

@register_feynman_eq_class
class FeynmanICh40Eq1(KnownEquation):
    """
    - Equation: I.40.1
    - Raw: n_0*exp(-m*g*x/(kb*T))
    - Num. Vars: 6
    - Vars:
        - x[0]: n_0 (float, default range (1.0,5.0))
        - x[1]: m (float, default range (1.0,5.0))
        - x[2]: x (float, default range (1.0,5.0))
        - x[3]: T (float, default range (1.0,5.0))
        - x[4]: g (float, default range (1.0,5.0))
        - x[5]: kb (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.40.1'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*sympy.exp(-x[1]*x[4]*x[2]/(x[5]*x[3]))

    def eq_func(self, x):
        return x[0]*np.exp(-x[1]*x[4]*x[2]/(x[5]*x[3]))
  

@register_feynman_eq_class
class FeynmanICh41Eq16(KnownEquation):
    """
    - Equation: I.41.16
    - Raw: h/(2*pi)*omega**3/(pi**2*c**2*(exp((h/(2*pi))*omega/(kb*T))-1))
    - Num. Vars: 5
    - Vars:
        - x[0]: omega (float, default range (1.0,5.0))
        - x[1]: T (float, default range (1.0,5.0))
        - x[2]: h (float, default range (1.0,5.0))
        - x[3]: kb (float, default range (1.0,5.0))
        - x[4]: c (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.41.16'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[2]/(2*sympy.pi)*x[0]**3/(sympy.pi**2*x[4]**2*(sympy.exp((x[2]/(2*sympy.pi))*x[0]/(x[3]*x[1]))-1))

    def eq_func(self, x):
        return x[2]/(2*np.pi)*x[0]**3/(np.pi**2*x[4]**2*(np.exp((x[2]/(2*np.pi))*x[0]/(x[3]*x[1]))-1))
  

@register_feynman_eq_class
class FeynmanICh43Eq16(KnownEquation):
    """
    - Equation: I.43.16
    - Raw: mu_drift*q*Volt/d
    - Num. Vars: 4
    - Vars:
        - x[0]: mu_drift (float, default range (1.0,5.0))
        - x[1]: q (float, default range (1.0,5.0))
        - x[2]: Volt (float, default range (1.0,5.0))
        - x[3]: d (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.43.16'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]/x[3]

    def eq_func(self, x):
        return x[0]*x[1]*x[2]/x[3]
  

@register_feynman_eq_class
class FeynmanICh43Eq31(KnownEquation):
    """
    - Equation: I.43.31
    - Raw: mob*kb*T
    - Num. Vars: 3
    - Vars:
        - x[0]: mob (float, default range (1.0,5.0))
        - x[1]: T (float, default range (1.0,5.0))
        - x[2]: kb (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.43.31'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[2]*x[1]

    def eq_func(self, x):
        return x[0]*x[2]*x[1]
  

@register_feynman_eq_class
class FeynmanICh43Eq43(KnownEquation):
    """
    - Equation: I.43.43
    - Raw: 1/(gamma-1)*kb*v/A
    - Num. Vars: 4
    - Vars:
        - x[0]: gamma (float, default range (2.0,5.0))
        - x[1]: kb (float, default range (1.0,5.0))
        - x[2]: A (float, default range (1.0,5.0))
        - x[3]: v (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.43.43'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(2.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(x[0]-1)*x[1]*x[3]/x[2]

    def eq_func(self, x):
        return 1/(x[0]-1)*x[1]*x[3]/x[2]
  

@register_feynman_eq_class
class FeynmanICh44Eq4(KnownEquation):
    """
    - Equation: I.44.4
    - Raw: n*kb*T*ln(V2/V1)
    - Num. Vars: 5
    - Vars:
        - x[0]: n (float, default range (1.0,5.0))
        - x[1]: kb (float, default range (1.0,5.0))
        - x[2]: T (float, default range (1.0,5.0))
        - x[3]: V1 (float, default range (1.0,5.0))
        - x[4]: V2 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.44.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]*sympy.log(x[4]/x[3])

    def eq_func(self, x):
        return x[0]*x[1]*x[2]*np.log(x[4]/x[3])
  

@register_feynman_eq_class
class FeynmanICh47Eq23(KnownEquation):
    """
    - Equation: I.47.23
    - Raw: sqrt(gamma*pr/rho)
    - Num. Vars: 3
    - Vars:
        - x[0]: gamma (float, default range (1.0,5.0))
        - x[1]: pr (float, default range (1.0,5.0))
        - x[2]: rho (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-i.47.23'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0]*x[1]/x[2])

    def eq_func(self, x):
        return np.sqrt(x[0]*x[1]/x[2])
  

@register_feynman_eq_class
class FeynmanICh48Eq2(KnownEquation):
    """
    - Equation: I.48.2
    - Raw: m*c**2/sqrt(1-v**2/c**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: c (float, default range (3.0,10.0))
    """
    _eq_name = 'feynman-i.48.2'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[2]**2/sympy.sqrt(1-x[1]**2/x[2]**2)

    def eq_func(self, x):
        return x[0]*x[2]**2/np.sqrt(1-x[1]**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanICh50Eq26(KnownEquation):
    """
    - Equation: I.50.26
    - Raw: x1*(cos(omega*t)+alpha*cos(omega*t)**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: x1 (float, default range (1.0,3.0))
        - x[1]: omega (float, default range (1.0,3.0))
        - x[2]: t (float, default range (1.0,3.0))
        - x[3]: alpha (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-i.50.26'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(sympy.cos(x[1]*x[2])+x[3]*sympy.cos(x[1]*x[2])**2)

    def eq_func(self, x):
        return x[0]*(np.cos(x[1]*x[2])+x[3]*np.cos(x[1]*x[2])**2)
  

@register_feynman_eq_class
class FeynmanIICh2Eq42(KnownEquation):
    """
    - Equation: II.2.42
    - Raw: kappa*(T2-T1)*A/d
    - Num. Vars: 5
    - Vars:
        - x[0]: kappa (float, default range (1.0,5.0))
        - x[1]: T1 (float, default range (1.0,5.0))
        - x[2]: T2 (float, default range (1.0,5.0))
        - x[3]: A (float, default range (1.0,5.0))
        - x[4]: d (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.2.42'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(x[2]-x[1])*x[3]/x[4]

    def eq_func(self, x):
        return x[0]*(x[2]-x[1])*x[3]/x[4]
  

@register_feynman_eq_class
class FeynmanIICh3Eq24(KnownEquation):
    """
    - Equation: II.3.24
    - Raw: Pwr/(4*pi*r**2)
    - Num. Vars: 2
    - Vars:
        - x[0]: Pwr (float, default range (1.0,5.0))
        - x[1]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.3.24'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(4*sympy.pi*x[1]**2)

    def eq_func(self, x):
        return x[0]/(4*np.pi*x[1]**2)
  

@register_feynman_eq_class
class FeynmanIICh4Eq23(KnownEquation):
    """
    - Equation: II.4.23
    - Raw: q/(4*pi*epsilon*r)
    - Num. Vars: 3
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: epsilon (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.4.23'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(4*sympy.pi*x[1]*x[2])

    def eq_func(self, x):
        return x[0]/(4*np.pi*x[1]*x[2])
  

@register_feynman_eq_class
class FeynmanIICh6Eq11(KnownEquation):
    """
    - Equation: II.6.11
    - Raw: 1/(4*pi*epsilon)*p_d*cos(theta)/r**2
    - Num. Vars: 4
    - Vars:
        - x[0]: epsilon (float, default range (1.0,3.0))
        - x[1]: p_d (float, default range (1.0,3.0))
        - x[2]: theta (float, default range (1.0,3.0))
        - x[3]: r (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-ii.6.11'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(4*sympy.pi*x[0])*x[1]*sympy.cos(x[2])/x[3]**2

    def eq_func(self, x):
        return 1/(4*np.pi*x[0])*x[1]*np.cos(x[2])/x[3]**2
  

@register_feynman_eq_class
class FeynmanIICh6Eq15a(KnownEquation):
    """
    - Equation: II.6.15a
    - Raw: p_d/(4*pi*epsilon)*3*z/r**5*sqrt(x**2+y**2)
    - Num. Vars: 6
    - Vars:
        - x[0]: epsilon (float, default range (1.0,3.0))
        - x[1]: p_d (float, default range (1.0,3.0))
        - x[2]: r (float, default range (1.0,3.0))
        - x[3]: x (float, default range (1.0,3.0))
        - x[4]: y (float, default range (1.0,3.0))
        - x[5]: z (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-ii.6.15a'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[1]/(4*sympy.pi*x[0])*3*x[5]/x[2]**5*sympy.sqrt(x[3]**2+x[4]**2)

    def eq_func(self, x):
        return x[1]/(4*np.pi*x[0])*3*x[5]/x[2]**5*np.sqrt(x[3]**2+x[4]**2)
  

@register_feynman_eq_class
class FeynmanIICh6Eq15b(KnownEquation):
    """
    - Equation: II.6.15b
    - Raw: p_d/(4*pi*epsilon)*3*cos(theta)*sin(theta)/r**3
    - Num. Vars: 4
    - Vars:
        - x[0]: epsilon (float, default range (1.0,3.0))
        - x[1]: p_d (float, default range (1.0,3.0))
        - x[2]: theta (float, default range (1.0,3.0))
        - x[3]: r (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-ii.6.15b'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[1]/(4*sympy.pi*x[0])*3*sympy.cos(x[2])*sympy.sin(x[2])/x[3]**3

    def eq_func(self, x):
        return x[1]/(4*np.pi*x[0])*3*np.cos(x[2])*np.sin(x[2])/x[3]**3
  

@register_feynman_eq_class
class FeynmanIICh8Eq7(KnownEquation):
    """
    - Equation: II.8.7
    - Raw: 3/5*q**2/(4*pi*epsilon*d)
    - Num. Vars: 3
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: epsilon (float, default range (1.0,5.0))
        - x[2]: d (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.8.7'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 3/5*x[0]**2/(4*sympy.pi*x[1]*x[2])

    def eq_func(self, x):
        return 3/5*x[0]**2/(4*np.pi*x[1]*x[2])
  

@register_feynman_eq_class
class FeynmanIICh8Eq31(KnownEquation):
    """
    - Equation: II.8.31
    - Raw: epsilon*Ef**2/2
    - Num. Vars: 2
    - Vars:
        - x[0]: epsilon (float, default range (1.0,5.0))
        - x[1]: Ef (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.8.31'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]**2/2

    def eq_func(self, x):
        return x[0]*x[1]**2/2
  

@register_feynman_eq_class
class FeynmanIICh10Eq9(KnownEquation):
    """
    - Equation: II.10.9
    - Raw: sigma_den/epsilon*1/(1+chi)
    - Num. Vars: 3
    - Vars:
        - x[0]: sigma_den (float, default range (1.0,5.0))
        - x[1]: epsilon (float, default range (1.0,5.0))
        - x[2]: chi (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.10.9'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/x[1]*1/(1+x[2])

    def eq_func(self, x):
        return x[0]/x[1]*1/(1+x[2])
  

@register_feynman_eq_class
class FeynmanIICh11Eq3(KnownEquation):
    """
    - Equation: II.11.3
    - Raw: q*Ef/(m*(omega_0**2-omega**2))
    - Num. Vars: 5
    - Vars:
        - x[0]: q (float, default range (1.0,3.0))
        - x[1]: Ef (float, default range (1.0,3.0))
        - x[2]: m (float, default range (1.0,3.0))
        - x[3]: omega_0 (float, default range (3.0,5.0))
        - x[4]: omega (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-ii.11.3'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(3.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/(x[2]*(x[3]**2-x[4]**2))

    def eq_func(self, x):
        return x[0]*x[1]/(x[2]*(x[3]**2-x[4]**2))
  

@register_feynman_eq_class
class FeynmanIICh11Eq17(KnownEquation):
    """
    - Equation: II.11.17
    - Raw: n_0*(1+p_d*Ef*cos(theta)/(kb*T))
    - Num. Vars: 6
    - Vars:
        - x[0]: n_0 (float, default range (1.0,3.0))
        - x[1]: kb (float, default range (1.0,3.0))
        - x[2]: T (float, default range (1.0,3.0))
        - x[3]: theta (float, default range (1.0,3.0))
        - x[4]: p_d (float, default range (1.0,3.0))
        - x[5]: Ef (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-ii.11.17'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(1+x[4]*x[5]*sympy.cos(x[3])/(x[1]*x[2]))

    def eq_func(self, x):
        return x[0]*(1+x[4]*x[5]*np.cos(x[3])/(x[1]*x[2]))
  

@register_feynman_eq_class
class FeynmanIICh11Eq20(KnownEquation):
    """
    - Equation: II.11.20
    - Raw: n_rho*p_d**2*Ef/(3*kb*T)
    - Num. Vars: 5
    - Vars:
        - x[0]: n_rho (float, default range (1.0,5.0))
        - x[1]: p_d (float, default range (1.0,5.0))
        - x[2]: Ef (float, default range (1.0,5.0))
        - x[3]: kb (float, default range (1.0,5.0))
        - x[4]: T (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.11.20'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]**2*x[2]/(3*x[3]*x[4])

    def eq_func(self, x):
        return x[0]*x[1]**2*x[2]/(3*x[3]*x[4])
  

@register_feynman_eq_class
class FeynmanIICh11Eq27(KnownEquation):
    """
    - Equation: II.11.27
    - Raw: n*alpha/(1-(n*alpha/3))*epsilon*Ef
    - Num. Vars: 4
    - Vars:
        - x[0]: n (float, default range (0.0,1.0))
        - x[1]: alpha (float, default range (0.0,1.0))
        - x[2]: epsilon (float, default range (1.0,2.0))
        - x[3]: Ef (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-ii.11.27'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(0.0,1.0, uses_negative=False),
              SimpleSampling(0.0,1.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/(1-(x[0]*x[1]/3))*x[2]*x[3]

    def eq_func(self, x):
        return x[0]*x[1]/(1-(x[0]*x[1]/3))*x[2]*x[3]
  

@register_feynman_eq_class
class FeynmanIICh11Eq28(KnownEquation):
    """
    - Equation: II.11.28
    - Raw: 1+n*alpha/(1-(n*alpha/3))
    - Num. Vars: 2
    - Vars:
        - x[0]: n (float, default range (0.0,1.0))
        - x[1]: alpha (float, default range (0.0,1.0))
    """
    _eq_name = 'feynman-ii.11.28'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(0.0,1.0, uses_negative=False),
              SimpleSampling(0.0,1.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1+x[0]*x[1]/(1-(x[0]*x[1]/3))

    def eq_func(self, x):
        return 1+x[0]*x[1]/(1-(x[0]*x[1]/3))
  

@register_feynman_eq_class
class FeynmanIICh13Eq17(KnownEquation):
    """
    - Equation: II.13.17
    - Raw: 1/(4*pi*epsilon*c**2)*2*I/r
    - Num. Vars: 4
    - Vars:
        - x[0]: epsilon (float, default range (1.0,5.0))
        - x[1]: c (float, default range (1.0,5.0))
        - x[2]: I (float, default range (1.0,5.0))
        - x[3]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.13.17'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(4*sympy.pi*x[0]*x[1]**2)*2*x[2]/x[3]

    def eq_func(self, x):
        return 1/(4*np.pi*x[0]*x[1]**2)*2*x[2]/x[3]
  

@register_feynman_eq_class
class FeynmanIICh13Eq23(KnownEquation):
    """
    - Equation: II.13.23
    - Raw: rho_c_0/sqrt(1-v**2/c**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: rho_c_0 (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: c (float, default range (3.0,10.0))
    """
    _eq_name = 'feynman-ii.13.23'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/sympy.sqrt(1-x[1]**2/x[2]**2)

    def eq_func(self, x):
        return x[0]/np.sqrt(1-x[1]**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanIICh13Eq34(KnownEquation):
    """
    - Equation: II.13.34
    - Raw: rho_c_0*v/sqrt(1-v**2/c**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: rho_c_0 (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,2.0))
        - x[2]: c (float, default range (3.0,10.0))
    """
    _eq_name = 'feynman-ii.13.34'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/sympy.sqrt(1-x[1]**2/x[2]**2)

    def eq_func(self, x):
        return x[0]*x[1]/np.sqrt(1-x[1]**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanIICh15Eq4(KnownEquation):
    """
    - Equation: II.15.4
    - Raw: -mom*B*cos(theta)
    - Num. Vars: 3
    - Vars:
        - x[0]: mom (float, default range (1.0,5.0))
        - x[1]: B (float, default range (1.0,5.0))
        - x[2]: theta (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.15.4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = -x[0]*x[1]*sympy.cos(x[2])

    def eq_func(self, x):
        return -x[0]*x[1]*np.cos(x[2])
  

@register_feynman_eq_class
class FeynmanIICh15Eq5(KnownEquation):
    """
    - Equation: II.15.5
    - Raw: -p_d*Ef*cos(theta)
    - Num. Vars: 3
    - Vars:
        - x[0]: p_d (float, default range (1.0,5.0))
        - x[1]: Ef (float, default range (1.0,5.0))
        - x[2]: theta (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.15.5'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = -x[0]*x[1]*sympy.cos(x[2])

    def eq_func(self, x):
        return -x[0]*x[1]*np.cos(x[2])
  

@register_feynman_eq_class
class FeynmanIICh21Eq32(KnownEquation):
    """
    - Equation: II.21.32
    - Raw: q/(4*pi*epsilon*r*(1-v/c))
    - Num. Vars: 5
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: epsilon (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
        - x[3]: v (float, default range (1.0,2.0))
        - x[4]: c (float, default range (3.0,10.0))
    """
    _eq_name = 'feynman-ii.21.32'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(3.0,10.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(4*sympy.pi*x[1]*x[2]*(1-x[3]/x[4]))

    def eq_func(self, x):
        return x[0]/(4*np.pi*x[1]*x[2]*(1-x[3]/x[4]))
  

@register_feynman_eq_class
class FeynmanIICh24Eq17(KnownEquation):
    """
    - Equation: II.24.17
    - Raw: sqrt(omega**2/c**2-pi**2/d**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: omega (float, default range (4.0,6.0))
        - x[1]: c (float, default range (1.0,2.0))
        - x[2]: d (float, default range (2.0,4.0))
    """
    _eq_name = 'feynman-ii.24.17'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(4.0,6.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(2.0,4.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(x[0]**2/x[1]**2-sympy.pi**2/x[2]**2)

    def eq_func(self, x):
        return np.sqrt(x[0]**2/x[1]**2-np.pi**2/x[2]**2)
  

@register_feynman_eq_class
class FeynmanIICh27Eq16(KnownEquation):
    """
    - Equation: II.27.16
    - Raw: epsilon*c*Ef**2
    - Num. Vars: 3
    - Vars:
        - x[0]: epsilon (float, default range (1.0,5.0))
        - x[1]: c (float, default range (1.0,5.0))
        - x[2]: Ef (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.27.16'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]**2

    def eq_func(self, x):
        return x[0]*x[1]*x[2]**2
  

@register_feynman_eq_class
class FeynmanIICh27Eq18(KnownEquation):
    """
    - Equation: II.27.18
    - Raw: epsilon*Ef**2
    - Num. Vars: 2
    - Vars:
        - x[0]: epsilon (float, default range (1.0,5.0))
        - x[1]: Ef (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.27.18'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]**2

    def eq_func(self, x):
        return x[0]*x[1]**2
  

@register_feynman_eq_class
class FeynmanIICh34Eq2a(KnownEquation):
    """
    - Equation: II.34.2a
    - Raw: q*v/(2*pi*r)
    - Num. Vars: 3
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.34.2a'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/(2*sympy.pi*x[2])

    def eq_func(self, x):
        return x[0]*x[1]/(2*np.pi*x[2])
  

@register_feynman_eq_class
class FeynmanIICh34Eq2(KnownEquation):
    """
    - Equation: II.34.2
    - Raw: q*v*r/2
    - Num. Vars: 3
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: v (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.34.2'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]/2

    def eq_func(self, x):
        return x[0]*x[1]*x[2]/2
  

@register_feynman_eq_class
class FeynmanIICh34Eq11(KnownEquation):
    """
    - Equation: II.34.11
    - Raw: g_*q*B/(2*m)
    - Num. Vars: 4
    - Vars:
        - x[0]: g_ (float, default range (1.0,5.0))
        - x[1]: q (float, default range (1.0,5.0))
        - x[2]: B (float, default range (1.0,5.0))
        - x[3]: m (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.34.11'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[2]/(2*x[3])

    def eq_func(self, x):
        return x[0]*x[1]*x[2]/(2*x[3])
  

@register_feynman_eq_class
class FeynmanIICh34Eq29a(KnownEquation):
    """
    - Equation: II.34.29a
    - Raw: q*h/(4*pi*m)
    - Num. Vars: 3
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: h (float, default range (1.0,5.0))
        - x[2]: m (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.34.29a'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/(4*sympy.pi*x[2])

    def eq_func(self, x):
        return x[0]*x[1]/(4*np.pi*x[2])
  

@register_feynman_eq_class
class FeynmanIICh34Eq29b(KnownEquation):
    """
    - Equation: II.34.29b
    - Raw: g_*mom*B*Jz/(h/(2*pi))
    - Num. Vars: 5
    - Vars:
        - x[0]: g_ (float, default range (1.0,5.0))
        - x[1]: h (float, default range (1.0,5.0))
        - x[2]: Jz (float, default range (1.0,5.0))
        - x[3]: mom (float, default range (1.0,5.0))
        - x[4]: B (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.34.29b'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[3]*x[4]*x[2]/(x[1]/(2*sympy.pi))

    def eq_func(self, x):
        return x[0]*x[3]*x[4]*x[2]/(x[1]/(2*np.pi))
  

@register_feynman_eq_class
class FeynmanIICh35Eq18(KnownEquation):
    """
    - Equation: II.35.18
    - Raw: n_0/(exp(mom*B/(kb*T))+exp(-mom*B/(kb*T)))
    - Num. Vars: 5
    - Vars:
        - x[0]: n_0 (float, default range (1.0,3.0))
        - x[1]: kb (float, default range (1.0,3.0))
        - x[2]: T (float, default range (1.0,3.0))
        - x[3]: mom (float, default range (1.0,3.0))
        - x[4]: B (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-ii.35.18'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(sympy.exp(x[3]*x[4]/(x[1]*x[2]))+sympy.exp(-x[3]*x[4]/(x[1]*x[2])))

    def eq_func(self, x):
        return x[0]/(np.exp(x[3]*x[4]/(x[1]*x[2]))+np.exp(-x[3]*x[4]/(x[1]*x[2])))
  

@register_feynman_eq_class
class FeynmanIICh35Eq21(KnownEquation):
    """
    - Equation: II.35.21
    - Raw: n_rho*mom*tanh(mom*B/(kb*T))
    - Num. Vars: 5
    - Vars:
        - x[0]: n_rho (float, default range (1.0,5.0))
        - x[1]: mom (float, default range (1.0,5.0))
        - x[2]: B (float, default range (1.0,5.0))
        - x[3]: kb (float, default range (1.0,5.0))
        - x[4]: T (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.35.21'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*sympy.tanh(x[1]*x[2]/(x[3]*x[4]))

    def eq_func(self, x):
        return x[0]*x[1]*np.tanh(x[1]*x[2]/(x[3]*x[4]))
  

@register_feynman_eq_class
class FeynmanIICh36Eq38(KnownEquation):
    """
    - Equation: II.36.38
    - Raw: mom*H/(kb*T)+(mom*alpha)/(epsilon*c**2*kb*T)*M
    - Num. Vars: 8
    - Vars:
        - x[0]: mom (float, default range (1.0,3.0))
        - x[1]: H (float, default range (1.0,3.0))
        - x[2]: kb (float, default range (1.0,3.0))
        - x[3]: T (float, default range (1.0,3.0))
        - x[4]: alpha (float, default range (1.0,3.0))
        - x[5]: epsilon (float, default range (1.0,3.0))
        - x[6]: c (float, default range (1.0,3.0))
        - x[7]: M (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-ii.36.38'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=8, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/(x[2]*x[3])+(x[0]*x[4])/(x[5]*x[6]**2*x[2]*x[3])*x[7]

    def eq_func(self, x):
        return x[0]*x[1]/(x[2]*x[3])+(x[0]*x[4])/(x[5]*x[6]**2*x[2]*x[3])*x[7]
  

@register_feynman_eq_class
class FeynmanIICh37Eq1(KnownEquation):
    """
    - Equation: II.37.1
    - Raw: mom*(1+chi)*B
    - Num. Vars: 3
    - Vars:
        - x[0]: mom (float, default range (1.0,5.0))
        - x[1]: B (float, default range (1.0,5.0))
        - x[2]: chi (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.37.1'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(1+x[2])*x[1]

    def eq_func(self, x):
        return x[0]*(1+x[2])*x[1]
  

@register_feynman_eq_class
class FeynmanIICh38Eq3(KnownEquation):
    """
    - Equation: II.38.3
    - Raw: Y*A*x/d
    - Num. Vars: 4
    - Vars:
        - x[0]: Y (float, default range (1.0,5.0))
        - x[1]: A (float, default range (1.0,5.0))
        - x[2]: d (float, default range (1.0,5.0))
        - x[3]: x (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.38.3'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]*x[3]/x[2]

    def eq_func(self, x):
        return x[0]*x[1]*x[3]/x[2]
  

@register_feynman_eq_class
class FeynmanIICh38Eq14(KnownEquation):
    """
    - Equation: II.38.14
    - Raw: Y/(2*(1+sigma))
    - Num. Vars: 2
    - Vars:
        - x[0]: Y (float, default range (1.0,5.0))
        - x[1]: sigma (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-ii.38.14'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(2*(1+x[1]))

    def eq_func(self, x):
        return x[0]/(2*(1+x[1]))
  

@register_feynman_eq_class
class FeynmanIIICh4Eq32(KnownEquation):
    """
    - Equation: III.4.32
    - Raw: 1/(exp((h/(2*pi))*omega/(kb*T))-1)
    - Num. Vars: 4
    - Vars:
        - x[0]: h (float, default range (1.0,5.0))
        - x[1]: omega (float, default range (1.0,5.0))
        - x[2]: kb (float, default range (1.0,5.0))
        - x[3]: T (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.4.32'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(sympy.exp((x[0]/(2*sympy.pi))*x[1]/(x[2]*x[3]))-1)

    def eq_func(self, x):
        return 1/(np.exp((x[0]/(2*np.pi))*x[1]/(x[2]*x[3]))-1)
  

@register_feynman_eq_class
class FeynmanIIICh4Eq33(KnownEquation):
    """
    - Equation: III.4.33
    - Raw: (h/(2*pi))*omega/(exp((h/(2*pi))*omega/(kb*T))-1)
    - Num. Vars: 4
    - Vars:
        - x[0]: h (float, default range (1.0,5.0))
        - x[1]: omega (float, default range (1.0,5.0))
        - x[2]: kb (float, default range (1.0,5.0))
        - x[3]: T (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.4.33'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[0]/(2*sympy.pi))*x[1]/(sympy.exp((x[0]/(2*sympy.pi))*x[1]/(x[2]*x[3]))-1)

    def eq_func(self, x):
        return (x[0]/(2*np.pi))*x[1]/(np.exp((x[0]/(2*np.pi))*x[1]/(x[2]*x[3]))-1)
  

@register_feynman_eq_class
class FeynmanIIICh7Eq38(KnownEquation):
    """
    - Equation: III.7.38
    - Raw: 2*mom*B/(h/(2*pi))
    - Num. Vars: 3
    - Vars:
        - x[0]: mom (float, default range (1.0,5.0))
        - x[1]: B (float, default range (1.0,5.0))
        - x[2]: h (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.7.38'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 2*x[0]*x[1]/(x[2]/(2*sympy.pi))

    def eq_func(self, x):
        return 2*x[0]*x[1]/(x[2]/(2*np.pi))
  

@register_feynman_eq_class
class FeynmanIIICh8Eq54(KnownEquation):
    """
    - Equation: III.8.54
    - Raw: sin(E_n*t/(h/(2*pi)))**2
    - Num. Vars: 3
    - Vars:
        - x[0]: E_n (float, default range (1.0,2.0))
        - x[1]: t (float, default range (1.0,2.0))
        - x[2]: h (float, default range (1.0,4.0))
    """
    _eq_name = 'feynman-iii.8.54'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,4.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sin(x[0]*x[1]/(x[2]/(2*sympy.pi)))**2

    def eq_func(self, x):
        return np.sin(x[0]*x[1]/(x[2]/(2*np.pi)))**2
  

@register_feynman_eq_class
class FeynmanIIICh9Eq52(KnownEquation):
    """
    - Equation: III.9.52
    - Raw: (p_d*Ef*t/(h/(2*pi)))*sin((omega-omega_0)*t/2)**2/((omega-omega_0)*t/2)**2
    - Num. Vars: 6
    - Vars:
        - x[0]: p_d (float, default range (1.0,3.0))
        - x[1]: Ef (float, default range (1.0,3.0))
        - x[2]: t (float, default range (1.0,3.0))
        - x[3]: h (float, default range (1.0,3.0))
        - x[4]: omega (float, default range (1.0,5.0))
        - x[5]: omega_0 (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.9.52'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[0]*x[1]*x[2]/(x[3]/(2*sympy.pi)))*sympy.sin((x[4]-x[5])*x[2]/2)**2/((x[4]-x[5])*x[2]/2)**2

    def eq_func(self, x):
        return (x[0]*x[1]*x[2]/(x[3]/(2*np.pi)))*np.sin((x[4]-x[5])*x[2]/2)**2/((x[4]-x[5])*x[2]/2)**2
  

@register_feynman_eq_class
class FeynmanIIICh10Eq19(KnownEquation):
    """
    - Equation: III.10.19
    - Raw: mom*sqrt(Bx**2+By**2+Bz**2)
    - Num. Vars: 4
    - Vars:
        - x[0]: mom (float, default range (1.0,5.0))
        - x[1]: Bx (float, default range (1.0,5.0))
        - x[2]: By (float, default range (1.0,5.0))
        - x[3]: Bz (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.10.19'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*sympy.sqrt(x[1]**2+x[2]**2+x[3]**2)

    def eq_func(self, x):
        return x[0]*np.sqrt(x[1]**2+x[2]**2+x[3]**2)
  

@register_feynman_eq_class
class FeynmanIIICh12Eq43(KnownEquation):
    """
    - Equation: III.12.43
    - Raw: n*(h/(2*pi))
    - Num. Vars: 2
    - Vars:
        - x[0]: n (float, default range (1.0,5.0))
        - x[1]: h (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.12.43'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=2, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(x[1]/(2*sympy.pi))

    def eq_func(self, x):
        return x[0]*(x[1]/(2*np.pi))
  

@register_feynman_eq_class
class FeynmanIIICh13Eq18(KnownEquation):
    """
    - Equation: III.13.18
    - Raw: 2*E_n*d**2*k/(h/(2*pi))
    - Num. Vars: 4
    - Vars:
        - x[0]: E_n (float, default range (1.0,5.0))
        - x[1]: d (float, default range (1.0,5.0))
        - x[2]: k (float, default range (1.0,5.0))
        - x[3]: h (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.13.18'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 2*x[0]*x[1]**2*x[2]/(x[3]/(2*sympy.pi))

    def eq_func(self, x):
        return 2*x[0]*x[1]**2*x[2]/(x[3]/(2*np.pi))
  

@register_feynman_eq_class
class FeynmanIIICh14Eq14(KnownEquation):
    """
    - Equation: III.14.14
    - Raw: I_0*(exp(q*Volt/(kb*T))-1)
    - Num. Vars: 5
    - Vars:
        - x[0]: I_0 (float, default range (1.0,5.0))
        - x[1]: q (float, default range (1.0,2.0))
        - x[2]: Volt (float, default range (1.0,2.0))
        - x[3]: kb (float, default range (1.0,2.0))
        - x[4]: T (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-iii.14.14'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(sympy.exp(x[1]*x[2]/(x[3]*x[4]))-1)

    def eq_func(self, x):
        return x[0]*(np.exp(x[1]*x[2]/(x[3]*x[4]))-1)
  

@register_feynman_eq_class
class FeynmanIIICh15Eq12(KnownEquation):
    """
    - Equation: III.15.12
    - Raw: 2*U*(1-cos(k*d))
    - Num. Vars: 3
    - Vars:
        - x[0]: U (float, default range (1.0,5.0))
        - x[1]: k (float, default range (1.0,5.0))
        - x[2]: d (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.15.12'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 2*x[0]*(1-sympy.cos(x[1]*x[2]))

    def eq_func(self, x):
        return 2*x[0]*(1-np.cos(x[1]*x[2]))
  

@register_feynman_eq_class
class FeynmanIIICh15Eq14(KnownEquation):
    """
    - Equation: III.15.14
    - Raw: (h/(2*pi))**2/(2*E_n*d**2)
    - Num. Vars: 3
    - Vars:
        - x[0]: h (float, default range (1.0,5.0))
        - x[1]: E_n (float, default range (1.0,5.0))
        - x[2]: d (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.15.14'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[0]/(2*sympy.pi))**2/(2*x[1]*x[2]**2)

    def eq_func(self, x):
        return (x[0]/(2*np.pi))**2/(2*x[1]*x[2]**2)
  

@register_feynman_eq_class
class FeynmanIIICh15Eq27(KnownEquation):
    """
    - Equation: III.15.27
    - Raw: 2*pi*alpha/(n*d)
    - Num. Vars: 3
    - Vars:
        - x[0]: alpha (float, default range (1.0,5.0))
        - x[1]: n (float, default range (1.0,5.0))
        - x[2]: d (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.15.27'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 2*sympy.pi*x[0]/(x[1]*x[2])

    def eq_func(self, x):
        return 2*np.pi*x[0]/(x[1]*x[2])
  

@register_feynman_eq_class
class FeynmanIIICh17Eq37(KnownEquation):
    """
    - Equation: III.17.37
    - Raw: beta*(1+alpha*cos(theta))
    - Num. Vars: 3
    - Vars:
        - x[0]: beta (float, default range (1.0,5.0))
        - x[1]: alpha (float, default range (1.0,5.0))
        - x[2]: theta (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.17.37'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(1+x[1]*sympy.cos(x[2]))

    def eq_func(self, x):
        return x[0]*(1+x[1]*np.cos(x[2]))
  

@register_feynman_eq_class
class FeynmanIIICh19Eq51(KnownEquation):
    """
    - Equation: III.19.51
    - Raw: -m*q**4/(2*(4*pi*epsilon)**2*(h/(2*pi))**2)*(1/n**2)
    - Num. Vars: 5
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: q (float, default range (1.0,5.0))
        - x[2]: h (float, default range (1.0,5.0))
        - x[3]: n (float, default range (1.0,5.0))
        - x[4]: epsilon (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.19.51'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = -x[0]*x[1]**4/(2*(4*sympy.pi*x[4])**2*(x[2]/(2*sympy.pi))**2)*(1/x[3]**2)

    def eq_func(self, x):
        return -x[0]*x[1]**4/(2*(4*np.pi*x[4])**2*(x[2]/(2*np.pi))**2)*(1/x[3]**2)
  

@register_feynman_eq_class
class FeynmanIIICh21Eq20(KnownEquation):
    """
    - Equation: III.21.20
    - Raw: -rho_c_0*q*A_vec/m
    - Num. Vars: 4
    - Vars:
        - x[0]: rho_c_0 (float, default range (1.0,5.0))
        - x[1]: q (float, default range (1.0,5.0))
        - x[2]: A_vec (float, default range (1.0,5.0))
        - x[3]: m (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-iii.21.20'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = -x[0]*x[1]*x[2]/x[3]

    def eq_func(self, x):
        return -x[0]*x[1]*x[2]/x[3]
  

@register_feynman_eq_class
class FeynmanBonus1(KnownEquation):
    """
    - Equation: test_1
    - Raw: (Z_1*Z_2*alpha*hbar*c/(4*E_n*sin(theta/2)**2))**2
    - Num. Vars: 7
    - Vars:
        - x[0]: Z_1 (float, default range (1.0,2.0))
        - x[1]: Z_2 (float, default range (1.0,2.0))
        - x[2]: alpha (float, default range (1.0,2.0))
        - x[3]: hbar (float, default range (1.0,2.0))
        - x[4]: c (float, default range (1.0,2.0))
        - x[5]: E_n (float, default range (1.0,3.0))
        - x[6]: theta (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_1'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=7, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = (x[0]*x[1]*x[2]*x[3]*x[4]/(4*x[5]*sympy.sin(x[6]/2)**2))**2

    def eq_func(self, x):
        return (x[0]*x[1]*x[2]*x[3]*x[4]/(4*x[5]*np.sin(x[6]/2)**2))**2
  

@register_feynman_eq_class
class FeynmanBonus2(KnownEquation):
    """
    - Equation: test_2
    - Raw: m*k_G/L**2*(1+sqrt(1+2*E_n*L**2/(m*k_G**2))*cos(theta1-theta2))
    - Num. Vars: 6
    - Vars:
        - x[0]: m (float, default range (1.0,3.0))
        - x[1]: k_G (float, default range (1.0,3.0))
        - x[2]: L (float, default range (1.0,3.0))
        - x[3]: E_n (float, default range (1.0,3.0))
        - x[4]: theta1 (float, default range (0.0,6.0))
        - x[5]: theta2 (float, default range (0.0,6.0))
    """
    _eq_name = 'feynman-test_2'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(0.0,6.0, uses_negative=False),
              SimpleSampling(0.0,6.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*x[1]/x[2]**2*(1+sympy.sqrt(1+2*x[3]*x[2]**2/(x[0]*x[1]**2))*sympy.cos(x[4]-x[5]))

    def eq_func(self, x):
        return x[0]*x[1]/x[2]**2*(1+np.sqrt(1+2*x[3]*x[2]**2/(x[0]*x[1]**2))*np.cos(x[4]-x[5]))
  

@register_feynman_eq_class
class FeynmanBonus3(KnownEquation):
    """
    - Equation: test_3
    - Raw: d*(1-alpha**2)/(1+alpha*cos(theta1-theta2))
    - Num. Vars: 4
    - Vars:
        - x[0]: d (float, default range (1.0,3.0))
        - x[1]: alpha (float, default range (2.0,4.0))
        - x[2]: theta1 (float, default range (4.0,5.0))
        - x[3]: theta2 (float, default range (4.0,5.0))
    """
    _eq_name = 'feynman-test_3'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(2.0,4.0, uses_negative=False),
              SimpleSampling(4.0,5.0, uses_negative=False),
              SimpleSampling(4.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(1-x[1]**2)/(1+x[1]*sympy.cos(x[2]-x[3]))

    def eq_func(self, x):
        return x[0]*(1-x[1]**2)/(1+x[1]*np.cos(x[2]-x[3]))
  

@register_feynman_eq_class
class FeynmanBonus4(KnownEquation):
    """
    - Equation: test_4
    - Raw: sqrt(2/m*(E_n-U-L**2/(2*m*r**2)))
    - Num. Vars: 5
    - Vars:
        - x[0]: m (float, default range (1.0,3.0))
        - x[1]: E_n (float, default range (8.0,12.0))
        - x[2]: U (float, default range (1.0,3.0))
        - x[3]: L (float, default range (1.0,3.0))
        - x[4]: r (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_4'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(8.0,12.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(2/x[0]*(x[1]-x[2]-x[3]**2/(2*x[0]*x[4]**2)))

    def eq_func(self, x):
        return np.sqrt(2/x[0]*(x[1]-x[2]-x[3]**2/(2*x[0]*x[4]**2)))
  

@register_feynman_eq_class
class FeynmanBonus5(KnownEquation):
    """
    - Equation: test_5
    - Raw: 2*pi*d**(3/2)/sqrt(G*(m1+m2))
    - Num. Vars: 4
    - Vars:
        - x[0]: d (float, default range (1.0,3.0))
        - x[1]: G (float, default range (1.0,3.0))
        - x[2]: m1 (float, default range (1.0,3.0))
        - x[3]: m2 (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_5'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 2*sympy.pi*x[0]**(3/2)/sympy.sqrt(x[1]*(x[2]+x[3]))

    def eq_func(self, x):
        return 2*np.pi*x[0]**(3/2)/np.sqrt(x[1]*(x[2]+x[3]))
  

@register_feynman_eq_class
class FeynmanBonus6(KnownEquation):
    """
    - Equation: test_6
    - Raw: sqrt(1+2*epsilon**2*E_n*L**2/(m*(Z_1*Z_2*q**2)**2))
    - Num. Vars: 7
    - Vars:
        - x[0]: epsilon (float, default range (1.0,3.0))
        - x[1]: L (float, default range (1.0,3.0))
        - x[2]: m (float, default range (1.0,3.0))
        - x[3]: Z_1 (float, default range (1.0,3.0))
        - x[4]: Z_2 (float, default range (1.0,3.0))
        - x[5]: q (float, default range (1.0,3.0))
        - x[6]: E_n (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_6'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=7, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(1+2*x[0]**2*x[6]*x[1]**2/(x[2]*(x[3]*x[4]*x[5]**2)**2))

    def eq_func(self, x):
        return np.sqrt(1+2*x[0]**2*x[6]*x[1]**2/(x[2]*(x[3]*x[4]*x[5]**2)**2))
  

@register_feynman_eq_class
class FeynmanBonus7(KnownEquation):
    """
    - Equation: test_7
    - Raw: sqrt(8*pi*G*rho/3-alpha*c**2/d**2)
    - Num. Vars: 5
    - Vars:
        - x[0]: G (float, default range (1.0,3.0))
        - x[1]: rho (float, default range (1.0,3.0))
        - x[2]: alpha (float, default range (1.0,2.0))
        - x[3]: c (float, default range (1.0,2.0))
        - x[4]: d (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_7'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(8*sympy.pi*x[0]*x[1]/3-x[2]*x[3]**2/x[4]**2)

    def eq_func(self, x):
        return np.sqrt(8*np.pi*x[0]*x[1]/3-x[2]*x[3]**2/x[4]**2)
  

@register_feynman_eq_class
class FeynmanBonus8(KnownEquation):
    """
    - Equation: test_8
    - Raw: E_n/(1+E_n/(m*c**2)*(1-cos(theta)))
    - Num. Vars: 4
    - Vars:
        - x[0]: E_n (float, default range (1.0,3.0))
        - x[1]: m (float, default range (1.0,3.0))
        - x[2]: c (float, default range (1.0,3.0))
        - x[3]: theta (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_8'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(1+x[0]/(x[1]*x[2]**2)*(1-sympy.cos(x[3])))

    def eq_func(self, x):
        return x[0]/(1+x[0]/(x[1]*x[2]**2)*(1-np.cos(x[3])))
  

@register_feynman_eq_class
class FeynmanBonus9(KnownEquation):
    """
    - Equation: test_9
    - Raw: -32/5*G**4/c**5*(m1*m2)**2*(m1+m2)/r**5
    - Num. Vars: 5
    - Vars:
        - x[0]: G (float, default range (1.0,2.0))
        - x[1]: c (float, default range (1.0,2.0))
        - x[2]: m1 (float, default range (1.0,5.0))
        - x[3]: m2 (float, default range (1.0,5.0))
        - x[4]: r (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-test_9'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = -32/5*x[0]**4/x[1]**5*(x[2]*x[3])**2*(x[2]+x[3])/x[4]**5

    def eq_func(self, x):
        return -32/5*x[0]**4/x[1]**5*(x[2]*x[3])**2*(x[2]+x[3])/x[4]**5
  

@register_feynman_eq_class
class FeynmanBonus10(KnownEquation):
    """
    - Equation: test_10
    - Raw: arccos((cos(theta2)-v/c)/(1-v/c*cos(theta2)))
    - Num. Vars: 3
    - Vars:
        - x[0]: c (float, default range (4.0,6.0))
        - x[1]: v (float, default range (1.0,3.0))
        - x[2]: theta2 (float, default range (1.0,3.0))
    """
    _eq_name = 'feynman-test_10'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(4.0,6.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False)
            ]

        super().__init__(num_vars=3, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.acos((sympy.cos(x[2])-x[1]/x[0])/(1-x[1]/x[0]*sympy.cos(x[2])))

    def eq_func(self, x):
        return np.arccos((np.cos(x[2])-x[1]/x[0])/(1-x[1]/x[0]*np.cos(x[2])))
  

@register_feynman_eq_class
class FeynmanBonus11(KnownEquation):
    """
    - Equation: test_11
    - Raw: I_0*(sin(alpha/2)*sin(n*delta/2)/(alpha/2*sin(delta/2)))**2
    - Num. Vars: 4
    - Vars:
        - x[0]: I_0 (float, default range (1.0,3.0))
        - x[1]: alpha (float, default range (1.0,3.0))
        - x[2]: delta (float, default range (1.0,3.0))
        - x[3]: n (float, default range (1.0,2.0))
    """
    _eq_name = 'feynman-test_11'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,2.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*(sympy.sin(x[1]/2)*sympy.sin(x[3]*x[2]/2)/(x[1]/2*sympy.sin(x[2]/2)))**2

    def eq_func(self, x):
        return x[0]*(np.sin(x[1]/2)*np.sin(x[3]*x[2]/2)/(x[1]/2*np.sin(x[2]/2)))**2
  

@register_feynman_eq_class
class FeynmanBonus12(KnownEquation):
    """
    - Equation: test_12
    - Raw: q/(4*pi*epsilon*y**2)*(4*pi*epsilon*Volt*d-q*d*y**3/(y**2-d**2)**2)
    - Num. Vars: 5
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: y (float, default range (1.0,3.0))
        - x[2]: Volt (float, default range (1.0,5.0))
        - x[3]: d (float, default range (4.0,6.0))
        - x[4]: epsilon (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_12'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(4.0,6.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]/(4*sympy.pi*x[4]*x[1]**2)*(4*sympy.pi*x[4]*x[2]*x[3]-x[0]*x[3]*x[1]**3/(x[1]**2-x[3]**2)**2)

    def eq_func(self, x):
        return x[0]/(4*np.pi*x[4]*x[1]**2)*(4*np.pi*x[4]*x[2]*x[3]-x[0]*x[3]*x[1]**3/(x[1]**2-x[3]**2)**2)
  

@register_feynman_eq_class
class FeynmanBonus13(KnownEquation):
    """
    - Equation: test_13
    - Raw: 1/(4*pi*epsilon)*q/sqrt(r**2+d**2-2*r*d*cos(alpha))
    - Num. Vars: 5
    - Vars:
        - x[0]: q (float, default range (1.0,5.0))
        - x[1]: r (float, default range (1.0,3.0))
        - x[2]: d (float, default range (4.0,6.0))
        - x[3]: alpha (float, default range (0.0,6.0))
        - x[4]: epsilon (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_13'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(4.0,6.0, uses_negative=False),
              SimpleSampling(0.0,6.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(4*sympy.pi*x[4])*x[0]/sympy.sqrt(x[1]**2+x[2]**2-2*x[1]*x[2]*sympy.cos(x[3]))

    def eq_func(self, x):
        return 1/(4*np.pi*x[4])*x[0]/np.sqrt(x[1]**2+x[2]**2-2*x[1]*x[2]*np.cos(x[3]))
  

@register_feynman_eq_class
class FeynmanBonus14(KnownEquation):
    """
    - Equation: test_14
    - Raw: Ef*cos(theta)*(-r+d**3/r**2*(alpha-1)/(alpha+2))
    - Num. Vars: 5
    - Vars:
        - x[0]: Ef (float, default range (1.0,5.0))
        - x[1]: theta (float, default range (0.0,6.0))
        - x[2]: r (float, default range (1.0,5.0))
        - x[3]: d (float, default range (1.0,5.0))
        - x[4]: alpha (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_14'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(0.0,6.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = x[0]*sympy.cos(x[1])*(-x[2]+x[3]**3/x[2]**2*(x[4]-1)/(x[4]+2))

    def eq_func(self, x):
        return x[0]*np.cos(x[1])*(-x[2]+x[3]**3/x[2]**2*(x[4]-1)/(x[4]+2))
  

@register_feynman_eq_class
class FeynmanBonus15(KnownEquation):
    """
    - Equation: test_15
    - Raw: sqrt(1-v**2/c**2)*omega/(1+v/c*cos(theta))
    - Num. Vars: 4
    - Vars:
        - x[0]: c (float, default range (5.0,20.0))
        - x[1]: v (float, default range (1.0,3.0))
        - x[2]: omega (float, default range (1.0,5.0))
        - x[3]: theta (float, default range (0.0,6.0))
    """
    _eq_name = 'feynman-test_15'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(5.0,20.0, uses_negative=False),
              SimpleSampling(1.0,3.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(0.0,6.0, uses_negative=False)
            ]

        super().__init__(num_vars=4, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt(1-x[1]**2/x[0]**2)*x[2]/(1+x[1]/x[0]*sympy.cos(x[3]))

    def eq_func(self, x):
        return np.sqrt(1-x[1]**2/x[0]**2)*x[2]/(1+x[1]/x[0]*np.cos(x[3]))
  

@register_feynman_eq_class
class FeynmanBonus16(KnownEquation):
    """
    - Equation: test_16
    - Raw: sqrt((p-q*A_vec)**2*c**2+m**2*c**4)+q*Volt
    - Num. Vars: 6
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: c (float, default range (1.0,5.0))
        - x[2]: p (float, default range (1.0,5.0))
        - x[3]: q (float, default range (1.0,5.0))
        - x[4]: A_vec (float, default range (1.0,5.0))
        - x[5]: Volt (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_16'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = sympy.sqrt((x[2]-x[3]*x[4])**2*x[1]**2+x[0]**2*x[1]**4)+x[3]*x[5]

    def eq_func(self, x):
        return np.sqrt((x[2]-x[3]*x[4])**2*x[1]**2+x[0]**2*x[1]**4)+x[3]*x[5]
  

@register_feynman_eq_class
class FeynmanBonus17(KnownEquation):
    """
    - Equation: test_17
    - Raw: 1/(2*m)*(p**2+m**2*omega**2*x**2*(1+alpha*x/y))
    - Num. Vars: 6
    - Vars:
        - x[0]: m (float, default range (1.0,5.0))
        - x[1]: omega (float, default range (1.0,5.0))
        - x[2]: p (float, default range (1.0,5.0))
        - x[3]: y (float, default range (1.0,5.0))
        - x[4]: x (float, default range (1.0,5.0))
        - x[5]: alpha (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_17'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(2*x[0])*(x[2]**2+x[0]**2*x[1]**2*x[4]**2*(1+x[5]*x[4]/x[3]))

    def eq_func(self, x):
        return 1/(2*x[0])*(x[2]**2+x[0]**2*x[1]**2*x[4]**2*(1+x[5]*x[4]/x[3]))
  

@register_feynman_eq_class
class FeynmanBonus18(KnownEquation):
    """
    - Equation: test_18
    - Raw: 3/(8*pi*G)*(c**2*k_f/r**2+H_G**2)
    - Num. Vars: 5
    - Vars:
        - x[0]: G (float, default range (1.0,5.0))
        - x[1]: k_f (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
        - x[3]: H_G (float, default range (1.0,5.0))
        - x[4]: c (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_18'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=5, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 3/(8*sympy.pi*x[0])*(x[4]**2*x[1]/x[2]**2+x[3]**2)

    def eq_func(self, x):
        return 3/(8*np.pi*x[0])*(x[4]**2*x[1]/x[2]**2+x[3]**2)
  

@register_feynman_eq_class
class FeynmanBonus19(KnownEquation):
    """
    - Equation: test_19
    - Raw: -1/(8*pi*G)*(c**4*k_f/r**2+H_G**2*c**2*(1-2*alpha))
    - Num. Vars: 6
    - Vars:
        - x[0]: G (float, default range (1.0,5.0))
        - x[1]: k_f (float, default range (1.0,5.0))
        - x[2]: r (float, default range (1.0,5.0))
        - x[3]: H_G (float, default range (1.0,5.0))
        - x[4]: alpha (float, default range (1.0,5.0))
        - x[5]: c (float, default range (1.0,5.0))
    """
    _eq_name = 'feynman-test_19'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False)
            ]

        super().__init__(num_vars=6, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = -1/(8*sympy.pi*x[0])*(x[5]**4*x[1]/x[2]**2+x[3]**2*x[5]**2*(1-2*x[4]))

    def eq_func(self, x):
        return -1/(8*np.pi*x[0])*(x[5]**4*x[1]/x[2]**2+x[3]**2*x[5]**2*(1-2*x[4]))
  

@register_feynman_eq_class
class FeynmanBonus20(KnownEquation):
    """
    - Equation: test_20
    - Raw: 1/(4*pi)*alpha**2*h**2/(m**2*c**2)*(omega_0/omega)**2*(omega_0/omega+omega/omega_0-sin(beta)**2)
    - Num. Vars: 7
    - Vars:
        - x[0]: omega (float, default range (1.0,5.0))
        - x[1]: omega_0 (float, default range (1.0,5.0))
        - x[2]: alpha (float, default range (1.0,5.0))
        - x[3]: h (float, default range (1.0,5.0))
        - x[4]: m (float, default range (1.0,5.0))
        - x[5]: c (float, default range (1.0,5.0))
        - x[6]: beta (float, default range (0.0,6.0))
    """
    _eq_name = 'feynman-test_20'

    def __init__(self, sampling_objs=None):
        if sampling_objs is None:
            sampling_objs = [
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(1.0,5.0, uses_negative=False),
              SimpleSampling(0.0,6.0, uses_negative=False)
            ]

        super().__init__(num_vars=7, sampling_objs=sampling_objs)
        x = self.x
        self.sympy_eq = 1/(4*sympy.pi)*x[2]**2*x[3]**2/(x[4]**2*x[5]**2)*(x[1]/x[0])**2*(x[1]/x[0]+x[0]/x[1]-sympy.sin(x[6])**2)

    def eq_func(self, x):
        return 1/(4*np.pi)*x[2]**2*x[3]**2/(x[4]**2*x[5]**2)*(x[1]/x[0])**2*(x[1]/x[0]+x[0]/x[1]-np.sin(x[6])**2)
  