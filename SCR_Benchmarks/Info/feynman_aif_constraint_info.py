AIF_EQUATION_CONSTRAINTS = [
  {'EquationName': 'FeynmanICh6Eq20a', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-sqrt(2)*x0*exp(-x0**2/2)/(2*sqrt(pi))', 'derivative_formatted': '-sqrt(2)*x0*exp(-x0**2/2)/(2*sqrt(pi))'
      }
    ], 'Variables': ['theta'
    ]
  },
  {'EquationName': 'FeynmanICh6Eq20', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'sigma', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-sqrt(2)*exp(-x1**2/(2*x0**2))/(2*sqrt(pi)*x0**2) + sqrt(2)*x1**2*exp(-x1**2/(2*x0**2))/(2*sqrt(pi)*x0**4)', 'derivative_formatted': '-sqrt(2)*exp(-x1**2/(2*x0**2))/(2*sqrt(pi)*x0**2) + sqrt(2)*x1**2*exp(-x1**2/(2*x0**2))/(2*sqrt(pi)*x0**4)'
      },
      {'var_name': 'x1', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-sqrt(2)*x1*exp(-x1**2/(2*x0**2))/(2*sqrt(pi)*x0**3)', 'derivative_formatted': '-sqrt(2)*x1*exp(-x1**2/(2*x0**2))/(2*sqrt(pi)*x0**3)'
      }
    ], 'Variables': ['sigma', 'theta'
    ]
  },
  {'EquationName': 'FeynmanICh6Eq20b', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'sigma', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-sqrt(2)*exp(-(x1 - x2)**2/(2*x0**2))/(2*sqrt(pi)*x0**2) + sqrt(2)*(x1 - x2)**2*exp(-(x1 - x2)**2/(2*x0**2))/(2*sqrt(pi)*x0**4)', 'derivative_formatted': '-sqrt(2)*exp(-(x1 - x2)**2/(2*x0**2))/(2*sqrt(pi)*x0**2) + sqrt(2)*(x1 - x2)**2*exp(-(x1 - x2)**2/(2*x0**2))/(2*sqrt(pi)*x0**4)'
      },
      {'var_name': 'x1', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-sqrt(2)*(2*x1 - 2*x2)*exp(-(x1 - x2)**2/(2*x0**2))/(4*sqrt(pi)*x0**3)', 'derivative_formatted': '-sqrt(2)*(2*x1 - 2*x2)*exp(-(x1 - x2)**2/(2*x0**2))/(4*sqrt(pi)*x0**3)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-sqrt(2)*(-2*x1 + 2*x2)*exp(-(x1 - x2)**2/(2*x0**2))/(4*sqrt(pi)*x0**3)', 'derivative_formatted': '-sqrt(2)*(-2*x1 + 2*x2)*exp(-(x1 - x2)**2/(2*x0**2))/(4*sqrt(pi)*x0**3)'
      }
    ], 'Variables': ['sigma', 'theta', 'theta1'
    ]
  },
  {'EquationName': 'FeynmanICh8Eq14', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'x1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(x0 - x1)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)', 'derivative_formatted': '(x0 - x1)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'x2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(-x0 + x1)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)', 'derivative_formatted': '(-x0 + x1)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'y1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(x2 - x3)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)', 'derivative_formatted': '(x2 - x3)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'y2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(-x2 + x3)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)', 'derivative_formatted': '(-x2 + x3)/sqrt((-x0 + x1)**2 + (-x2 + x3)**2)'
      }
    ], 'Variables': ['x1', 'x2', 'y1', 'y2'
    ]
  },
  {'EquationName': 'FeynmanICh9Eq18', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)', 'derivative_formatted': 'x1*x2/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'm2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)', 'derivative_formatted': 'x0*x2/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)', 'derivative_formatted': 'x0*x1/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'x1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*x1*x2*(-2*x3 + 2*x4)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2', 'derivative_formatted': 'x0*x1*x2*(-2*x3 + 2*x4)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2'
      },
      {'var_name': 'x4', 'var_display_name': 'x2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2*(2*x3 - 2*x4)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2', 'derivative_formatted': 'x0*x1*x2*(2*x3 - 2*x4)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2'
      },
      {'var_name': 'x5', 'var_display_name': 'y1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*x1*x2*(-2*x5 + 2*x6)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2', 'derivative_formatted': 'x0*x1*x2*(-2*x5 + 2*x6)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2'
      },
      {'var_name': 'x6', 'var_display_name': 'y2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2*(2*x5 - 2*x6)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2', 'derivative_formatted': 'x0*x1*x2*(2*x5 - 2*x6)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2'
      },
      {'var_name': 'x7', 'var_display_name': 'z1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*x1*x2*(-2*x7 + 2*x8)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2', 'derivative_formatted': 'x0*x1*x2*(-2*x7 + 2*x8)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2'
      },
      {'var_name': 'x8', 'var_display_name': 'z2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2*(2*x7 - 2*x8)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2', 'derivative_formatted': 'x0*x1*x2*(2*x7 - 2*x8)/((-x3 + x4)**2 + (-x5 + x6)**2 + (-x7 + x8)**2)**2'
      }
    ], 'Variables': ['m1', 'm2', 'G', 'x1', 'x2', 'y1', 'y2', 'z1', 'z2'
    ]
  },
  {'EquationName': 'FeynmanICh10Eq7', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': '1/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/(x2**2*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': 'x0*x1/(x2**2*(-x1**2/x2**2 + 1)**(3/2))'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2/(x2**3*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': '-x0*x1**2/(x2**3*(-x1**2/x2**2 + 1)**(3/2))'
      }
    ], 'Variables': ['m_0', 'v', 'c'
    ]
  },
  {'EquationName': 'FeynmanICh11Eq19', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'x1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x3', 'derivative_formatted': 'x3'
      },
      {'var_name': 'x1', 'var_display_name': 'x2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x4', 'derivative_formatted': 'x4'
      },
      {'var_name': 'x2', 'var_display_name': 'x3', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x5', 'derivative_formatted': 'x5'
      },
      {'var_name': 'x3', 'var_display_name': 'y1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0', 'derivative_formatted': 'x0'
      },
      {'var_name': 'x4', 'var_display_name': 'y2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1', 'derivative_formatted': 'x1'
      },
      {'var_name': 'x5', 'var_display_name': 'y3', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2', 'derivative_formatted': 'x2'
      }
    ], 'Variables': ['x1', 'x2', 'x3', 'y1', 'y2', 'y3'
    ]
  },
  {'EquationName': 'FeynmanICh12Eq1', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mu', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1', 'derivative_formatted': 'x1'
      },
      {'var_name': 'x1', 'var_display_name': 'Nn', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0', 'derivative_formatted': 'x0'
      }
    ], 'Variables': ['mu', 'Nn'
    ]
  },
  {'EquationName': 'FeynmanICh12Eq2', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(4*pi*x2*x3**2)', 'derivative_formatted': 'x1/(4*pi*x2*x3**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'q2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(4*pi*x2*x3**2)', 'derivative_formatted': 'x0/(4*pi*x2*x3**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(4*pi*x2**2*x3**2)', 'derivative_formatted': '-x0*x1/(4*pi*x2**2*x3**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(2*pi*x2*x3**3)', 'derivative_formatted': '-x0*x1/(2*pi*x2*x3**3)'
      }
    ], 'Variables': ['q1', 'q2', 'epsilon', 'r'
    ]
  },
  {'EquationName': 'FeynmanICh12Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(4*pi*x1*x2**2)', 'derivative_formatted': '1/(4*pi*x1*x2**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(4*pi*x1**2*x2**2)', 'derivative_formatted': '-x0/(4*pi*x1**2*x2**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(2*pi*x1*x2**3)', 'derivative_formatted': '-x0/(2*pi*x1*x2**3)'
      }
    ], 'Variables': ['q1', 'epsilon', 'r'
    ]
  },
  {'EquationName': 'FeynmanICh12Eq5', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1', 'derivative_formatted': 'x1'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0', 'derivative_formatted': 'x0'
      }
    ], 'Variables': ['q2', 'Ef'
    ]
  },
  {'EquationName': 'FeynmanICh12Eq11', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1 + x2*x3*sin(x4)', 'derivative_formatted': 'x1 + x2*x3*sin(x4)'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0', 'derivative_formatted': 'x0'
      },
      {'var_name': 'x2', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x3*sin(x4)', 'derivative_formatted': 'x0*x3*sin(x4)'
      },
      {'var_name': 'x3', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x2*sin(x4)', 'derivative_formatted': 'x0*x2*sin(x4)'
      },
      {'var_name': 'x4', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x2*x3*cos(x4)', 'derivative_formatted': 'x0*x2*x3*cos(x4)'
      }
    ], 'Variables': ['q', 'Ef', 'B', 'v', 'theta'
    ]
  },
  {'EquationName': 'FeynmanICh13Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.5*x1**2 + 0.5*x2**2 + 0.5*x3**2', 'derivative_formatted': '0.5*x1**2 + 0.5*x2**2 + 0.5*x3**2'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.0*x0*x1', 'derivative_formatted': '1.0*x0*x1'
      },
      {'var_name': 'x2', 'var_display_name': 'u', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.0*x0*x2', 'derivative_formatted': '1.0*x0*x2'
      },
      {'var_name': 'x3', 'var_display_name': 'w', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.0*x0*x3', 'derivative_formatted': '1.0*x0*x3'
      }
    ], 'Variables': ['m', 'v', 'u', 'w'
    ]
  },
  {'EquationName': 'FeynmanICh13Eq12', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*x4*(1/x3 - 1/x2)', 'derivative_formatted': 'x1*x4*(1/x3 - 1/x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'm2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x4*(1/x3 - 1/x2)', 'derivative_formatted': 'x0*x4*(1/x3 - 1/x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'r1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x4/x2**2', 'derivative_formatted': 'x0*x1*x4/x2**2'
      },
      {'var_name': 'x3', 'var_display_name': 'r2', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x4/x3**2', 'derivative_formatted': '-x0*x1*x4/x3**2'
      },
      {'var_name': 'x4', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*(1/x3 - 1/x2)', 'derivative_formatted': 'x0*x1*(1/x3 - 1/x2)'
      }
    ], 'Variables': ['m1', 'm2', 'r1', 'r2', 'G'
    ]
  },
  {'EquationName': 'FeynmanICh14Eq3', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2', 'derivative_formatted': 'x1*x2'
      },
      {'var_name': 'x1', 'var_display_name': 'g', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2', 'derivative_formatted': 'x0*x2'
      },
      {'var_name': 'x2', 'var_display_name': 'z', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1', 'derivative_formatted': 'x0*x1'
      }
    ], 'Variables': ['m', 'g', 'z'
    ]
  },
  {'EquationName': 'FeynmanICh14Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'k_spring', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.5*x1**2', 'derivative_formatted': '0.5*x1**2'
      },
      {'var_name': 'x1', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.0*x0*x1', 'derivative_formatted': '1.0*x0*x1'
      }
    ], 'Variables': ['k_spring', 'x'
    ]
  },
  {'EquationName': 'FeynmanICh15Eq3x', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': '1/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'u', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*(x0 - x1*x3)/(x2**2*(-x1**2/x2**2 + 1)**(3/2)) - x3/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': 'x1*(x0 - x1*x3)/(x2**2*(-x1**2/x2**2 + 1)**(3/2)) - x3/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1**2*(x0 - x1*x3)/(x2**3*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': '-x1**2*(x0 - x1*x3)/(x2**3*(-x1**2/x2**2 + 1)**(3/2))'
      },
      {'var_name': 'x3', 'var_display_name': 't', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': '-x1/sqrt(-x1**2/x2**2 + 1)'
      }
    ], 'Variables': ['x', 'u', 'c', 't'
    ]
  },
  {'EquationName': 'FeynmanICh15Eq3t', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x2/(x1**2*sqrt(1 - x2**2/x1**2))', 'derivative_formatted': '-x2/(x1**2*sqrt(1 - x2**2/x1**2))'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '2*x0*x2/(x1**3*sqrt(1 - x2**2/x1**2)) - x2**2*(-x0*x2/x1**2 + x3)/(x1**3*(1 - x2**2/x1**2)**(3/2))', 'derivative_formatted': '2*x0*x2/(x1**3*sqrt(1 - x2**2/x1**2)) - x2**2*(-x0*x2/x1**2 + x3)/(x1**3*(1 - x2**2/x1**2)**(3/2))'
      },
      {'var_name': 'x2', 'var_display_name': 'u', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0/(x1**2*sqrt(1 - x2**2/x1**2)) + x2*(-x0*x2/x1**2 + x3)/(x1**2*(1 - x2**2/x1**2)**(3/2))', 'derivative_formatted': '-x0/(x1**2*sqrt(1 - x2**2/x1**2)) + x2*(-x0*x2/x1**2 + x3)/(x1**2*(1 - x2**2/x1**2)**(3/2))'
      },
      {'var_name': 'x3', 'var_display_name': 't', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/sqrt(1 - x2**2/x1**2)', 'derivative_formatted': '1/sqrt(1 - x2**2/x1**2)'
      }
    ], 'Variables': ['x', 'c', 'u', 't'
    ]
  },
  {'EquationName': 'FeynmanICh15Eq10', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': 'x1/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2/(x2**2*(-x1**2/x2**2 + 1)**(3/2)) + x0/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': 'x0*x1**2/(x2**2*(-x1**2/x2**2 + 1)**(3/2)) + x0/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**3/(x2**3*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': '-x0*x1**3/(x2**3*(-x1**2/x2**2 + 1)**(3/2))'
      }
    ], 'Variables': ['m_0', 'v', 'c'
    ]
  },
  {'EquationName': 'FeynmanICh16Eq6', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x1*x2*(x1 + x2)/(x0**3*(1 + x1*x2/x0**2)**2)', 'derivative_formatted': '2*x1*x2*(x1 + x2)/(x0**3*(1 + x1*x2/x0**2)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '1/(1 + x1*x2/x0**2) - x2*(x1 + x2)/(x0**2*(1 + x1*x2/x0**2)**2)', 'derivative_formatted': '1/(1 + x1*x2/x0**2) - x2*(x1 + x2)/(x0**2*(1 + x1*x2/x0**2)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'u', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '1/(1 + x1*x2/x0**2) - x1*(x1 + x2)/(x0**2*(1 + x1*x2/x0**2)**2)', 'derivative_formatted': '1/(1 + x1*x2/x0**2) - x1*(x1 + x2)/(x0**2*(1 + x1*x2/x0**2)**2)'
      }
    ], 'Variables': ['c', 'v', 'u'
    ]
  },
  {'EquationName': 'FeynmanICh18Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x2/(x0 + x1) - (x0*x2 + x1*x3)/(x0 + x1)**2', 'derivative_formatted': 'x2/(x0 + x1) - (x0*x2 + x1*x3)/(x0 + x1)**2'
      },
      {'var_name': 'x1', 'var_display_name': 'm2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x3/(x0 + x1) - (x0*x2 + x1*x3)/(x0 + x1)**2', 'derivative_formatted': 'x3/(x0 + x1) - (x0*x2 + x1*x3)/(x0 + x1)**2'
      },
      {'var_name': 'x2', 'var_display_name': 'r1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(x0 + x1)', 'derivative_formatted': 'x0/(x0 + x1)'
      },
      {'var_name': 'x3', 'var_display_name': 'r2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(x0 + x1)', 'derivative_formatted': 'x1/(x0 + x1)'
      }
    ], 'Variables': ['m1', 'm2', 'r1', 'r2'
    ]
  },
  {'EquationName': 'FeynmanICh18Eq12', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*sin(x2)', 'derivative_formatted': 'x1*sin(x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'F', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*sin(x2)', 'derivative_formatted': 'x0*sin(x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*cos(x2)', 'derivative_formatted': 'x0*x1*cos(x2)'
      }
    ], 'Variables': ['r', 'F', 'theta'
    ]
  },
  {'EquationName': 'FeynmanICh18Eq16', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*x2*sin(x3)', 'derivative_formatted': 'x1*x2*sin(x3)'
      },
      {'var_name': 'x1', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x2*sin(x3)', 'derivative_formatted': 'x0*x2*sin(x3)'
      },
      {'var_name': 'x2', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*sin(x3)', 'derivative_formatted': 'x0*x1*sin(x3)'
      },
      {'var_name': 'x3', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*x2*cos(x3)', 'derivative_formatted': 'x0*x1*x2*cos(x3)'
      }
    ], 'Variables': ['m', 'r', 'v', 'theta'
    ]
  },
  {'EquationName': 'FeynmanICh24Eq6', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.25*x3**2*(x1**2 + x2**2)', 'derivative_formatted': '0.25*x3**2*(x1**2 + x2**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.5*x0*x1*x3**2', 'derivative_formatted': '0.5*x0*x1*x3**2'
      },
      {'var_name': 'x2', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.5*x0*x2*x3**2', 'derivative_formatted': '0.5*x0*x2*x3**2'
      },
      {'var_name': 'x3', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.5*x0*x3*(x1**2 + x2**2)', 'derivative_formatted': '0.5*x0*x3*(x1**2 + x2**2)'
      }
    ], 'Variables': ['m', 'omega', 'omega_0', 'x'
    ]
  },
  {'EquationName': 'FeynmanICh25Eq13', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/x1', 'derivative_formatted': '1/x1'
      },
      {'var_name': 'x1', 'var_display_name': 'C', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/x1**2', 'derivative_formatted': '-x0/x1**2'
      }
    ], 'Variables': ['q', 'C'
    ]
  },
  {'EquationName': 'FeynmanICh26Eq2', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'sin(x1)/sqrt(-x0**2*sin(x1)**2 + 1)', 'derivative_formatted': 'sin(x1)/sqrt(-x0**2*sin(x1)**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'theta2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*cos(x1)/sqrt(-x0**2*sin(x1)**2 + 1)', 'derivative_formatted': 'x0*cos(x1)/sqrt(-x0**2*sin(x1)**2 + 1)'
      }
    ], 'Variables': ['n', 'theta2'
    ]
  },
  {'EquationName': 'FeynmanICh27Eq6', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'd1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(x0**2*(x2/x1 + 1/x0)**2)', 'derivative_formatted': '1/(x0**2*(x2/x1 + 1/x0)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'd2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2/(x1**2*(x2/x1 + 1/x0)**2)', 'derivative_formatted': 'x2/(x1**2*(x2/x1 + 1/x0)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-1/(x1*(x2/x1 + 1/x0)**2)', 'derivative_formatted': '-1/(x1*(x2/x1 + 1/x0)**2)'
      }
    ], 'Variables': ['d1', 'd2', 'n'
    ]
  },
  {'EquationName': 'FeynmanICh29Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/x1', 'derivative_formatted': '1/x1'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/x1**2', 'derivative_formatted': '-x0/x1**2'
      }
    ], 'Variables': ['omega', 'c'
    ]
  },
  {'EquationName': 'FeynmanICh29Eq16', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'x1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(x0 - x1*cos(x2 - x3))/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)', 'derivative_formatted': '(x0 - x1*cos(x2 - x3))/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'x2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(-x0*cos(x2 - x3) + x1)/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)', 'derivative_formatted': '(-x0*cos(x2 - x3) + x1)/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*sin(x2 - x3)/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)', 'derivative_formatted': 'x0*x1*sin(x2 - x3)/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'theta2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x1*sin(x2 - x3)/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)', 'derivative_formatted': '-x0*x1*sin(x2 - x3)/sqrt(x0**2 - 2*x0*x1*cos(x2 - x3) + x1**2)'
      }
    ], 'Variables': ['x1', 'x2', 'theta1', 'theta2'
    ]
  },
  {'EquationName': 'FeynmanICh30Eq3', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'Int_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sin(x1*x2/2)**2/sin(x1/2)**2', 'derivative_formatted': 'sin(x1*x2/2)**2/sin(x1/2)**2'
      },
      {'var_name': 'x1', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x2*sin(x1*x2/2)*cos(x1*x2/2)/sin(x1/2)**2 - x0*sin(x1*x2/2)**2*cos(x1/2)/sin(x1/2)**3', 'derivative_formatted': 'x0*x2*sin(x1*x2/2)*cos(x1*x2/2)/sin(x1/2)**2 - x0*sin(x1*x2/2)**2*cos(x1/2)/sin(x1/2)**3'
      },
      {'var_name': 'x2', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*sin(x1*x2/2)*cos(x1*x2/2)/sin(x1/2)**2', 'derivative_formatted': 'x0*x1*sin(x1*x2/2)*cos(x1*x2/2)/sin(x1/2)**2'
      }
    ], 'Variables': ['Int_0', 'theta', 'n'
    ]
  },
  {'EquationName': 'FeynmanICh30Eq5', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'lambd', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(x1*x2*sqrt(-x0**2/(x1**2*x2**2) + 1))', 'derivative_formatted': '1/(x1*x2*sqrt(-x0**2/(x1**2*x2**2) + 1))'
      },
      {'var_name': 'x1', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(x1**2*x2*sqrt(-x0**2/(x1**2*x2**2) + 1))', 'derivative_formatted': '-x0/(x1**2*x2*sqrt(-x0**2/(x1**2*x2**2) + 1))'
      },
      {'var_name': 'x2', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(x1*x2**2*sqrt(-x0**2/(x1**2*x2**2) + 1))', 'derivative_formatted': '-x0/(x1*x2**2*sqrt(-x0**2/(x1**2*x2**2) + 1))'
      }
    ], 'Variables': ['lambd', 'd', 'n'
    ]
  },
  {'EquationName': 'FeynmanICh32Eq5', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2/(3*pi*x2*x3**3)', 'derivative_formatted': 'x0*x1**2/(3*pi*x2*x3**3)'
      },
      {'var_name': 'x1', 'var_display_name': 'a', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1/(3*pi*x2*x3**3)', 'derivative_formatted': 'x0**2*x1/(3*pi*x2*x3**3)'
      },
      {'var_name': 'x2', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*x1**2/(6*pi*x2**2*x3**3)', 'derivative_formatted': '-x0**2*x1**2/(6*pi*x2**2*x3**3)'
      },
      {'var_name': 'x3', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*x1**2/(2*pi*x2*x3**4)', 'derivative_formatted': '-x0**2*x1**2/(2*pi*x2*x3**4)'
      }
    ], 'Variables': ['q', 'a', 'epsilon', 'c'
    ]
  },
  {'EquationName': 'FeynmanICh32Eq17', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.33333333333333*pi*x1*x2**2*x3**2*x4**4/(x4**2 - x5**2)**2', 'derivative_formatted': '1.33333333333333*pi*x1*x2**2*x3**2*x4**4/(x4**2 - x5**2)**2'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.33333333333333*pi*x0*x2**2*x3**2*x4**4/(x4**2 - x5**2)**2', 'derivative_formatted': '1.33333333333333*pi*x0*x2**2*x3**2*x4**4/(x4**2 - x5**2)**2'
      },
      {'var_name': 'x2', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2.66666666666667*pi*x0*x1*x2*x3**2*x4**4/(x4**2 - x5**2)**2', 'derivative_formatted': '2.66666666666667*pi*x0*x1*x2*x3**2*x4**4/(x4**2 - x5**2)**2'
      },
      {'var_name': 'x3', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2.66666666666667*pi*x0*x1*x2**2*x3*x4**4/(x4**2 - x5**2)**2', 'derivative_formatted': '2.66666666666667*pi*x0*x1*x2**2*x3*x4**4/(x4**2 - x5**2)**2'
      },
      {'var_name': 'x4', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-5.33333333333333*pi*x0*x1*x2**2*x3**2*x4**5/(x4**2 - x5**2)**3 + 5.33333333333333*pi*x0*x1*x2**2*x3**2*x4**3/(x4**2 - x5**2)**2', 'derivative_formatted': '-5.33333333333333*pi*x0*x1*x2**2*x3**2*x4**5/(x4**2 - x5**2)**3 + 5.33333333333333*pi*x0*x1*x2**2*x3**2*x4**3/(x4**2 - x5**2)**2'
      },
      {'var_name': 'x5', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '5.33333333333333*pi*x0*x1*x2**2*x3**2*x4**4*x5/(x4**2 - x5**2)**3', 'derivative_formatted': '5.33333333333333*pi*x0*x1*x2**2*x3**2*x4**4*x5/(x4**2 - x5**2)**3'
      }
    ], 'Variables': ['epsilon', 'c', 'Ef', 'r', 'omega', 'omega_0'
    ]
  },
  {'EquationName': 'FeynmanICh34Eq8', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2/x3', 'derivative_formatted': 'x1*x2/x3'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2/x3', 'derivative_formatted': 'x0*x2/x3'
      },
      {'var_name': 'x2', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/x3', 'derivative_formatted': 'x0*x1/x3'
      },
      {'var_name': 'x3', 'var_display_name': 'p', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2/x3**2', 'derivative_formatted': '-x0*x1*x2/x3**2'
      }
    ], 'Variables': ['q', 'v', 'B', 'p'
    ]
  },
  {'EquationName': 'FeynmanICh34Eq10', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*x2/(x0**2*(1 - x1/x0)**2)', 'derivative_formatted': '-x1*x2/(x0**2*(1 - x1/x0)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2/(x0*(1 - x1/x0)**2)', 'derivative_formatted': 'x2/(x0*(1 - x1/x0)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(1 - x1/x0)', 'derivative_formatted': '1/(1 - x1/x0)'
      }
    ], 'Variables': ['c', 'v', 'omega_0'
    ]
  },
  {'EquationName': 'FeynmanICh34Eq14', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*x2/(x0**2*sqrt(1 - x1**2/x0**2)) - x1**2*x2*(1 + x1/x0)/(x0**3*(1 - x1**2/x0**2)**(3/2))', 'derivative_formatted': '-x1*x2/(x0**2*sqrt(1 - x1**2/x0**2)) - x1**2*x2*(1 + x1/x0)/(x0**3*(1 - x1**2/x0**2)**(3/2))'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2/(x0*sqrt(1 - x1**2/x0**2)) + x1*x2*(1 + x1/x0)/(x0**2*(1 - x1**2/x0**2)**(3/2))', 'derivative_formatted': 'x2/(x0*sqrt(1 - x1**2/x0**2)) + x1*x2*(1 + x1/x0)/(x0**2*(1 - x1**2/x0**2)**(3/2))'
      },
      {'var_name': 'x2', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '(1 + x1/x0)/sqrt(1 - x1**2/x0**2)', 'derivative_formatted': '(1 + x1/x0)/sqrt(1 - x1**2/x0**2)'
      }
    ], 'Variables': ['c', 'v', 'omega_0'
    ]
  },
  {'EquationName': 'FeynmanICh34Eq27', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(2*pi)', 'derivative_formatted': 'x1/(2*pi)'
      },
      {'var_name': 'x1', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(2*pi)', 'derivative_formatted': 'x0/(2*pi)'
      }
    ], 'Variables': ['omega', 'h'
    ]
  },
  {'EquationName': 'FeynmanICh37Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'I1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '1 + sqrt(x0*x1)*cos(x2)/x0', 'derivative_formatted': '1 + sqrt(x0*x1)*cos(x2)/x0'
      },
      {'var_name': 'x1', 'var_display_name': 'I2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '1 + sqrt(x0*x1)*cos(x2)/x1', 'derivative_formatted': '1 + sqrt(x0*x1)*cos(x2)/x1'
      },
      {'var_name': 'x2', 'var_display_name': 'delta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-2*sqrt(x0*x1)*sin(x2)', 'derivative_formatted': '-2*sqrt(x0*x1)*sin(x2)'
      }
    ], 'Variables': ['I1', 'I2', 'delta'
    ]
  },
  {'EquationName': 'FeynmanICh38Eq12', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x2**2*x3/(pi*x0**2*x1**2)', 'derivative_formatted': '-x2**2*x3/(pi*x0**2*x1**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x2**2*x3/(pi*x0*x1**3)', 'derivative_formatted': '-2*x2**2*x3/(pi*x0*x1**3)'
      },
      {'var_name': 'x2', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x2*x3/(pi*x0*x1**2)', 'derivative_formatted': '2*x2*x3/(pi*x0*x1**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2**2/(pi*x0*x1**2)', 'derivative_formatted': 'x2**2/(pi*x0*x1**2)'
      }
    ], 'Variables': ['m', 'q', 'h', 'epsilon'
    ]
  },
  {'EquationName': 'FeynmanICh39Eq10', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'pr', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.5*x1', 'derivative_formatted': '1.5*x1'
      },
      {'var_name': 'x1', 'var_display_name': 'V', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1.5*x0', 'derivative_formatted': '1.5*x0'
      }
    ], 'Variables': ['pr', 'V'
    ]
  },
  {'EquationName': 'FeynmanICh39Eq11', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'gamma', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*x2/(x0 - 1)**2', 'derivative_formatted': '-x1*x2/(x0 - 1)**2'
      },
      {'var_name': 'x1', 'var_display_name': 'pr', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2/(x0 - 1)', 'derivative_formatted': 'x2/(x0 - 1)'
      },
      {'var_name': 'x2', 'var_display_name': 'V', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(x0 - 1)', 'derivative_formatted': 'x1/(x0 - 1)'
      }
    ], 'Variables': ['gamma', 'pr', 'V'
    ]
  },
  {'EquationName': 'FeynmanICh39Eq22', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x3/x2', 'derivative_formatted': 'x1*x3/x2'
      },
      {'var_name': 'x1', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x3/x2', 'derivative_formatted': 'x0*x3/x2'
      },
      {'var_name': 'x2', 'var_display_name': 'V', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x3/x2**2', 'derivative_formatted': '-x0*x1*x3/x2**2'
      },
      {'var_name': 'x3', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/x2', 'derivative_formatted': 'x0*x1/x2'
      }
    ], 'Variables': ['n', 'T', 'V', 'kb'
    ]
  },
  {'EquationName': 'FeynmanICh40Eq1', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'exp(-x1*x2*x4/(x3*x5))', 'derivative_formatted': 'exp(-x1*x2*x4/(x3*x5))'
      },
      {'var_name': 'x1', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x2*x4*exp(-x1*x2*x4/(x3*x5))/(x3*x5)', 'derivative_formatted': '-x0*x2*x4*exp(-x1*x2*x4/(x3*x5))/(x3*x5)'
      },
      {'var_name': 'x2', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x4*exp(-x1*x2*x4/(x3*x5))/(x3*x5)', 'derivative_formatted': '-x0*x1*x4*exp(-x1*x2*x4/(x3*x5))/(x3*x5)'
      },
      {'var_name': 'x3', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2*x4*exp(-x1*x2*x4/(x3*x5))/(x3**2*x5)', 'derivative_formatted': 'x0*x1*x2*x4*exp(-x1*x2*x4/(x3*x5))/(x3**2*x5)'
      },
      {'var_name': 'x4', 'var_display_name': 'g', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2*exp(-x1*x2*x4/(x3*x5))/(x3*x5)', 'derivative_formatted': '-x0*x1*x2*exp(-x1*x2*x4/(x3*x5))/(x3*x5)'
      },
      {'var_name': 'x5', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2*x4*exp(-x1*x2*x4/(x3*x5))/(x3*x5**2)', 'derivative_formatted': 'x0*x1*x2*x4*exp(-x1*x2*x4/(x3*x5))/(x3*x5**2)'
      }
    ], 'Variables': ['n_0', 'm', 'x', 'T', 'g', 'kb'
    ]
  },
  {'EquationName': 'FeynmanICh41Eq16', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0**3*x2**2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1*x3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2) + 3*x0**2*x2/(2*pi**3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1))', 'derivative_formatted': '-x0**3*x2**2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1*x3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2) + 3*x0**2*x2/(2*pi**3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1))'
      },
      {'var_name': 'x1', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**4*x2**2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1**2*x3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2)', 'derivative_formatted': 'x0**4*x2**2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1**2*x3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**4*x2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1*x3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2) + x0**3/(2*pi**3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1))', 'derivative_formatted': '-x0**4*x2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1*x3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2) + x0**3/(2*pi**3*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1))'
      },
      {'var_name': 'x3', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**4*x2**2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1*x3**2*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2)', 'derivative_formatted': 'x0**4*x2**2*exp(x0*x2/(2*pi*x1*x3))/(4*pi**4*x1*x3**2*x4**2*(exp(x0*x2/(2*pi*x1*x3)) - 1)**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**3*x2/(pi**3*x4**3*(exp(x0*x2/(2*pi*x1*x3)) - 1))', 'derivative_formatted': '-x0**3*x2/(pi**3*x4**3*(exp(x0*x2/(2*pi*x1*x3)) - 1))'
      }
    ], 'Variables': ['omega', 'T', 'h', 'kb', 'c'
    ]
  },
  {'EquationName': 'FeynmanICh43Eq16', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mu_drift', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2/x3', 'derivative_formatted': 'x1*x2/x3'
      },
      {'var_name': 'x1', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2/x3', 'derivative_formatted': 'x0*x2/x3'
      },
      {'var_name': 'x2', 'var_display_name': 'Volt', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/x3', 'derivative_formatted': 'x0*x1/x3'
      },
      {'var_name': 'x3', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2/x3**2', 'derivative_formatted': '-x0*x1*x2/x3**2'
      }
    ], 'Variables': ['mu_drift', 'q', 'Volt', 'd'
    ]
  },
  {'EquationName': 'FeynmanICh43Eq31', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mob', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2', 'derivative_formatted': 'x1*x2'
      },
      {'var_name': 'x1', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2', 'derivative_formatted': 'x0*x2'
      },
      {'var_name': 'x2', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1', 'derivative_formatted': 'x0*x1'
      }
    ], 'Variables': ['mob', 'T', 'kb'
    ]
  },
  {'EquationName': 'FeynmanICh43Eq43', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'gamma', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*x3/(x2*(x0 - 1)**2)', 'derivative_formatted': '-x1*x3/(x2*(x0 - 1)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x3/(x2*(x0 - 1))', 'derivative_formatted': 'x3/(x2*(x0 - 1))'
      },
      {'var_name': 'x2', 'var_display_name': 'A', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*x3/(x2**2*(x0 - 1))', 'derivative_formatted': '-x1*x3/(x2**2*(x0 - 1))'
      },
      {'var_name': 'x3', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(x2*(x0 - 1))', 'derivative_formatted': 'x1/(x2*(x0 - 1))'
      }
    ], 'Variables': ['gamma', 'kb', 'A', 'v'
    ]
  },
  {'EquationName': 'FeynmanICh44Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*x2*log(x4/x3)', 'derivative_formatted': 'x1*x2*log(x4/x3)'
      },
      {'var_name': 'x1', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x2*log(x4/x3)', 'derivative_formatted': 'x0*x2*log(x4/x3)'
      },
      {'var_name': 'x2', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*log(x4/x3)', 'derivative_formatted': 'x0*x1*log(x4/x3)'
      },
      {'var_name': 'x3', 'var_display_name': 'V1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2/x3', 'derivative_formatted': '-x0*x1*x2/x3'
      },
      {'var_name': 'x4', 'var_display_name': 'V2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2/x4', 'derivative_formatted': 'x0*x1*x2/x4'
      }
    ], 'Variables': ['n', 'kb', 'T', 'V1', 'V2'
    ]
  },
  {'EquationName': 'FeynmanICh47Eq23', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'gamma', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sqrt(x0*x1/x2)/(2*x0)', 'derivative_formatted': 'sqrt(x0*x1/x2)/(2*x0)'
      },
      {'var_name': 'x1', 'var_display_name': 'pr', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sqrt(x0*x1/x2)/(2*x1)', 'derivative_formatted': 'sqrt(x0*x1/x2)/(2*x1)'
      },
      {'var_name': 'x2', 'var_display_name': 'rho', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-sqrt(x0*x1/x2)/(2*x2)', 'derivative_formatted': '-sqrt(x0*x1/x2)/(2*x2)'
      }
    ], 'Variables': ['gamma', 'pr', 'rho'
    ]
  },
  {'EquationName': 'FeynmanICh48Eq2', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2**2/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': 'x2**2/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/(-x1**2/x2**2 + 1)**(3/2)', 'derivative_formatted': 'x0*x1/(-x1**2/x2**2 + 1)**(3/2)'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-x0*x1**2/(x2*(-x1**2/x2**2 + 1)**(3/2)) + 2*x0*x2/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': '-x0*x1**2/(x2*(-x1**2/x2**2 + 1)**(3/2)) + 2*x0*x2/sqrt(-x1**2/x2**2 + 1)'
      }
    ], 'Variables': ['m', 'v', 'c'
    ]
  },
  {'EquationName': 'FeynmanICh50Eq26', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'x1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x3*cos(x1*x2)**2 + cos(x1*x2)', 'derivative_formatted': 'x3*cos(x1*x2)**2 + cos(x1*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*(-2*x2*x3*sin(x1*x2)*cos(x1*x2) - x2*sin(x1*x2))', 'derivative_formatted': 'x0*(-2*x2*x3*sin(x1*x2)*cos(x1*x2) - x2*sin(x1*x2))'
      },
      {'var_name': 'x2', 'var_display_name': 't', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*(-2*x1*x3*sin(x1*x2)*cos(x1*x2) - x1*sin(x1*x2))', 'derivative_formatted': 'x0*(-2*x1*x3*sin(x1*x2)*cos(x1*x2) - x1*sin(x1*x2))'
      },
      {'var_name': 'x3', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*cos(x1*x2)**2', 'derivative_formatted': 'x0*cos(x1*x2)**2'
      }
    ], 'Variables': ['x1', 'omega', 't', 'alpha'
    ]
  },
  {'EquationName': 'FeynmanIICh2Eq42', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'kappa', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x3*(-x1 + x2)/x4', 'derivative_formatted': 'x3*(-x1 + x2)/x4'
      },
      {'var_name': 'x1', 'var_display_name': 'T1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x3/x4', 'derivative_formatted': '-x0*x3/x4'
      },
      {'var_name': 'x2', 'var_display_name': 'T2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x3/x4', 'derivative_formatted': 'x0*x3/x4'
      },
      {'var_name': 'x3', 'var_display_name': 'A', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*(-x1 + x2)/x4', 'derivative_formatted': 'x0*(-x1 + x2)/x4'
      },
      {'var_name': 'x4', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x3*(-x1 + x2)/x4**2', 'derivative_formatted': '-x0*x3*(-x1 + x2)/x4**2'
      }
    ], 'Variables': ['kappa', 'T1', 'T2', 'A', 'd'
    ]
  },
  {'EquationName': 'FeynmanIICh3Eq24', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'Pwr', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(4*pi*x1**2)', 'derivative_formatted': '1/(4*pi*x1**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(2*pi*x1**3)', 'derivative_formatted': '-x0/(2*pi*x1**3)'
      }
    ], 'Variables': ['Pwr', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh4Eq23', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(4*pi*x1*x2)', 'derivative_formatted': '1/(4*pi*x1*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(4*pi*x1**2*x2)', 'derivative_formatted': '-x0/(4*pi*x1**2*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(4*pi*x1*x2**2)', 'derivative_formatted': '-x0/(4*pi*x1*x2**2)'
      }
    ], 'Variables': ['q', 'epsilon', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh6Eq11', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1*cos(x2)/(4*pi*x0**2*x3**2)', 'derivative_formatted': '-x1*cos(x2)/(4*pi*x0**2*x3**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'cos(x2)/(4*pi*x0*x3**2)', 'derivative_formatted': 'cos(x2)/(4*pi*x0*x3**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*sin(x2)/(4*pi*x0*x3**2)', 'derivative_formatted': '-x1*sin(x2)/(4*pi*x0*x3**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1*cos(x2)/(2*pi*x0*x3**3)', 'derivative_formatted': '-x1*cos(x2)/(2*pi*x0*x3**3)'
      }
    ], 'Variables': ['epsilon', 'p_d', 'theta', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh6Eq15a', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-3*x1*x5*sqrt(x3**2 + x4**2)/(4*pi*x0**2*x2**5)', 'derivative_formatted': '-3*x1*x5*sqrt(x3**2 + x4**2)/(4*pi*x0**2*x2**5)'
      },
      {'var_name': 'x1', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x5*sqrt(x3**2 + x4**2)/(4*pi*x0*x2**5)', 'derivative_formatted': '3*x5*sqrt(x3**2 + x4**2)/(4*pi*x0*x2**5)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-15*x1*x5*sqrt(x3**2 + x4**2)/(4*pi*x0*x2**6)', 'derivative_formatted': '-15*x1*x5*sqrt(x3**2 + x4**2)/(4*pi*x0*x2**6)'
      },
      {'var_name': 'x3', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x1*x3*x5/(4*pi*x0*x2**5*sqrt(x3**2 + x4**2))', 'derivative_formatted': '3*x1*x3*x5/(4*pi*x0*x2**5*sqrt(x3**2 + x4**2))'
      },
      {'var_name': 'x4', 'var_display_name': 'y', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x1*x4*x5/(4*pi*x0*x2**5*sqrt(x3**2 + x4**2))', 'derivative_formatted': '3*x1*x4*x5/(4*pi*x0*x2**5*sqrt(x3**2 + x4**2))'
      },
      {'var_name': 'x5', 'var_display_name': 'z', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x1*sqrt(x3**2 + x4**2)/(4*pi*x0*x2**5)', 'derivative_formatted': '3*x1*sqrt(x3**2 + x4**2)/(4*pi*x0*x2**5)'
      }
    ], 'Variables': ['epsilon', 'p_d', 'r', 'x', 'y', 'z'
    ]
  },
  {'EquationName': 'FeynmanIICh6Eq15b', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-3*x1*sin(x2)*cos(x2)/(4*pi*x0**2*x3**3)', 'derivative_formatted': '-3*x1*sin(x2)*cos(x2)/(4*pi*x0**2*x3**3)'
      },
      {'var_name': 'x1', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '3*sin(x2)*cos(x2)/(4*pi*x0*x3**3)', 'derivative_formatted': '3*sin(x2)*cos(x2)/(4*pi*x0*x3**3)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-3*x1*sin(x2)**2/(4*pi*x0*x3**3) + 3*x1*cos(x2)**2/(4*pi*x0*x3**3)', 'derivative_formatted': '-3*x1*sin(x2)**2/(4*pi*x0*x3**3) + 3*x1*cos(x2)**2/(4*pi*x0*x3**3)'
      },
      {'var_name': 'x3', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-9*x1*sin(x2)*cos(x2)/(4*pi*x0*x3**4)', 'derivative_formatted': '-9*x1*sin(x2)*cos(x2)/(4*pi*x0*x3**4)'
      }
    ], 'Variables': ['epsilon', 'p_d', 'theta', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh8Eq7', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '0.3*x0/(pi*x1*x2)', 'derivative_formatted': '0.3*x0/(pi*x1*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-0.15*x0**2/(pi*x1**2*x2)', 'derivative_formatted': '-0.15*x0**2/(pi*x1**2*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-0.15*x0**2/(pi*x1*x2**2)', 'derivative_formatted': '-0.15*x0**2/(pi*x1*x2**2)'
      }
    ], 'Variables': ['q', 'epsilon', 'd'
    ]
  },
  {'EquationName': 'FeynmanIICh8Eq31', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1**2/2', 'derivative_formatted': 'x1**2/2'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1', 'derivative_formatted': 'x0*x1'
      }
    ], 'Variables': ['epsilon', 'Ef'
    ]
  },
  {'EquationName': 'FeynmanIICh10Eq9', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'sigma_den', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(x1*(x2 + 1))', 'derivative_formatted': '1/(x1*(x2 + 1))'
      },
      {'var_name': 'x1', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(x1**2*(x2 + 1))', 'derivative_formatted': '-x0/(x1**2*(x2 + 1))'
      },
      {'var_name': 'x2', 'var_display_name': 'chi', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(x1*(x2 + 1)**2)', 'derivative_formatted': '-x0/(x1*(x2 + 1)**2)'
      }
    ], 'Variables': ['sigma_den', 'epsilon', 'chi'
    ]
  },
  {'EquationName': 'FeynmanIICh11Eq3', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(x2*(x3**2 - x4**2))', 'derivative_formatted': 'x1/(x2*(x3**2 - x4**2))'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(x2*(x3**2 - x4**2))', 'derivative_formatted': 'x0/(x2*(x3**2 - x4**2))'
      },
      {'var_name': 'x2', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(x2**2*(x3**2 - x4**2))', 'derivative_formatted': '-x0*x1/(x2**2*(x3**2 - x4**2))'
      },
      {'var_name': 'x3', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x0*x1*x3/(x2*(x3**2 - x4**2)**2)', 'derivative_formatted': '-2*x0*x1*x3/(x2*(x3**2 - x4**2)**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0*x1*x4/(x2*(x3**2 - x4**2)**2)', 'derivative_formatted': '2*x0*x1*x4/(x2*(x3**2 - x4**2)**2)'
      }
    ], 'Variables': ['q', 'Ef', 'm', 'omega_0', 'omega'
    ]
  },
  {'EquationName': 'FeynmanIICh11Eq17', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n_0', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '1 + x4*x5*cos(x3)/(x1*x2)', 'derivative_formatted': '1 + x4*x5*cos(x3)/(x1*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x4*x5*cos(x3)/(x1**2*x2)', 'derivative_formatted': '-x0*x4*x5*cos(x3)/(x1**2*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x4*x5*cos(x3)/(x1*x2**2)', 'derivative_formatted': '-x0*x4*x5*cos(x3)/(x1*x2**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x4*x5*sin(x3)/(x1*x2)', 'derivative_formatted': '-x0*x4*x5*sin(x3)/(x1*x2)'
      },
      {'var_name': 'x4', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x5*cos(x3)/(x1*x2)', 'derivative_formatted': 'x0*x5*cos(x3)/(x1*x2)'
      },
      {'var_name': 'x5', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x4*cos(x3)/(x1*x2)', 'derivative_formatted': 'x0*x4*cos(x3)/(x1*x2)'
      }
    ], 'Variables': ['n_0', 'kb', 'T', 'theta', 'p_d', 'Ef'
    ]
  },
  {'EquationName': 'FeynmanIICh11Eq20', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n_rho', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1**2*x2/(3*x3*x4)', 'derivative_formatted': 'x1**2*x2/(3*x3*x4)'
      },
      {'var_name': 'x1', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0*x1*x2/(3*x3*x4)', 'derivative_formatted': '2*x0*x1*x2/(3*x3*x4)'
      },
      {'var_name': 'x2', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2/(3*x3*x4)', 'derivative_formatted': 'x0*x1**2/(3*x3*x4)'
      },
      {'var_name': 'x3', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2*x2/(3*x3**2*x4)', 'derivative_formatted': '-x0*x1**2*x2/(3*x3**2*x4)'
      },
      {'var_name': 'x4', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2*x2/(3*x3*x4**2)', 'derivative_formatted': '-x0*x1**2*x2/(3*x3*x4**2)'
      }
    ], 'Variables': ['n_rho', 'p_d', 'Ef', 'kb', 'T'
    ]
  },
  {'EquationName': 'FeynmanIICh11Eq27', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2*x2*x3/(3*(-x0*x1/3 + 1)**2) + x1*x2*x3/(-x0*x1/3 + 1)', 'derivative_formatted': 'x0*x1**2*x2*x3/(3*(-x0*x1/3 + 1)**2) + x1*x2*x3/(-x0*x1/3 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1*x2*x3/(3*(-x0*x1/3 + 1)**2) + x0*x2*x3/(-x0*x1/3 + 1)', 'derivative_formatted': 'x0**2*x1*x2*x3/(3*(-x0*x1/3 + 1)**2) + x0*x2*x3/(-x0*x1/3 + 1)'
      },
      {'var_name': 'x2', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x3/(-x0*x1/3 + 1)', 'derivative_formatted': 'x0*x1*x3/(-x0*x1/3 + 1)'
      },
      {'var_name': 'x3', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2/(-x0*x1/3 + 1)', 'derivative_formatted': 'x0*x1*x2/(-x0*x1/3 + 1)'
      }
    ], 'Variables': ['n', 'alpha', 'epsilon', 'Ef'
    ]
  },
  {'EquationName': 'FeynmanIICh11Eq28', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2/(3*(-x0*x1/3 + 1)**2) + x1/(-x0*x1/3 + 1)', 'derivative_formatted': 'x0*x1**2/(3*(-x0*x1/3 + 1)**2) + x1/(-x0*x1/3 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1/(3*(-x0*x1/3 + 1)**2) + x0/(-x0*x1/3 + 1)', 'derivative_formatted': 'x0**2*x1/(3*(-x0*x1/3 + 1)**2) + x0/(-x0*x1/3 + 1)'
      }
    ], 'Variables': ['n', 'alpha'
    ]
  },
  {'EquationName': 'FeynmanIICh13Eq17', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x2/(2*pi*x0**2*x1**2*x3)', 'derivative_formatted': '-x2/(2*pi*x0**2*x1**2*x3)'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x2/(pi*x0*x1**3*x3)', 'derivative_formatted': '-x2/(pi*x0*x1**3*x3)'
      },
      {'var_name': 'x2', 'var_display_name': 'I', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(2*pi*x0*x1**2*x3)', 'derivative_formatted': '1/(2*pi*x0*x1**2*x3)'
      },
      {'var_name': 'x3', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x2/(2*pi*x0*x1**2*x3**2)', 'derivative_formatted': '-x2/(2*pi*x0*x1**2*x3**2)'
      }
    ], 'Variables': ['epsilon', 'c', 'I', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh13Eq23', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'rho_c_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': '1/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/(x2**2*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': 'x0*x1/(x2**2*(-x1**2/x2**2 + 1)**(3/2))'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2/(x2**3*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': '-x0*x1**2/(x2**3*(-x1**2/x2**2 + 1)**(3/2))'
      }
    ], 'Variables': ['rho_c_0', 'v', 'c'
    ]
  },
  {'EquationName': 'FeynmanIICh13Eq34', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'rho_c_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': 'x1/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2/(x2**2*(-x1**2/x2**2 + 1)**(3/2)) + x0/sqrt(-x1**2/x2**2 + 1)', 'derivative_formatted': 'x0*x1**2/(x2**2*(-x1**2/x2**2 + 1)**(3/2)) + x0/sqrt(-x1**2/x2**2 + 1)'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**3/(x2**3*(-x1**2/x2**2 + 1)**(3/2))', 'derivative_formatted': '-x0*x1**3/(x2**3*(-x1**2/x2**2 + 1)**(3/2))'
      }
    ], 'Variables': ['rho_c_0', 'v', 'c'
    ]
  },
  {'EquationName': 'FeynmanIICh15Eq4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1*cos(x2)', 'derivative_formatted': '-x1*cos(x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*cos(x2)', 'derivative_formatted': '-x0*cos(x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*sin(x2)', 'derivative_formatted': 'x0*x1*sin(x2)'
      }
    ], 'Variables': ['mom', 'B', 'theta'
    ]
  },
  {'EquationName': 'FeynmanIICh15Eq5', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1*cos(x2)', 'derivative_formatted': '-x1*cos(x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*cos(x2)', 'derivative_formatted': '-x0*cos(x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*sin(x2)', 'derivative_formatted': 'x0*x1*sin(x2)'
      }
    ], 'Variables': ['p_d', 'Ef', 'theta'
    ]
  },
  {'EquationName': 'FeynmanIICh21Eq32', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(4*pi*x1*x2*(-x3/x4 + 1))', 'derivative_formatted': '1/(4*pi*x1*x2*(-x3/x4 + 1))'
      },
      {'var_name': 'x1', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(4*pi*x1**2*x2*(-x3/x4 + 1))', 'derivative_formatted': '-x0/(4*pi*x1**2*x2*(-x3/x4 + 1))'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(4*pi*x1*x2**2*(-x3/x4 + 1))', 'derivative_formatted': '-x0/(4*pi*x1*x2**2*(-x3/x4 + 1))'
      },
      {'var_name': 'x3', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(4*pi*x1*x2*x4*(-x3/x4 + 1)**2)', 'derivative_formatted': 'x0/(4*pi*x1*x2*x4*(-x3/x4 + 1)**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x3/(4*pi*x1*x2*x4**2*(-x3/x4 + 1)**2)', 'derivative_formatted': '-x0*x3/(4*pi*x1*x2*x4**2*(-x3/x4 + 1)**2)'
      }
    ], 'Variables': ['q', 'epsilon', 'r', 'v', 'c'
    ]
  },
  {'EquationName': 'FeynmanIICh24Eq17', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(x1**2*sqrt(x0**2/x1**2 - pi**2/x2**2))', 'derivative_formatted': 'x0/(x1**2*sqrt(x0**2/x1**2 - pi**2/x2**2))'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2/(x1**3*sqrt(x0**2/x1**2 - pi**2/x2**2))', 'derivative_formatted': '-x0**2/(x1**3*sqrt(x0**2/x1**2 - pi**2/x2**2))'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'pi**2/(x2**3*sqrt(x0**2/x1**2 - pi**2/x2**2))', 'derivative_formatted': 'pi**2/(x2**3*sqrt(x0**2/x1**2 - pi**2/x2**2))'
      }
    ], 'Variables': ['omega', 'c', 'd'
    ]
  },
  {'EquationName': 'FeynmanIICh27Eq16', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2**2', 'derivative_formatted': 'x1*x2**2'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2**2', 'derivative_formatted': 'x0*x2**2'
      },
      {'var_name': 'x2', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0*x1*x2', 'derivative_formatted': '2*x0*x1*x2'
      }
    ], 'Variables': ['epsilon', 'c', 'Ef'
    ]
  },
  {'EquationName': 'FeynmanIICh27Eq18', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1**2', 'derivative_formatted': 'x1**2'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0*x1', 'derivative_formatted': '2*x0*x1'
      }
    ], 'Variables': ['epsilon', 'Ef'
    ]
  },
  {'EquationName': 'FeynmanIICh34Eq2a', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(2*pi*x2)', 'derivative_formatted': 'x1/(2*pi*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(2*pi*x2)', 'derivative_formatted': 'x0/(2*pi*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(2*pi*x2**2)', 'derivative_formatted': '-x0*x1/(2*pi*x2**2)'
      }
    ], 'Variables': ['q', 'v', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh34Eq2', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2/2', 'derivative_formatted': 'x1*x2/2'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2/2', 'derivative_formatted': 'x0*x2/2'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/2', 'derivative_formatted': 'x0*x1/2'
      }
    ], 'Variables': ['q', 'v', 'r'
    ]
  },
  {'EquationName': 'FeynmanIICh34Eq11', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'g_', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x2/(2*x3)', 'derivative_formatted': 'x1*x2/(2*x3)'
      },
      {'var_name': 'x1', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2/(2*x3)', 'derivative_formatted': 'x0*x2/(2*x3)'
      },
      {'var_name': 'x2', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/(2*x3)', 'derivative_formatted': 'x0*x1/(2*x3)'
      },
      {'var_name': 'x3', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2/(2*x3**2)', 'derivative_formatted': '-x0*x1*x2/(2*x3**2)'
      }
    ], 'Variables': ['g_', 'q', 'B', 'm'
    ]
  },
  {'EquationName': 'FeynmanIICh34Eq29a', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(4*pi*x2)', 'derivative_formatted': 'x1/(4*pi*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(4*pi*x2)', 'derivative_formatted': 'x0/(4*pi*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(4*pi*x2**2)', 'derivative_formatted': '-x0*x1/(4*pi*x2**2)'
      }
    ], 'Variables': ['q', 'h', 'm'
    ]
  },
  {'EquationName': 'FeynmanIICh34Eq29b', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'g_', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*pi*x2*x3*x4/x1', 'derivative_formatted': '2*pi*x2*x3*x4/x1'
      },
      {'var_name': 'x1', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*pi*x0*x2*x3*x4/x1**2', 'derivative_formatted': '-2*pi*x0*x2*x3*x4/x1**2'
      },
      {'var_name': 'x2', 'var_display_name': 'Jz', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*pi*x0*x3*x4/x1', 'derivative_formatted': '2*pi*x0*x3*x4/x1'
      },
      {'var_name': 'x3', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*pi*x0*x2*x4/x1', 'derivative_formatted': '2*pi*x0*x2*x4/x1'
      },
      {'var_name': 'x4', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*pi*x0*x2*x3/x1', 'derivative_formatted': '2*pi*x0*x2*x3/x1'
      }
    ], 'Variables': ['g_', 'h', 'Jz', 'mom', 'B'
    ]
  },
  {'EquationName': 'FeynmanIICh35Eq18', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))', 'derivative_formatted': '1/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))'
      },
      {'var_name': 'x1', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*(x3*x4*exp(x3*x4/(x1*x2))/(x1**2*x2) - x3*x4*exp(-x3*x4/(x1*x2))/(x1**2*x2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2', 'derivative_formatted': 'x0*(x3*x4*exp(x3*x4/(x1*x2))/(x1**2*x2) - x3*x4*exp(-x3*x4/(x1*x2))/(x1**2*x2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2'
      },
      {'var_name': 'x2', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*(x3*x4*exp(x3*x4/(x1*x2))/(x1*x2**2) - x3*x4*exp(-x3*x4/(x1*x2))/(x1*x2**2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2', 'derivative_formatted': 'x0*(x3*x4*exp(x3*x4/(x1*x2))/(x1*x2**2) - x3*x4*exp(-x3*x4/(x1*x2))/(x1*x2**2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2'
      },
      {'var_name': 'x3', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*(-x4*exp(x3*x4/(x1*x2))/(x1*x2) + x4*exp(-x3*x4/(x1*x2))/(x1*x2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2', 'derivative_formatted': 'x0*(-x4*exp(x3*x4/(x1*x2))/(x1*x2) + x4*exp(-x3*x4/(x1*x2))/(x1*x2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2'
      },
      {'var_name': 'x4', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*(-x3*exp(x3*x4/(x1*x2))/(x1*x2) + x3*exp(-x3*x4/(x1*x2))/(x1*x2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2', 'derivative_formatted': 'x0*(-x3*exp(x3*x4/(x1*x2))/(x1*x2) + x3*exp(-x3*x4/(x1*x2))/(x1*x2))/(exp(x3*x4/(x1*x2)) + exp(-x3*x4/(x1*x2)))**2'
      }
    ], 'Variables': ['n_0', 'kb', 'T', 'mom', 'B'
    ]
  },
  {'EquationName': 'FeynmanIICh35Eq21', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n_rho', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*tanh(x1*x2/(x3*x4))', 'derivative_formatted': 'x1*tanh(x1*x2/(x3*x4))'
      },
      {'var_name': 'x1', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3*x4) + x0*tanh(x1*x2/(x3*x4))', 'derivative_formatted': 'x0*x1*x2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3*x4) + x0*tanh(x1*x2/(x3*x4))'
      },
      {'var_name': 'x2', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3*x4)', 'derivative_formatted': 'x0*x1**2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3*x4)'
      },
      {'var_name': 'x3', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2*x2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3**2*x4)', 'derivative_formatted': '-x0*x1**2*x2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3**2*x4)'
      },
      {'var_name': 'x4', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2*x2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3*x4**2)', 'derivative_formatted': '-x0*x1**2*x2*(1 - tanh(x1*x2/(x3*x4))**2)/(x3*x4**2)'
      }
    ], 'Variables': ['n_rho', 'mom', 'B', 'kb', 'T'
    ]
  },
  {'EquationName': 'FeynmanIICh36Eq38', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(x2*x3) + x4*x7/(x2*x3*x5*x6**2)', 'derivative_formatted': 'x1/(x2*x3) + x4*x7/(x2*x3*x5*x6**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'H', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(x2*x3)', 'derivative_formatted': 'x0/(x2*x3)'
      },
      {'var_name': 'x2', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(x2**2*x3) - x0*x4*x7/(x2**2*x3*x5*x6**2)', 'derivative_formatted': '-x0*x1/(x2**2*x3) - x0*x4*x7/(x2**2*x3*x5*x6**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/(x2*x3**2) - x0*x4*x7/(x2*x3**2*x5*x6**2)', 'derivative_formatted': '-x0*x1/(x2*x3**2) - x0*x4*x7/(x2*x3**2*x5*x6**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x7/(x2*x3*x5*x6**2)', 'derivative_formatted': 'x0*x7/(x2*x3*x5*x6**2)'
      },
      {'var_name': 'x5', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x4*x7/(x2*x3*x5**2*x6**2)', 'derivative_formatted': '-x0*x4*x7/(x2*x3*x5**2*x6**2)'
      },
      {'var_name': 'x6', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x0*x4*x7/(x2*x3*x5*x6**3)', 'derivative_formatted': '-2*x0*x4*x7/(x2*x3*x5*x6**3)'
      },
      {'var_name': 'x7', 'var_display_name': 'M', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x4/(x2*x3*x5*x6**2)', 'derivative_formatted': 'x0*x4/(x2*x3*x5*x6**2)'
      }
    ], 'Variables': ['mom', 'H', 'kb', 'T', 'alpha', 'epsilon', 'c', 'M'
    ]
  },
  {'EquationName': 'FeynmanIICh37Eq1', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*(x2 + 1)', 'derivative_formatted': 'x1*(x2 + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*(x2 + 1)', 'derivative_formatted': 'x0*(x2 + 1)'
      },
      {'var_name': 'x2', 'var_display_name': 'chi', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1', 'derivative_formatted': 'x0*x1'
      }
    ], 'Variables': ['mom', 'B', 'chi'
    ]
  },
  {'EquationName': 'FeynmanIICh38Eq3', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'Y', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x3/x2', 'derivative_formatted': 'x1*x3/x2'
      },
      {'var_name': 'x1', 'var_display_name': 'A', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x3/x2', 'derivative_formatted': 'x0*x3/x2'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x3/x2**2', 'derivative_formatted': '-x0*x1*x3/x2**2'
      },
      {'var_name': 'x3', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/x2', 'derivative_formatted': 'x0*x1/x2'
      }
    ], 'Variables': ['Y', 'A', 'd', 'x'
    ]
  },
  {'EquationName': 'FeynmanIICh38Eq14', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'Y', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(2*x1 + 2)', 'derivative_formatted': '1/(2*x1 + 2)'
      },
      {'var_name': 'x1', 'var_display_name': 'sigma', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x0/(2*x1 + 2)**2', 'derivative_formatted': '-2*x0/(2*x1 + 2)**2'
      }
    ], 'Variables': ['Y', 'sigma'
    ]
  },
  {'EquationName': 'FeynmanIIICh4Eq32', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)', 'derivative_formatted': '-x1*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)', 'derivative_formatted': '-x0*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2**2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)', 'derivative_formatted': 'x0*x1*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2**2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2*x3**2*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)', 'derivative_formatted': 'x0*x1*exp(x0*x1/(2*pi*x2*x3))/(2*pi*x2*x3**2*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)'
      }
    ], 'Variables': ['h', 'omega', 'kb', 'T'
    ]
  },
  {'EquationName': 'FeynmanIIICh4Eq33', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2) + x1/(2*pi*(exp(x0*x1/(2*pi*x2*x3)) - 1))', 'derivative_formatted': '-x0*x1**2*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2) + x1/(2*pi*(exp(x0*x1/(2*pi*x2*x3)) - 1))'
      },
      {'var_name': 'x1', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*x1*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2) + x0/(2*pi*(exp(x0*x1/(2*pi*x2*x3)) - 1))', 'derivative_formatted': '-x0**2*x1*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2) + x0/(2*pi*(exp(x0*x1/(2*pi*x2*x3)) - 1))'
      },
      {'var_name': 'x2', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1**2*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2**2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)', 'derivative_formatted': 'x0**2*x1**2*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2**2*x3*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1**2*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2*x3**2*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)', 'derivative_formatted': 'x0**2*x1**2*exp(x0*x1/(2*pi*x2*x3))/(4*pi**2*x2*x3**2*(exp(x0*x1/(2*pi*x2*x3)) - 1)**2)'
      }
    ], 'Variables': ['h', 'omega', 'kb', 'T'
    ]
  },
  {'EquationName': 'FeynmanIIICh7Eq38', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*pi*x1/x2', 'derivative_formatted': '4*pi*x1/x2'
      },
      {'var_name': 'x1', 'var_display_name': 'B', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*pi*x0/x2', 'derivative_formatted': '4*pi*x0/x2'
      },
      {'var_name': 'x2', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-4*pi*x0*x1/x2**2', 'derivative_formatted': '-4*pi*x0*x1/x2**2'
      }
    ], 'Variables': ['mom', 'B', 'h'
    ]
  },
  {'EquationName': 'FeynmanIIICh8Eq54', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '4*pi*x1*sin(2*pi*x0*x1/x2)*cos(2*pi*x0*x1/x2)/x2', 'derivative_formatted': '4*pi*x1*sin(2*pi*x0*x1/x2)*cos(2*pi*x0*x1/x2)/x2'
      },
      {'var_name': 'x1', 'var_display_name': 't', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '4*pi*x0*sin(2*pi*x0*x1/x2)*cos(2*pi*x0*x1/x2)/x2', 'derivative_formatted': '4*pi*x0*sin(2*pi*x0*x1/x2)*cos(2*pi*x0*x1/x2)/x2'
      },
      {'var_name': 'x2', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-4*pi*x0*x1*sin(2*pi*x0*x1/x2)*cos(2*pi*x0*x1/x2)/x2**2', 'derivative_formatted': '-4*pi*x0*x1*sin(2*pi*x0*x1/x2)*cos(2*pi*x0*x1/x2)/x2**2'
      }
    ], 'Variables': ['E_n', 't', 'h'
    ]
  },
  {'EquationName': 'FeynmanIIICh9Eq52', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'p_d', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '8*pi*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**2)', 'derivative_formatted': '8*pi*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '8*pi*x0*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**2)', 'derivative_formatted': '8*pi*x0*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 't', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '16*pi*x0*x1*(x4/2 - x5/2)*sin(x2*(x4 - x5)/2)*cos(x2*(x4 - x5)/2)/(x2*x3*(x4 - x5)**2) - 8*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2**2*x3*(x4 - x5)**2)', 'derivative_formatted': '16*pi*x0*x1*(x4/2 - x5/2)*sin(x2*(x4 - x5)/2)*cos(x2*(x4 - x5)/2)/(x2*x3*(x4 - x5)**2) - 8*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2**2*x3*(x4 - x5)**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-8*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3**2*(x4 - x5)**2)', 'derivative_formatted': '-8*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3**2*(x4 - x5)**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '8*pi*x0*x1*sin(x2*(x4 - x5)/2)*cos(x2*(x4 - x5)/2)/(x3*(x4 - x5)**2) - 16*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**3)', 'derivative_formatted': '8*pi*x0*x1*sin(x2*(x4 - x5)/2)*cos(x2*(x4 - x5)/2)/(x3*(x4 - x5)**2) - 16*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**3)'
      },
      {'var_name': 'x5', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-8*pi*x0*x1*sin(x2*(x4 - x5)/2)*cos(x2*(x4 - x5)/2)/(x3*(x4 - x5)**2) + 16*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**3)', 'derivative_formatted': '-8*pi*x0*x1*sin(x2*(x4 - x5)/2)*cos(x2*(x4 - x5)/2)/(x3*(x4 - x5)**2) + 16*pi*x0*x1*sin(x2*(x4 - x5)/2)**2/(x2*x3*(x4 - x5)**3)'
      }
    ], 'Variables': ['p_d', 'Ef', 't', 'h', 'omega', 'omega_0'
    ]
  },
  {'EquationName': 'FeynmanIIICh10Eq19', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'mom', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sqrt(x1**2 + x2**2 + x3**2)', 'derivative_formatted': 'sqrt(x1**2 + x2**2 + x3**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'Bx', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1/sqrt(x1**2 + x2**2 + x3**2)', 'derivative_formatted': 'x0*x1/sqrt(x1**2 + x2**2 + x3**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'By', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2/sqrt(x1**2 + x2**2 + x3**2)', 'derivative_formatted': 'x0*x2/sqrt(x1**2 + x2**2 + x3**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'Bz', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x3/sqrt(x1**2 + x2**2 + x3**2)', 'derivative_formatted': 'x0*x3/sqrt(x1**2 + x2**2 + x3**2)'
      }
    ], 'Variables': ['mom', 'Bx', 'By', 'Bz'
    ]
  },
  {'EquationName': 'FeynmanIIICh12Eq43', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1/(2*pi)', 'derivative_formatted': 'x1/(2*pi)'
      },
      {'var_name': 'x1', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(2*pi)', 'derivative_formatted': 'x0/(2*pi)'
      }
    ], 'Variables': ['n', 'h'
    ]
  },
  {'EquationName': 'FeynmanIIICh13Eq18', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*pi*x1**2*x2/x3', 'derivative_formatted': '4*pi*x1**2*x2/x3'
      },
      {'var_name': 'x1', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '8*pi*x0*x1*x2/x3', 'derivative_formatted': '8*pi*x0*x1*x2/x3'
      },
      {'var_name': 'x2', 'var_display_name': 'k', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*pi*x0*x1**2/x3', 'derivative_formatted': '4*pi*x0*x1**2/x3'
      },
      {'var_name': 'x3', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-4*pi*x0*x1**2*x2/x3**2', 'derivative_formatted': '-4*pi*x0*x1**2*x2/x3**2'
      }
    ], 'Variables': ['E_n', 'd', 'k', 'h'
    ]
  },
  {'EquationName': 'FeynmanIIICh14Eq14', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'I_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'exp(x1*x2/(x3*x4)) - 1', 'derivative_formatted': 'exp(x1*x2/(x3*x4)) - 1'
      },
      {'var_name': 'x1', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2*exp(x1*x2/(x3*x4))/(x3*x4)', 'derivative_formatted': 'x0*x2*exp(x1*x2/(x3*x4))/(x3*x4)'
      },
      {'var_name': 'x2', 'var_display_name': 'Volt', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*exp(x1*x2/(x3*x4))/(x3*x4)', 'derivative_formatted': 'x0*x1*exp(x1*x2/(x3*x4))/(x3*x4)'
      },
      {'var_name': 'x3', 'var_display_name': 'kb', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2*exp(x1*x2/(x3*x4))/(x3**2*x4)', 'derivative_formatted': '-x0*x1*x2*exp(x1*x2/(x3*x4))/(x3**2*x4)'
      },
      {'var_name': 'x4', 'var_display_name': 'T', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1*x2*exp(x1*x2/(x3*x4))/(x3*x4**2)', 'derivative_formatted': '-x0*x1*x2*exp(x1*x2/(x3*x4))/(x3*x4**2)'
      }
    ], 'Variables': ['I_0', 'q', 'Volt', 'kb', 'T'
    ]
  },
  {'EquationName': 'FeynmanIIICh15Eq12', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'U', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2 - 2*cos(x1*x2)', 'derivative_formatted': '2 - 2*cos(x1*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'k', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '2*x0*x2*sin(x1*x2)', 'derivative_formatted': '2*x0*x2*sin(x1*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '2*x0*x1*sin(x1*x2)', 'derivative_formatted': '2*x0*x1*sin(x1*x2)'
      }
    ], 'Variables': ['U', 'k', 'd'
    ]
  },
  {'EquationName': 'FeynmanIIICh15Eq14', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0/(4*pi**2*x1*x2**2)', 'derivative_formatted': 'x0/(4*pi**2*x1*x2**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2/(8*pi**2*x1**2*x2**2)', 'derivative_formatted': '-x0**2/(8*pi**2*x1**2*x2**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2/(4*pi**2*x1*x2**3)', 'derivative_formatted': '-x0**2/(4*pi**2*x1*x2**3)'
      }
    ], 'Variables': ['h', 'E_n', 'd'
    ]
  },
  {'EquationName': 'FeynmanIIICh15Eq27', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*pi/(x1*x2)', 'derivative_formatted': '2*pi/(x1*x2)'
      },
      {'var_name': 'x1', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*pi*x0/(x1**2*x2)', 'derivative_formatted': '-2*pi*x0/(x1**2*x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*pi*x0/(x1*x2**2)', 'derivative_formatted': '-2*pi*x0/(x1*x2**2)'
      }
    ], 'Variables': ['alpha', 'n', 'd'
    ]
  },
  {'EquationName': 'FeynmanIIICh17Eq37', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'beta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*cos(x2) + 1', 'derivative_formatted': 'x1*cos(x2) + 1'
      },
      {'var_name': 'x1', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*cos(x2)', 'derivative_formatted': 'x0*cos(x2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x1*sin(x2)', 'derivative_formatted': '-x0*x1*sin(x2)'
      }
    ], 'Variables': ['beta', 'alpha', 'theta'
    ]
  },
  {'EquationName': 'FeynmanIIICh19Eq51', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1**4/(8*x2**2*x3**2*x4**2)', 'derivative_formatted': '-x1**4/(8*x2**2*x3**2*x4**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**3/(2*x2**2*x3**2*x4**2)', 'derivative_formatted': '-x0*x1**3/(2*x2**2*x3**2*x4**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**4/(4*x2**3*x3**2*x4**2)', 'derivative_formatted': 'x0*x1**4/(4*x2**3*x3**2*x4**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**4/(4*x2**2*x3**3*x4**2)', 'derivative_formatted': 'x0*x1**4/(4*x2**2*x3**3*x4**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**4/(4*x2**2*x3**2*x4**3)', 'derivative_formatted': 'x0*x1**4/(4*x2**2*x3**2*x4**3)'
      }
    ], 'Variables': ['m', 'q', 'h', 'n', 'epsilon'
    ]
  },
  {'EquationName': 'FeynmanIIICh21Eq20', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'rho_c_0', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1*x2/x3', 'derivative_formatted': '-x1*x2/x3'
      },
      {'var_name': 'x1', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x2/x3', 'derivative_formatted': '-x0*x2/x3'
      },
      {'var_name': 'x2', 'var_display_name': 'A_vec', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1/x3', 'derivative_formatted': '-x0*x1/x3'
      },
      {'var_name': 'x3', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x2/x3**2', 'derivative_formatted': 'x0*x1*x2/x3**2'
      }
    ], 'Variables': ['rho_c_0', 'q', 'A_vec', 'm'
    ]
  },
  {'EquationName': 'FeynmanBonus1', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'Z_1', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2*x2**2*x3**2*x4**2/(8*x5**2*sin(x6/2)**4)', 'derivative_formatted': 'x0*x1**2*x2**2*x3**2*x4**2/(8*x5**2*sin(x6/2)**4)'
      },
      {'var_name': 'x1', 'var_display_name': 'Z_2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1*x2**2*x3**2*x4**2/(8*x5**2*sin(x6/2)**4)', 'derivative_formatted': 'x0**2*x1*x2**2*x3**2*x4**2/(8*x5**2*sin(x6/2)**4)'
      },
      {'var_name': 'x2', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1**2*x2*x3**2*x4**2/(8*x5**2*sin(x6/2)**4)', 'derivative_formatted': 'x0**2*x1**2*x2*x3**2*x4**2/(8*x5**2*sin(x6/2)**4)'
      },
      {'var_name': 'x3', 'var_display_name': 'hbar', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1**2*x2**2*x3*x4**2/(8*x5**2*sin(x6/2)**4)', 'derivative_formatted': 'x0**2*x1**2*x2**2*x3*x4**2/(8*x5**2*sin(x6/2)**4)'
      },
      {'var_name': 'x4', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1**2*x2**2*x3**2*x4/(8*x5**2*sin(x6/2)**4)', 'derivative_formatted': 'x0**2*x1**2*x2**2*x3**2*x4/(8*x5**2*sin(x6/2)**4)'
      },
      {'var_name': 'x5', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*x1**2*x2**2*x3**2*x4**2/(8*x5**3*sin(x6/2)**4)', 'derivative_formatted': '-x0**2*x1**2*x2**2*x3**2*x4**2/(8*x5**3*sin(x6/2)**4)'
      },
      {'var_name': 'x6', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*x1**2*x2**2*x3**2*x4**2*cos(x6/2)/(8*x5**2*sin(x6/2)**5)', 'derivative_formatted': '-x0**2*x1**2*x2**2*x3**2*x4**2*cos(x6/2)/(8*x5**2*sin(x6/2)**5)'
      }
    ], 'Variables': ['Z_1', 'Z_2', 'alpha', 'hbar', 'c', 'E_n', 'theta'
    ]
  },
  {'EquationName': 'FeynmanBonus2', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**2 - x3*cos(x4 - x5)/(x0*x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))', 'derivative_formatted': 'x1*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**2 - x3*cos(x4 - x5)/(x0*x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))'
      },
      {'var_name': 'x1', 'var_display_name': 'k_G', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**2 - 2*x3*cos(x4 - x5)/(x1**2*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))', 'derivative_formatted': 'x0*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**2 - 2*x3*cos(x4 - x5)/(x1**2*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))'
      },
      {'var_name': 'x2', 'var_display_name': 'L', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-2*x0*x1*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**3 + 2*x3*cos(x4 - x5)/(x1*x2*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))', 'derivative_formatted': '-2*x0*x1*(sqrt(1 + 2*x2**2*x3/(x0*x1**2))*cos(x4 - x5) + 1)/x2**3 + 2*x3*cos(x4 - x5)/(x1*x2*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))'
      },
      {'var_name': 'x3', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'cos(x4 - x5)/(x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))', 'derivative_formatted': 'cos(x4 - x5)/(x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2)))'
      },
      {'var_name': 'x4', 'var_display_name': 'theta1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2))*sin(x4 - x5)/x2**2', 'derivative_formatted': '-x0*x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2))*sin(x4 - x5)/x2**2'
      },
      {'var_name': 'x5', 'var_display_name': 'theta2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2))*sin(x4 - x5)/x2**2', 'derivative_formatted': 'x0*x1*sqrt(1 + 2*x2**2*x3/(x0*x1**2))*sin(x4 - x5)/x2**2'
      }
    ], 'Variables': ['m', 'k_G', 'L', 'E_n', 'theta1', 'theta2'
    ]
  },
  {'EquationName': 'FeynmanBonus3', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '(1 - x1**2)/(x1*cos(x2 - x3) + 1)', 'derivative_formatted': '(1 - x1**2)/(x1*cos(x2 - x3) + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x0*x1/(x1*cos(x2 - x3) + 1) - x0*(1 - x1**2)*cos(x2 - x3)/(x1*cos(x2 - x3) + 1)**2', 'derivative_formatted': '-2*x0*x1/(x1*cos(x2 - x3) + 1) - x0*(1 - x1**2)*cos(x2 - x3)/(x1*cos(x2 - x3) + 1)**2'
      },
      {'var_name': 'x2', 'var_display_name': 'theta1', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*x1*(1 - x1**2)*sin(x2 - x3)/(x1*cos(x2 - x3) + 1)**2', 'derivative_formatted': 'x0*x1*(1 - x1**2)*sin(x2 - x3)/(x1*cos(x2 - x3) + 1)**2'
      },
      {'var_name': 'x3', 'var_display_name': 'theta2', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x1*(1 - x1**2)*sin(x2 - x3)/(x1*cos(x2 - x3) + 1)**2', 'derivative_formatted': '-x0*x1*(1 - x1**2)*sin(x2 - x3)/(x1*cos(x2 - x3) + 1)**2'
      }
    ], 'Variables': ['d', 'alpha', 'theta1', 'theta2'
    ]
  },
  {'EquationName': 'FeynmanBonus4', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'sqrt(2)*x0*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)*(-(x1 - x2 - x3**2/(2*x0*x4**2))/(2*x0**2) + x3**2/(4*x0**3*x4**2))/(x1 - x2 - x3**2/(2*x0*x4**2))', 'derivative_formatted': 'sqrt(2)*x0*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)*(-(x1 - x2 - x3**2/(2*x0*x4**2))/(2*x0**2) + x3**2/(4*x0**3*x4**2))/(x1 - x2 - x3**2/(2*x0*x4**2))'
      },
      {'var_name': 'x1', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*(x1 - x2 - x3**2/(2*x0*x4**2)))', 'derivative_formatted': 'sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*(x1 - x2 - x3**2/(2*x0*x4**2)))'
      },
      {'var_name': 'x2', 'var_display_name': 'U', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*(x1 - x2 - x3**2/(2*x0*x4**2)))', 'derivative_formatted': '-sqrt(2)*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*(x1 - x2 - x3**2/(2*x0*x4**2)))'
      },
      {'var_name': 'x3', 'var_display_name': 'L', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-sqrt(2)*x3*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**2*(x1 - x2 - x3**2/(2*x0*x4**2)))', 'derivative_formatted': '-sqrt(2)*x3*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**2*(x1 - x2 - x3**2/(2*x0*x4**2)))'
      },
      {'var_name': 'x4', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sqrt(2)*x3**2*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**3*(x1 - x2 - x3**2/(2*x0*x4**2)))', 'derivative_formatted': 'sqrt(2)*x3**2*sqrt((x1 - x2 - x3**2/(2*x0*x4**2))/x0)/(2*x0*x4**3*(x1 - x2 - x3**2/(2*x0*x4**2)))'
      }
    ], 'Variables': ['m', 'E_n', 'U', 'L', 'r'
    ]
  },
  {'EquationName': 'FeynmanBonus5', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3.0*pi*x0**0.5/sqrt(x1*(x2 + x3))', 'derivative_formatted': '3.0*pi*x0**0.5/sqrt(x1*(x2 + x3))'
      },
      {'var_name': 'x1', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '2*pi*x0**1.5*(-x2/2 - x3/2)/(x1*sqrt(x1*(x2 + x3))*(x2 + x3))', 'derivative_formatted': '2*pi*x0**1.5*(-x2/2 - x3/2)/(x1*sqrt(x1*(x2 + x3))*(x2 + x3))'
      },
      {'var_name': 'x2', 'var_display_name': 'm1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-pi*x0**1.5/(sqrt(x1*(x2 + x3))*(x2 + x3))', 'derivative_formatted': '-pi*x0**1.5/(sqrt(x1*(x2 + x3))*(x2 + x3))'
      },
      {'var_name': 'x3', 'var_display_name': 'm2', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-pi*x0**1.5/(sqrt(x1*(x2 + x3))*(x2 + x3))', 'derivative_formatted': '-pi*x0**1.5/(sqrt(x1*(x2 + x3))*(x2 + x3))'
      }
    ], 'Variables': ['d', 'G', 'm1', 'm2'
    ]
  },
  {'EquationName': 'FeynmanBonus6', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0*x1**2*x6/(x2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': '2*x0*x1**2*x6/(x2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      },
      {'var_name': 'x1', 'var_display_name': 'L', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0**2*x1*x6/(x2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': '2*x0**2*x1*x6/(x2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      },
      {'var_name': 'x2', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*x1**2*x6/(x2**2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': '-x0**2*x1**2*x6/(x2**2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      },
      {'var_name': 'x3', 'var_display_name': 'Z_1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x0**2*x1**2*x6/(x2*x3**3*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': '-2*x0**2*x1**2*x6/(x2*x3**3*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      },
      {'var_name': 'x4', 'var_display_name': 'Z_2', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-2*x0**2*x1**2*x6/(x2*x3**2*x4**3*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': '-2*x0**2*x1**2*x6/(x2*x3**2*x4**3*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      },
      {'var_name': 'x5', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-4*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**5*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': '-4*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**5*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      },
      {'var_name': 'x6', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*x1**2/(x2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))', 'derivative_formatted': 'x0**2*x1**2/(x2*x3**2*x4**2*x5**4*sqrt(2*x0**2*x1**2*x6/(x2*x3**2*x4**2*x5**4) + 1))'
      }
    ], 'Variables': ['epsilon', 'L', 'm', 'Z_1', 'Z_2', 'q', 'E_n'
    ]
  },
  {'EquationName': 'FeynmanBonus7', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*pi*x1/(3*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))', 'derivative_formatted': '4*pi*x1/(3*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))'
      },
      {'var_name': 'x1', 'var_display_name': 'rho', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*pi*x0/(3*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))', 'derivative_formatted': '4*pi*x0/(3*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))'
      },
      {'var_name': 'x2', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x3**2/(2*x4**2*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))', 'derivative_formatted': '-x3**2/(2*x4**2*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))'
      },
      {'var_name': 'x3', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x2*x3/(x4**2*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))', 'derivative_formatted': '-x2*x3/(x4**2*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))'
      },
      {'var_name': 'x4', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2*x3**2/(x4**3*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))', 'derivative_formatted': 'x2*x3**2/(x4**3*sqrt(8*pi*x0*x1/3 - x2*x3**2/x4**2))'
      }
    ], 'Variables': ['G', 'rho', 'alpha', 'c', 'd'
    ]
  },
  {'EquationName': 'FeynmanBonus8', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'E_n', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-x0*(1 - cos(x3))/(x1*x2**2*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2) + 1/(x0*(1 - cos(x3))/(x1*x2**2) + 1)', 'derivative_formatted': '-x0*(1 - cos(x3))/(x1*x2**2*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2) + 1/(x0*(1 - cos(x3))/(x1*x2**2) + 1)'
      },
      {'var_name': 'x1', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0**2*(1 - cos(x3))/(x1**2*x2**2*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2)', 'derivative_formatted': 'x0**2*(1 - cos(x3))/(x1**2*x2**2*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '2*x0**2*(1 - cos(x3))/(x1*x2**3*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2)', 'derivative_formatted': '2*x0**2*(1 - cos(x3))/(x1*x2**3*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0**2*sin(x3)/(x1*x2**2*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2)', 'derivative_formatted': '-x0**2*sin(x3)/(x1*x2**2*(x0*(1 - cos(x3))/(x1*x2**2) + 1)**2)'
      }
    ], 'Variables': ['E_n', 'm', 'c', 'theta'
    ]
  },
  {'EquationName': 'FeynmanBonus9', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-25.6*x0**3*x2**2*x3**2*(x2 + x3)/(x1**5*x4**5)', 'derivative_formatted': '-25.6*x0**3*x2**2*x3**2*(x2 + x3)/(x1**5*x4**5)'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '32.0*x0**4*x2**2*x3**2*(x2 + x3)/(x1**6*x4**5)', 'derivative_formatted': '32.0*x0**4*x2**2*x3**2*(x2 + x3)/(x1**6*x4**5)'
      },
      {'var_name': 'x2', 'var_display_name': 'm1', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-6.4*x0**4*x2**2*x3**2/(x1**5*x4**5) - 12.8*x0**4*x2*x3**2*(x2 + x3)/(x1**5*x4**5)', 'derivative_formatted': '-6.4*x0**4*x2**2*x3**2/(x1**5*x4**5) - 12.8*x0**4*x2*x3**2*(x2 + x3)/(x1**5*x4**5)'
      },
      {'var_name': 'x3', 'var_display_name': 'm2', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-6.4*x0**4*x2**2*x3**2/(x1**5*x4**5) - 12.8*x0**4*x2**2*x3*(x2 + x3)/(x1**5*x4**5)', 'derivative_formatted': '-6.4*x0**4*x2**2*x3**2/(x1**5*x4**5) - 12.8*x0**4*x2**2*x3*(x2 + x3)/(x1**5*x4**5)'
      },
      {'var_name': 'x4', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '32.0*x0**4*x2**2*x3**2*(x2 + x3)/(x1**5*x4**6)', 'derivative_formatted': '32.0*x0**4*x2**2*x3**2*(x2 + x3)/(x1**5*x4**6)'
      }
    ], 'Variables': ['G', 'c', 'm1', 'm2', 'r'
    ]
  },
  {'EquationName': 'FeynmanBonus10', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-(x1/(x0**2*(1 - x1*cos(x2)/x0)) - x1*(cos(x2) - x1/x0)*cos(x2)/(x0**2*(1 - x1*cos(x2)/x0)**2))/sqrt(1 - (cos(x2) - x1/x0)**2/(1 - x1*cos(x2)/x0)**2)', 'derivative_formatted': '-(x1/(x0**2*(1 - x1*cos(x2)/x0)) - x1*(cos(x2) - x1/x0)*cos(x2)/(x0**2*(1 - x1*cos(x2)/x0)**2))/sqrt(1 - (cos(x2) - x1/x0)**2/(1 - x1*cos(x2)/x0)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-(-1/(x0*(1 - x1*cos(x2)/x0)) + (cos(x2) - x1/x0)*cos(x2)/(x0*(1 - x1*cos(x2)/x0)**2))/sqrt(1 - (cos(x2) - x1/x0)**2/(1 - x1*cos(x2)/x0)**2)', 'derivative_formatted': '-(-1/(x0*(1 - x1*cos(x2)/x0)) + (cos(x2) - x1/x0)*cos(x2)/(x0*(1 - x1*cos(x2)/x0)**2))/sqrt(1 - (cos(x2) - x1/x0)**2/(1 - x1*cos(x2)/x0)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'theta2', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-(-sin(x2)/(1 - x1*cos(x2)/x0) - x1*(cos(x2) - x1/x0)*sin(x2)/(x0*(1 - x1*cos(x2)/x0)**2))/sqrt(1 - (cos(x2) - x1/x0)**2/(1 - x1*cos(x2)/x0)**2)', 'derivative_formatted': '-(-sin(x2)/(1 - x1*cos(x2)/x0) - x1*(cos(x2) - x1/x0)*sin(x2)/(x0*(1 - x1*cos(x2)/x0)**2))/sqrt(1 - (cos(x2) - x1/x0)**2/(1 - x1*cos(x2)/x0)**2)'
      }
    ], 'Variables': ['c', 'v', 'theta2'
    ]
  },
  {'EquationName': 'FeynmanBonus11', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'I_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '4*sin(x1/2)**2*sin(x2*x3/2)**2/(x1**2*sin(x2/2)**2)', 'derivative_formatted': '4*sin(x1/2)**2*sin(x2*x3/2)**2/(x1**2*sin(x2/2)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '4*x0*sin(x1/2)*sin(x2*x3/2)**2*cos(x1/2)/(x1**2*sin(x2/2)**2) - 8*x0*sin(x1/2)**2*sin(x2*x3/2)**2/(x1**3*sin(x2/2)**2)', 'derivative_formatted': '4*x0*sin(x1/2)*sin(x2*x3/2)**2*cos(x1/2)/(x1**2*sin(x2/2)**2) - 8*x0*sin(x1/2)**2*sin(x2*x3/2)**2/(x1**3*sin(x2/2)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'delta', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '4*x0*x3*sin(x1/2)**2*sin(x2*x3/2)*cos(x2*x3/2)/(x1**2*sin(x2/2)**2) - 4*x0*sin(x1/2)**2*sin(x2*x3/2)**2*cos(x2/2)/(x1**2*sin(x2/2)**3)', 'derivative_formatted': '4*x0*x3*sin(x1/2)**2*sin(x2*x3/2)*cos(x2*x3/2)/(x1**2*sin(x2/2)**2) - 4*x0*sin(x1/2)**2*sin(x2*x3/2)**2*cos(x2/2)/(x1**2*sin(x2/2)**3)'
      },
      {'var_name': 'x3', 'var_display_name': 'n', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '4*x0*x2*sin(x1/2)**2*sin(x2*x3/2)*cos(x2*x3/2)/(x1**2*sin(x2/2)**2)', 'derivative_formatted': '4*x0*x2*sin(x1/2)**2*sin(x2*x3/2)*cos(x2*x3/2)/(x1**2*sin(x2/2)**2)'
      }
    ], 'Variables': ['I_0', 'alpha', 'delta', 'n'
    ]
  },
  {'EquationName': 'FeynmanBonus12', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-x0*x1*x3/(4*pi*x4*(x1**2 - x3**2)**2) + (-x0*x1**3*x3/(x1**2 - x3**2)**2 + 4*pi*x2*x3*x4)/(4*pi*x1**2*x4)', 'derivative_formatted': '-x0*x1*x3/(4*pi*x4*(x1**2 - x3**2)**2) + (-x0*x1**3*x3/(x1**2 - x3**2)**2 + 4*pi*x2*x3*x4)/(4*pi*x1**2*x4)'
      },
      {'var_name': 'x1', 'var_display_name': 'y', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*(4*x0*x1**4*x3/(x1**2 - x3**2)**3 - 3*x0*x1**2*x3/(x1**2 - x3**2)**2)/(4*pi*x1**2*x4) - x0*(-x0*x1**3*x3/(x1**2 - x3**2)**2 + 4*pi*x2*x3*x4)/(2*pi*x1**3*x4)', 'derivative_formatted': 'x0*(4*x0*x1**4*x3/(x1**2 - x3**2)**3 - 3*x0*x1**2*x3/(x1**2 - x3**2)**2)/(4*pi*x1**2*x4) - x0*(-x0*x1**3*x3/(x1**2 - x3**2)**2 + 4*pi*x2*x3*x4)/(2*pi*x1**3*x4)'
      },
      {'var_name': 'x2', 'var_display_name': 'Volt', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x3/x1**2', 'derivative_formatted': 'x0*x3/x1**2'
      },
      {'var_name': 'x3', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*(-4*x0*x1**3*x3**2/(x1**2 - x3**2)**3 - x0*x1**3/(x1**2 - x3**2)**2 + 4*pi*x2*x4)/(4*pi*x1**2*x4)', 'derivative_formatted': 'x0*(-4*x0*x1**3*x3**2/(x1**2 - x3**2)**3 - x0*x1**3/(x1**2 - x3**2)**2 + 4*pi*x2*x4)/(4*pi*x1**2*x4)'
      },
      {'var_name': 'x4', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x2*x3/(x1**2*x4) - x0*(-x0*x1**3*x3/(x1**2 - x3**2)**2 + 4*pi*x2*x3*x4)/(4*pi*x1**2*x4**2)', 'derivative_formatted': 'x0*x2*x3/(x1**2*x4) - x0*(-x0*x1**3*x3/(x1**2 - x3**2)**2 + 4*pi*x2*x3*x4)/(4*pi*x1**2*x4**2)'
      }
    ], 'Variables': ['q', 'y', 'Volt', 'd', 'epsilon'
    ]
  },
  {'EquationName': 'FeynmanBonus13', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '1/(4*pi*x4*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))', 'derivative_formatted': '1/(4*pi*x4*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))'
      },
      {'var_name': 'x1', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*(-x1 + x2*cos(x3))/(4*pi*x4*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))', 'derivative_formatted': 'x0*(-x1 + x2*cos(x3))/(4*pi*x4*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))'
      },
      {'var_name': 'x2', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x0*(x1*cos(x3) - x2)/(4*pi*x4*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))', 'derivative_formatted': 'x0*(x1*cos(x3) - x2)/(4*pi*x4*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))'
      },
      {'var_name': 'x3', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*x1*x2*sin(x3)/(4*pi*x4*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))', 'derivative_formatted': '-x0*x1*x2*sin(x3)/(4*pi*x4*(x1**2 - 2*x1*x2*cos(x3) + x2**2)**(3/2))'
      },
      {'var_name': 'x4', 'var_display_name': 'epsilon', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0/(4*pi*x4**2*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))', 'derivative_formatted': '-x0/(4*pi*x4**2*sqrt(x1**2 - 2*x1*x2*cos(x3) + x2**2))'
      }
    ], 'Variables': ['q', 'r', 'd', 'alpha', 'epsilon'
    ]
  },
  {'EquationName': 'FeynmanBonus14', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'Ef', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(-x2 + x3**3*(x4 - 1)/(x2**2*(x4 + 2)))*cos(x1)', 'derivative_formatted': '(-x2 + x3**3*(x4 - 1)/(x2**2*(x4 + 2)))*cos(x1)'
      },
      {'var_name': 'x1', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x0*(-x2 + x3**3*(x4 - 1)/(x2**2*(x4 + 2)))*sin(x1)', 'derivative_formatted': '-x0*(-x2 + x3**3*(x4 - 1)/(x2**2*(x4 + 2)))*sin(x1)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*(-1 - 2*x3**3*(x4 - 1)/(x2**3*(x4 + 2)))*cos(x1)', 'derivative_formatted': 'x0*(-1 - 2*x3**3*(x4 - 1)/(x2**3*(x4 + 2)))*cos(x1)'
      },
      {'var_name': 'x3', 'var_display_name': 'd', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '3*x0*x3**2*(x4 - 1)*cos(x1)/(x2**2*(x4 + 2))', 'derivative_formatted': '3*x0*x3**2*(x4 - 1)*cos(x1)/(x2**2*(x4 + 2))'
      },
      {'var_name': 'x4', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x0*(-x3**3*(x4 - 1)/(x2**2*(x4 + 2)**2) + x3**3/(x2**2*(x4 + 2)))*cos(x1)', 'derivative_formatted': 'x0*(-x3**3*(x4 - 1)/(x2**2*(x4 + 2)**2) + x3**3/(x2**2*(x4 + 2)))*cos(x1)'
      }
    ], 'Variables': ['Ef', 'theta', 'r', 'd', 'alpha'
    ]
  },
  {'EquationName': 'FeynmanBonus15', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*x2*sqrt(1 - x1**2/x0**2)*cos(x3)/(x0**2*(1 + x1*cos(x3)/x0)**2) + x1**2*x2/(x0**3*sqrt(1 - x1**2/x0**2)*(1 + x1*cos(x3)/x0))', 'derivative_formatted': 'x1*x2*sqrt(1 - x1**2/x0**2)*cos(x3)/(x0**2*(1 + x1*cos(x3)/x0)**2) + x1**2*x2/(x0**3*sqrt(1 - x1**2/x0**2)*(1 + x1*cos(x3)/x0))'
      },
      {'var_name': 'x1', 'var_display_name': 'v', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x2*sqrt(1 - x1**2/x0**2)*cos(x3)/(x0*(1 + x1*cos(x3)/x0)**2) - x1*x2/(x0**2*sqrt(1 - x1**2/x0**2)*(1 + x1*cos(x3)/x0))', 'derivative_formatted': '-x2*sqrt(1 - x1**2/x0**2)*cos(x3)/(x0*(1 + x1*cos(x3)/x0)**2) - x1*x2/(x0**2*sqrt(1 - x1**2/x0**2)*(1 + x1*cos(x3)/x0))'
      },
      {'var_name': 'x2', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'sqrt(1 - x1**2/x0**2)/(1 + x1*cos(x3)/x0)', 'derivative_formatted': 'sqrt(1 - x1**2/x0**2)/(1 + x1*cos(x3)/x0)'
      },
      {'var_name': 'x3', 'var_display_name': 'theta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1*x2*sqrt(1 - x1**2/x0**2)*sin(x3)/(x0*(1 + x1*cos(x3)/x0)**2)', 'derivative_formatted': 'x1*x2*sqrt(1 - x1**2/x0**2)*sin(x3)/(x0*(1 + x1*cos(x3)/x0)**2)'
      }
    ], 'Variables': ['c', 'v', 'omega', 'theta'
    ]
  },
  {'EquationName': 'FeynmanBonus16', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**4/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2)', 'derivative_formatted': 'x0*x1**4/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '(2*x0**2*x1**3 + x1*(x2 - x3*x4)**2)/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2)', 'derivative_formatted': '(2*x0**2*x1**3 + x1*(x2 - x3*x4)**2)/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'p', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1**2*(2*x2 - 2*x3*x4)/(2*sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2))', 'derivative_formatted': 'x1**2*(2*x2 - 2*x3*x4)/(2*sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2))'
      },
      {'var_name': 'x3', 'var_display_name': 'q', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1**2*x4*(x2 - x3*x4)/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2) + x5', 'derivative_formatted': '-x1**2*x4*(x2 - x3*x4)/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2) + x5'
      },
      {'var_name': 'x4', 'var_display_name': 'A_vec', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1**2*x3*(x2 - x3*x4)/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2)', 'derivative_formatted': '-x1**2*x3*(x2 - x3*x4)/sqrt(x0**2*x1**4 + x1**2*(x2 - x3*x4)**2)'
      },
      {'var_name': 'x5', 'var_display_name': 'Volt', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x3', 'derivative_formatted': 'x3'
      }
    ], 'Variables': ['m', 'c', 'p', 'q', 'A_vec', 'Volt'
    ]
  },
  {'EquationName': 'FeynmanBonus17', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'None', 'derivative': 'x1**2*x4**2*(1 + x4*x5/x3) - (x0**2*x1**2*x4**2*(1 + x4*x5/x3) + x2**2)/(2*x0**2)', 'derivative_formatted': 'x1**2*x4**2*(1 + x4*x5/x3) - (x0**2*x1**2*x4**2*(1 + x4*x5/x3) + x2**2)/(2*x0**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1*x4**2*(1 + x4*x5/x3)', 'derivative_formatted': 'x0*x1*x4**2*(1 + x4*x5/x3)'
      },
      {'var_name': 'x2', 'var_display_name': 'p', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x2/x0', 'derivative_formatted': 'x2/x0'
      },
      {'var_name': 'x3', 'var_display_name': 'y', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x0*x1**2*x4**3*x5/(2*x3**2)', 'derivative_formatted': '-x0*x1**2*x4**3*x5/(2*x3**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'x', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '(2*x0**2*x1**2*x4*(1 + x4*x5/x3) + x0**2*x1**2*x4**2*x5/x3)/(2*x0)', 'derivative_formatted': '(2*x0**2*x1**2*x4*(1 + x4*x5/x3) + x0**2*x1**2*x4**2*x5/x3)/(2*x0)'
      },
      {'var_name': 'x5', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x0*x1**2*x4**3/(2*x3)', 'derivative_formatted': 'x0*x1**2*x4**3/(2*x3)'
      }
    ], 'Variables': ['m', 'omega', 'p', 'y', 'x', 'alpha'
    ]
  },
  {'EquationName': 'FeynmanBonus18', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-3*(x1*x4**2/x2**2 + x3**2)/(8*pi*x0**2)', 'derivative_formatted': '-3*(x1*x4**2/x2**2 + x3**2)/(8*pi*x0**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'k_f', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x4**2/(8*pi*x0*x2**2)', 'derivative_formatted': '3*x4**2/(8*pi*x0*x2**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-3*x1*x4**2/(4*pi*x0*x2**3)', 'derivative_formatted': '-3*x1*x4**2/(4*pi*x0*x2**3)'
      },
      {'var_name': 'x3', 'var_display_name': 'H_G', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x3/(4*pi*x0)', 'derivative_formatted': '3*x3/(4*pi*x0)'
      },
      {'var_name': 'x4', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '3*x1*x4/(4*pi*x0*x2**2)', 'derivative_formatted': '3*x1*x4/(4*pi*x0*x2**2)'
      }
    ], 'Variables': ['G', 'k_f', 'r', 'H_G', 'c'
    ]
  },
  {'EquationName': 'FeynmanBonus19', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'G', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '(x1*x5**4/x2**2 + x3**2*x5**2*(1 - 2*x4))/(8*pi*x0**2)', 'derivative_formatted': '(x1*x5**4/x2**2 + x3**2*x5**2*(1 - 2*x4))/(8*pi*x0**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'k_f', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x5**4/(8*pi*x0*x2**2)', 'derivative_formatted': '-x5**4/(8*pi*x0*x2**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'r', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1*x5**4/(4*pi*x0*x2**3)', 'derivative_formatted': 'x1*x5**4/(4*pi*x0*x2**3)'
      },
      {'var_name': 'x3', 'var_display_name': 'H_G', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': '-x3*x5**2*(1 - 2*x4)/(4*pi*x0)', 'derivative_formatted': '-x3*x5**2*(1 - 2*x4)/(4*pi*x0)'
      },
      {'var_name': 'x4', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x3**2*x5**2/(4*pi*x0)', 'derivative_formatted': 'x3**2*x5**2/(4*pi*x0)'
      },
      {'var_name': 'x5', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-(4*x1*x5**3/x2**2 + 2*x3**2*x5*(1 - 2*x4))/(8*pi*x0)', 'derivative_formatted': '-(4*x1*x5**3/x2**2 + 2*x3**2*x5*(1 - 2*x4))/(8*pi*x0)'
      }
    ], 'Variables': ['G', 'k_f', 'r', 'H_G', 'alpha', 'c'
    ]
  },
  {'EquationName': 'FeynmanBonus20', 'Constraints': [
      {'var_name': 'x0', 'var_display_name': 'omega', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': 'x1**2*x2**2*x3**2*(1/x1 - x1/x0**2)/(4*pi*x0**2*x4**2*x5**2) - x1**2*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**3*x4**2*x5**2)', 'derivative_formatted': 'x1**2*x2**2*x3**2*(1/x1 - x1/x0**2)/(4*pi*x0**2*x4**2*x5**2) - x1**2*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**3*x4**2*x5**2)'
      },
      {'var_name': 'x1', 'var_display_name': 'omega_0', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1**2*x2**2*x3**2*(-x0/x1**2 + 1/x0)/(4*pi*x0**2*x4**2*x5**2) + x1*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**2)', 'derivative_formatted': 'x1**2*x2**2*x3**2*(-x0/x1**2 + 1/x0)/(4*pi*x0**2*x4**2*x5**2) + x1*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**2)'
      },
      {'var_name': 'x2', 'var_display_name': 'alpha', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1**2*x2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**2)', 'derivative_formatted': 'x1**2*x2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**2)'
      },
      {'var_name': 'x3', 'var_display_name': 'h', 'order_derivative': 1, 'descriptor': 'monotonic increasing', 'derivative': 'x1**2*x2**2*x3*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**2)', 'derivative_formatted': 'x1**2*x2**2*x3*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**2)'
      },
      {'var_name': 'x4', 'var_display_name': 'm', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1**2*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**3*x5**2)', 'derivative_formatted': '-x1**2*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**3*x5**2)'
      },
      {'var_name': 'x5', 'var_display_name': 'c', 'order_derivative': 1, 'descriptor': 'monotonic decreasing', 'derivative': '-x1**2*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**3)', 'derivative_formatted': '-x1**2*x2**2*x3**2*(x0/x1 - sin(x6)**2 + x1/x0)/(2*pi*x0**2*x4**2*x5**3)'
      },
      {'var_name': 'x6', 'var_display_name': 'beta', 'order_derivative': 1, 'descriptor': 'None', 'derivative': '-x1**2*x2**2*x3**2*sin(x6)*cos(x6)/(2*pi*x0**2*x4**2*x5**2)', 'derivative_formatted': '-x1**2*x2**2*x3**2*sin(x6)*cos(x6)/(2*pi*x0**2*x4**2*x5**2)'
      }
    ], 'Variables': ['omega', 'omega_0', 'alpha', 'h', 'm', 'c', 'beta'
    ]
  },
]