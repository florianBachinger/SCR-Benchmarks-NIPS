
"""

"""

AIF_EQUATION_CONFIG_DICT = {

    "FeynmanICh6Eq20a": {
        "EquationRaw" : "exp(-theta**2/2)/sqrt(2*pi)",
        "variables" : ["theta"],
        "output" : "f"
    },
  
    "FeynmanICh6Eq20": {
        "EquationRaw" : "exp(-(theta/sigma)**2/2)/(sqrt(2*pi)*sigma)",
        "variables" : ["sigma","theta"],
        "output" : "f"
    },
  
    "FeynmanICh6Eq20b": {
        "EquationRaw" : "exp(-((theta-theta1)/sigma)**2/2)/(sqrt(2*pi)*sigma)",
        "variables" : ["sigma","theta","theta1"],
        "output" : "f"
    },
  
    "FeynmanICh8Eq14": {
        "EquationRaw" : "sqrt((x2-x1)**2+(y2-y1)**2)",
        "variables" : ["x1","x2","y1","y2"],
        "output" : "d"
    },
  
    "FeynmanICh9Eq18": {
        "EquationRaw" : "G*m1*m2/((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)",
        "variables" : ["m1","m2","G","x1","x2","y1","y2","z1","z2"],
        "output" : "F"
    },
  
    "FeynmanICh10Eq7": {
        "EquationRaw" : "m_0/sqrt(1-v**2/c**2)",
        "variables" : ["m_0","v","c"],
        "output" : "m"
    },
  
    "FeynmanICh11Eq19": {
        "EquationRaw" : "x1*y1+x2*y2+x3*y3",
        "variables" : ["x1","x2","x3","y1","y2","y3"],
        "output" : "A"
    },
  
    "FeynmanICh12Eq1": {
        "EquationRaw" : "mu*Nn",
        "variables" : ["mu","Nn"],
        "output" : "F"
    },
  
    "FeynmanICh12Eq2": {
        "EquationRaw" : "q1*q2*r/(4*pi*epsilon*r**3)",
        "variables" : ["q1","q2","epsilon","r"],
        "output" : "F"
    },
  
    "FeynmanICh12Eq4": {
        "EquationRaw" : "q1*r/(4*pi*epsilon*r**3)",
        "variables" : ["q1","epsilon","r"],
        "output" : "Ef"
    },
  
    "FeynmanICh12Eq5": {
        "EquationRaw" : "q2*Ef",
        "variables" : ["q2","Ef"],
        "output" : "F"
    },
  
    "FeynmanICh12Eq11": {
        "EquationRaw" : "q*(Ef+B*v*sin(theta))",
        "variables" : ["q","Ef","B","v","theta"],
        "output" : "F"
    },
  
    "FeynmanICh13Eq4": {
        "EquationRaw" : "1/2*m*(v**2+u**2+w**2)",
        "variables" : ["m","v","u","w"],
        "output" : "K"
    },
  
    "FeynmanICh13Eq12": {
        "EquationRaw" : "G*m1*m2*(1/r2-1/r1)",
        "variables" : ["m1","m2","r1","r2","G"],
        "output" : "U"
    },
  
    "FeynmanICh14Eq3": {
        "EquationRaw" : "m*g*z",
        "variables" : ["m","g","z"],
        "output" : "U"
    },
  
    "FeynmanICh14Eq4": {
        "EquationRaw" : "1/2*k_spring*x**2",
        "variables" : ["k_spring","x"],
        "output" : "U"
    },
  
    "FeynmanICh15Eq3x": {
        "EquationRaw" : "(x-u*t)/sqrt(1-u**2/c**2)",
        "variables" : ["x","u","c","t"],
        "output" : "x1"
    },
  
    "FeynmanICh15Eq3t": {
        "EquationRaw" : "(t-u*x/c**2)/sqrt(1-u**2/c**2)",
        "variables" : ["x","c","u","t"],
        "output" : "t1"
    },
  
    "FeynmanICh15Eq10": {
        "EquationRaw" : "m_0*v/sqrt(1-v**2/c**2)",
        "variables" : ["m_0","v","c"],
        "output" : "p"
    },
  
    "FeynmanICh16Eq6": {
        "EquationRaw" : "(u+v)/(1+u*v/c**2)",
        "variables" : ["c","v","u"],
        "output" : "v1"
    },
  
    "FeynmanICh18Eq4": {
        "EquationRaw" : "(m1*r1+m2*r2)/(m1+m2)",
        "variables" : ["m1","m2","r1","r2"],
        "output" : "r"
    },
  
    "FeynmanICh18Eq12": {
        "EquationRaw" : "r*F*sin(theta)",
        "variables" : ["r","F","theta"],
        "output" : "tau"
    },
  
    "FeynmanICh18Eq16": {
        "EquationRaw" : "m*r*v*sin(theta)",
        "variables" : ["m","r","v","theta"],
        "output" : "L"
    },
  
    "FeynmanICh24Eq6": {
        "EquationRaw" : "1/2*m*(omega**2+omega_0**2)*1/2*x**2",
        "variables" : ["m","omega","omega_0","x"],
        "output" : "E_n"
    },
  
    "FeynmanICh25Eq13": {
        "EquationRaw" : "q/C",
        "variables" : ["q","C"],
        "output" : "Volt"
    },
  
    "FeynmanICh26Eq2": {
        "EquationRaw" : "arcsin(n*sin(theta2))",
        "variables" : ["n","theta2"],
        "output" : "theta1"
    },
  
    "FeynmanICh27Eq6": {
        "EquationRaw" : "1/(1/d1+n/d2)",
        "variables" : ["d1","d2","n"],
        "output" : "foc"
    },
  
    "FeynmanICh29Eq4": {
        "EquationRaw" : "omega/c",
        "variables" : ["omega","c"],
        "output" : "k"
    },
  
    "FeynmanICh29Eq16": {
        "EquationRaw" : "sqrt(x1**2+x2**2-2*x1*x2*cos(theta1-theta2))",
        "variables" : ["x1","x2","theta1","theta2"],
        "output" : "x"
    },
  
    "FeynmanICh30Eq3": {
        "EquationRaw" : "Int_0*sin(n*theta/2)**2/sin(theta/2)**2",
        "variables" : ["Int_0","theta","n"],
        "output" : "Int"
    },
  
    "FeynmanICh30Eq5": {
        "EquationRaw" : "arcsin(lambd/(n*d))",
        "variables" : ["lambd","d","n"],
        "output" : "theta"
    },
  
    "FeynmanICh32Eq5": {
        "EquationRaw" : "q**2*a**2/(6*pi*epsilon*c**3)",
        "variables" : ["q","a","epsilon","c"],
        "output" : "Pwr"
    },
  
    "FeynmanICh32Eq17": {
        "EquationRaw" : "(1/2*epsilon*c*Ef**2)*(8*pi*r**2/3)*(omega**4/(omega**2-omega_0**2)**2)",
        "variables" : ["epsilon","c","Ef","r","omega","omega_0"],
        "output" : "Pwr"
    },
  
    "FeynmanICh34Eq8": {
        "EquationRaw" : "q*v*B/p",
        "variables" : ["q","v","B","p"],
        "output" : "omega"
    },
  
    "FeynmanICh34Eq10": {
        "EquationRaw" : "omega_0/(1-v/c)",
        "variables" : ["c","v","omega_0"],
        "output" : "omega"
    },
  
    "FeynmanICh34Eq14": {
        "EquationRaw" : "(1+v/c)/sqrt(1-v**2/c**2)*omega_0",
        "variables" : ["c","v","omega_0"],
        "output" : "omega"
    },
  
    "FeynmanICh34Eq27": {
        "EquationRaw" : "(h/(2*pi))*omega",
        "variables" : ["omega","h"],
        "output" : "E_n"
    },
  
    "FeynmanICh37Eq4": {
        "EquationRaw" : "I1+I2+2*sqrt(I1*I2)*cos(delta)",
        "variables" : ["I1","I2","delta"],
        "output" : "Int"
    },
  
    "FeynmanICh38Eq12": {
        "EquationRaw" : "4*pi*epsilon*(h/(2*pi))**2/(m*q**2)",
        "variables" : ["m","q","h","epsilon"],
        "output" : "r"
    },
  
    "FeynmanICh39Eq10": {
        "EquationRaw" : "3/2*pr*V",
        "variables" : ["pr","V"],
        "output" : "E_n"
    },
  
    "FeynmanICh39Eq11": {
        "EquationRaw" : "1/(gamma-1)*pr*V",
        "variables" : ["gamma","pr","V"],
        "output" : "E_n"
    },
  
    "FeynmanICh39Eq22": {
        "EquationRaw" : "n*kb*T/V",
        "variables" : ["n","T","V","kb"],
        "output" : "pr"
    },
  
    "FeynmanICh40Eq1": {
        "EquationRaw" : "n_0*exp(-m*g*x/(kb*T))",
        "variables" : ["n_0","m","x","T","g","kb"],
        "output" : "n"
    },
  
    "FeynmanICh41Eq16": {
        "EquationRaw" : "h/(2*pi)*omega**3/(pi**2*c**2*(exp((h/(2*pi))*omega/(kb*T))-1))",
        "variables" : ["omega","T","h","kb","c"],
        "output" : "L_rad"
    },
  
    "FeynmanICh43Eq16": {
        "EquationRaw" : "mu_drift*q*Volt/d",
        "variables" : ["mu_drift","q","Volt","d"],
        "output" : "v"
    },
  
    "FeynmanICh43Eq31": {
        "EquationRaw" : "mob*kb*T",
        "variables" : ["mob","T","kb"],
        "output" : "D"
    },
  
    "FeynmanICh43Eq43": {
        "EquationRaw" : "1/(gamma-1)*kb*v/A",
        "variables" : ["gamma","kb","A","v"],
        "output" : "kappa"
    },
  
    "FeynmanICh44Eq4": {
        "EquationRaw" : "n*kb*T*ln(V2/V1)",
        "variables" : ["n","kb","T","V1","V2"],
        "output" : "E_n"
    },
  
    "FeynmanICh47Eq23": {
        "EquationRaw" : "sqrt(gamma*pr/rho)",
        "variables" : ["gamma","pr","rho"],
        "output" : "c"
    },
  
    "FeynmanICh48Eq2": {
        "EquationRaw" : "m*c**2/sqrt(1-v**2/c**2)",
        "variables" : ["m","v","c"],
        "output" : "E_n"
    },
  
    "FeynmanICh50Eq26": {
        "EquationRaw" : "x1*(cos(omega*t)+alpha*cos(omega*t)**2)",
        "variables" : ["x1","omega","t","alpha"],
        "output" : "x"
    },
  
    "FeynmanIICh2Eq42": {
        "EquationRaw" : "kappa*(T2-T1)*A/d",
        "variables" : ["kappa","T1","T2","A","d"],
        "output" : "Pwr"
    },
  
    "FeynmanIICh3Eq24": {
        "EquationRaw" : "Pwr/(4*pi*r**2)",
        "variables" : ["Pwr","r"],
        "output" : "flux"
    },
  
    "FeynmanIICh4Eq23": {
        "EquationRaw" : "q/(4*pi*epsilon*r)",
        "variables" : ["q","epsilon","r"],
        "output" : "Volt"
    },
  
    "FeynmanIICh6Eq11": {
        "EquationRaw" : "1/(4*pi*epsilon)*p_d*cos(theta)/r**2",
        "variables" : ["epsilon","p_d","theta","r"],
        "output" : "Volt"
    },
  
    "FeynmanIICh6Eq15a": {
        "EquationRaw" : "p_d/(4*pi*epsilon)*3*z/r**5*sqrt(x**2+y**2)",
        "variables" : ["epsilon","p_d","r","x","y","z"],
        "output" : "Ef"
    },
  
    "FeynmanIICh6Eq15b": {
        "EquationRaw" : "p_d/(4*pi*epsilon)*3*cos(theta)*sin(theta)/r**3",
        "variables" : ["epsilon","p_d","theta","r"],
        "output" : "Ef"
    },
  
    "FeynmanIICh8Eq7": {
        "EquationRaw" : "3/5*q**2/(4*pi*epsilon*d)",
        "variables" : ["q","epsilon","d"],
        "output" : "E_n"
    },
  
    "FeynmanIICh8Eq31": {
        "EquationRaw" : "epsilon*Ef**2/2",
        "variables" : ["epsilon","Ef"],
        "output" : "E_den"
    },
  
    "FeynmanIICh10Eq9": {
        "EquationRaw" : "sigma_den/epsilon*1/(1+chi)",
        "variables" : ["sigma_den","epsilon","chi"],
        "output" : "Ef"
    },
  
    "FeynmanIICh11Eq3": {
        "EquationRaw" : "q*Ef/(m*(omega_0**2-omega**2))",
        "variables" : ["q","Ef","m","omega_0","omega"],
        "output" : "x"
    },
  
    "FeynmanIICh11Eq17": {
        "EquationRaw" : "n_0*(1+p_d*Ef*cos(theta)/(kb*T))",
        "variables" : ["n_0","kb","T","theta","p_d","Ef"],
        "output" : "n"
    },
  
    "FeynmanIICh11Eq20": {
        "EquationRaw" : "n_rho*p_d**2*Ef/(3*kb*T)",
        "variables" : ["n_rho","p_d","Ef","kb","T"],
        "output" : "Pol"
    },
  
    "FeynmanIICh11Eq27": {
        "EquationRaw" : "n*alpha/(1-(n*alpha/3))*epsilon*Ef",
        "variables" : ["n","alpha","epsilon","Ef"],
        "output" : "Pol"
    },
  
    "FeynmanIICh11Eq28": {
        "EquationRaw" : "1+n*alpha/(1-(n*alpha/3))",
        "variables" : ["n","alpha"],
        "output" : "theta"
    },
  
    "FeynmanIICh13Eq17": {
        "EquationRaw" : "1/(4*pi*epsilon*c**2)*2*I/r",
        "variables" : ["epsilon","c","I","r"],
        "output" : "B"
    },
  
    "FeynmanIICh13Eq23": {
        "EquationRaw" : "rho_c_0/sqrt(1-v**2/c**2)",
        "variables" : ["rho_c_0","v","c"],
        "output" : "rho_c"
    },
  
    "FeynmanIICh13Eq34": {
        "EquationRaw" : "rho_c_0*v/sqrt(1-v**2/c**2)",
        "variables" : ["rho_c_0","v","c"],
        "output" : "j"
    },
  
    "FeynmanIICh15Eq4": {
        "EquationRaw" : "-mom*B*cos(theta)",
        "variables" : ["mom","B","theta"],
        "output" : "E_n"
    },
  
    "FeynmanIICh15Eq5": {
        "EquationRaw" : "-p_d*Ef*cos(theta)",
        "variables" : ["p_d","Ef","theta"],
        "output" : "E_n"
    },
  
    "FeynmanIICh21Eq32": {
        "EquationRaw" : "q/(4*pi*epsilon*r*(1-v/c))",
        "variables" : ["q","epsilon","r","v","c"],
        "output" : "Volt"
    },
  
    "FeynmanIICh24Eq17": {
        "EquationRaw" : "sqrt(omega**2/c**2-pi**2/d**2)",
        "variables" : ["omega","c","d"],
        "output" : "k"
    },
  
    "FeynmanIICh27Eq16": {
        "EquationRaw" : "epsilon*c*Ef**2",
        "variables" : ["epsilon","c","Ef"],
        "output" : "flux"
    },
  
    "FeynmanIICh27Eq18": {
        "EquationRaw" : "epsilon*Ef**2",
        "variables" : ["epsilon","Ef"],
        "output" : "E_den"
    },
  
    "FeynmanIICh34Eq2a": {
        "EquationRaw" : "q*v/(2*pi*r)",
        "variables" : ["q","v","r"],
        "output" : "I"
    },
  
    "FeynmanIICh34Eq2": {
        "EquationRaw" : "q*v*r/2",
        "variables" : ["q","v","r"],
        "output" : "mom"
    },
  
    "FeynmanIICh34Eq11": {
        "EquationRaw" : "g_*q*B/(2*m)",
        "variables" : ["g_","q","B","m"],
        "output" : "omega"
    },
  
    "FeynmanIICh34Eq29a": {
        "EquationRaw" : "q*h/(4*pi*m)",
        "variables" : ["q","h","m"],
        "output" : "mom"
    },
  
    "FeynmanIICh34Eq29b": {
        "EquationRaw" : "g_*mom*B*Jz/(h/(2*pi))",
        "variables" : ["g_","h","Jz","mom","B"],
        "output" : "E_n"
    },
  
    "FeynmanIICh35Eq18": {
        "EquationRaw" : "n_0/(exp(mom*B/(kb*T))+exp(-mom*B/(kb*T)))",
        "variables" : ["n_0","kb","T","mom","B"],
        "output" : "n"
    },
  
    "FeynmanIICh35Eq21": {
        "EquationRaw" : "n_rho*mom*tanh(mom*B/(kb*T))",
        "variables" : ["n_rho","mom","B","kb","T"],
        "output" : "M"
    },
  
    "FeynmanIICh36Eq38": {
        "EquationRaw" : "mom*H/(kb*T)+(mom*alpha)/(epsilon*c**2*kb*T)*M",
        "variables" : ["mom","H","kb","T","alpha","epsilon","c","M"],
        "output" : "f"
    },
  
    "FeynmanIICh37Eq1": {
        "EquationRaw" : "mom*(1+chi)*B",
        "variables" : ["mom","B","chi"],
        "output" : "E_n"
    },
  
    "FeynmanIICh38Eq3": {
        "EquationRaw" : "Y*A*x/d",
        "variables" : ["Y","A","d","x"],
        "output" : "F"
    },
  
    "FeynmanIICh38Eq14": {
        "EquationRaw" : "Y/(2*(1+sigma))",
        "variables" : ["Y","sigma"],
        "output" : "mu_S"
    },
  
    "FeynmanIIICh4Eq32": {
        "EquationRaw" : "1/(exp((h/(2*pi))*omega/(kb*T))-1)",
        "variables" : ["h","omega","kb","T"],
        "output" : "n"
    },
  
    "FeynmanIIICh4Eq33": {
        "EquationRaw" : "(h/(2*pi))*omega/(exp((h/(2*pi))*omega/(kb*T))-1)",
        "variables" : ["h","omega","kb","T"],
        "output" : "E_n"
    },
  
    "FeynmanIIICh7Eq38": {
        "EquationRaw" : "2*mom*B/(h/(2*pi))",
        "variables" : ["mom","B","h"],
        "output" : "omega"
    },
  
    "FeynmanIIICh8Eq54": {
        "EquationRaw" : "sin(E_n*t/(h/(2*pi)))**2",
        "variables" : ["E_n","t","h"],
        "output" : "prob"
    },
  
    "FeynmanIIICh9Eq52": {
        "EquationRaw" : "(p_d*Ef*t/(h/(2*pi)))*sin((omega-omega_0)*t/2)**2/((omega-omega_0)*t/2)**2",
        "variables" : ["p_d","Ef","t","h","omega","omega_0"],
        "output" : "prob"
    },
  
    "FeynmanIIICh10Eq19": {
        "EquationRaw" : "mom*sqrt(Bx**2+By**2+Bz**2)",
        "variables" : ["mom","Bx","By","Bz"],
        "output" : "E_n"
    },
  
    "FeynmanIIICh12Eq43": {
        "EquationRaw" : "n*(h/(2*pi))",
        "variables" : ["n","h"],
        "output" : "L"
    },
  
    "FeynmanIIICh13Eq18": {
        "EquationRaw" : "2*E_n*d**2*k/(h/(2*pi))",
        "variables" : ["E_n","d","k","h"],
        "output" : "v"
    },
  
    "FeynmanIIICh14Eq14": {
        "EquationRaw" : "I_0*(exp(q*Volt/(kb*T))-1)",
        "variables" : ["I_0","q","Volt","kb","T"],
        "output" : "I"
    },
  
    "FeynmanIIICh15Eq12": {
        "EquationRaw" : "2*U*(1-cos(k*d))",
        "variables" : ["U","k","d"],
        "output" : "E_n"
    },
  
    "FeynmanIIICh15Eq14": {
        "EquationRaw" : "(h/(2*pi))**2/(2*E_n*d**2)",
        "variables" : ["h","E_n","d"],
        "output" : "m"
    },
  
    "FeynmanIIICh15Eq27": {
        "EquationRaw" : "2*pi*alpha/(n*d)",
        "variables" : ["alpha","n","d"],
        "output" : "k"
    },
  
    "FeynmanIIICh17Eq37": {
        "EquationRaw" : "beta*(1+alpha*cos(theta))",
        "variables" : ["beta","alpha","theta"],
        "output" : "f"
    },
  
    "FeynmanIIICh19Eq51": {
        "EquationRaw" : "-m*q**4/(2*(4*pi*epsilon)**2*(h/(2*pi))**2)*(1/n**2)",
        "variables" : ["m","q","h","n","epsilon"],
        "output" : "E_n"
    },
  
    "FeynmanIIICh21Eq20": {
        "EquationRaw" : "-rho_c_0*q*A_vec/m",
        "variables" : ["rho_c_0","q","A_vec","m"],
        "output" : "j"
    },
  
    "FeynmanBonus1": {
        "EquationRaw" : "(Z_1*Z_2*alpha*hbar*c/(4*E_n*sin(theta/2)**2))**2",
        "variables" : ["Z_1","Z_2","alpha","hbar","c","E_n","theta"],
        "output" : "A"
    },
  
    "FeynmanBonus2": {
        "EquationRaw" : "m*k_G/L**2*(1+sqrt(1+2*E_n*L**2/(m*k_G**2))*cos(theta1-theta2))",
        "variables" : ["m","k_G","L","E_n","theta1","theta2"],
        "output" : "k"
    },
  
    "FeynmanBonus3": {
        "EquationRaw" : "d*(1-alpha**2)/(1+alpha*cos(theta1-theta2))",
        "variables" : ["d","alpha","theta1","theta2"],
        "output" : "r"
    },
  
    "FeynmanBonus4": {
        "EquationRaw" : "sqrt(2/m*(E_n-U-L**2/(2*m*r**2)))",
        "variables" : ["m","E_n","U","L","r"],
        "output" : "v"
    },
  
    "FeynmanBonus5": {
        "EquationRaw" : "2*pi*d**(3/2)/sqrt(G*(m1+m2))",
        "variables" : ["d","G","m1","m2"],
        "output" : "t"
    },
  
    "FeynmanBonus6": {
        "EquationRaw" : "sqrt(1+2*epsilon**2*E_n*L**2/(m*(Z_1*Z_2*q**2)**2))",
        "variables" : ["epsilon","L","m","Z_1","Z_2","q","E_n"],
        "output" : "alpha"
    },
  
    "FeynmanBonus7": {
        "EquationRaw" : "sqrt(8*pi*G*rho/3-alpha*c**2/d**2)",
        "variables" : ["G","rho","alpha","c","d"],
        "output" : "H_G"
    },
  
    "FeynmanBonus8": {
        "EquationRaw" : "E_n/(1+E_n/(m*c**2)*(1-cos(theta)))",
        "variables" : ["E_n","m","c","theta"],
        "output" : "K"
    },
  
    "FeynmanBonus9": {
        "EquationRaw" : "-32/5*G**4/c**5*(m1*m2)**2*(m1+m2)/r**5",
        "variables" : ["G","c","m1","m2","r"],
        "output" : "Pwr"
    },
  
    "FeynmanBonus10": {
        "EquationRaw" : "arccos((cos(theta2)-v/c)/(1-v/c*cos(theta2)))",
        "variables" : ["c","v","theta2"],
        "output" : "theta1"
    },
  
    "FeynmanBonus11": {
        "EquationRaw" : "I_0*(sin(alpha/2)*sin(n*delta/2)/(alpha/2*sin(delta/2)))**2",
        "variables" : ["I_0","alpha","delta","n"],
        "output" : "I"
    },
  
    "FeynmanBonus12": {
        "EquationRaw" : "q/(4*pi*epsilon*y**2)*(4*pi*epsilon*Volt*d-q*d*y**3/(y**2-d**2)**2)",
        "variables" : ["q","y","Volt","d","epsilon"],
        "output" : "F"
    },
  
    "FeynmanBonus13": {
        "EquationRaw" : "1/(4*pi*epsilon)*q/sqrt(r**2+d**2-2*r*d*cos(alpha))",
        "variables" : ["q","r","d","alpha","epsilon"],
        "output" : "Volt"
    },
  
    "FeynmanBonus14": {
        "EquationRaw" : "Ef*cos(theta)*(-r+d**3/r**2*(alpha-1)/(alpha+2))",
        "variables" : ["Ef","theta","r","d","alpha"],
        "output" : "Volt"
    },
  
    "FeynmanBonus15": {
        "EquationRaw" : "sqrt(1-v**2/c**2)*omega/(1+v/c*cos(theta))",
        "variables" : ["c","v","omega","theta"],
        "output" : "omega_0"
    },
  
    "FeynmanBonus16": {
        "EquationRaw" : "sqrt((p-q*A_vec)**2*c**2+m**2*c**4)+q*Volt",
        "variables" : ["m","c","p","q","A_vec","Volt"],
        "output" : "E_n"
    },
  
    "FeynmanBonus17": {
        "EquationRaw" : "1/(2*m)*(p**2+m**2*omega**2*x**2*(1+alpha*x/y))",
        "variables" : ["m","omega","p","y","x","alpha"],
        "output" : "E_n"
    },
  
    "FeynmanBonus18": {
        "EquationRaw" : "3/(8*pi*G)*(c**2*k_f/r**2+H_G**2)",
        "variables" : ["G","k_f","r","H_G","c"],
        "output" : "rho_0"
    },
  
    "FeynmanBonus19": {
        "EquationRaw" : "-1/(8*pi*G)*(c**4*k_f/r**2+H_G**2*c**2*(1-2*alpha))",
        "variables" : ["G","k_f","r","H_G","alpha","c"],
        "output" : "pr"
    },
  
    "FeynmanBonus20": {
        "EquationRaw" : "1/(4*pi)*alpha**2*h**2/(m**2*c**2)*(omega_0/omega)**2*(omega_0/omega+omega/omega_0-sin(beta)**2)",
        "variables" : ["omega","omega_0","alpha","h","m","c","beta"],
        "output" : "A"
    },
  }