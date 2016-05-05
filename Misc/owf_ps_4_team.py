import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import newton, fsolve
from math import sqrt

#############
#   part c  #
#############

# given parameters / waveguide structure
n1 = 3.48   # core
n2 = 1.44   # substrate
n3 = 1      # cladding
a = 250 * (10 ** -9)    # core thrickness in nm
modeNumber = [0,1,2]    # mode numbers
lamb = np.linspace(1.12 * (10**-6), 3.7 * (10**-6), 201)
B = np.linspace(0, 0.9, 201)

# Calculations
pi = 3.14
k0 = 2*pi/lamb
normalizedFreq = a*k0*sqrt((n1**2) - (n2**2))   # normalized frequency
gamma = ((n2**2)-(n3**2))/((n1**2)-(n2**2))     # assymetric parameter

B_all_modes_solution = []
B_one_mode_solution = []

# Equation
for j in range(len(modeNumber)):
    m = modeNumber[j]
    print m
    for i in range(len(lamb)):
        V = normalizedFreq[i]
        func = lambda B : (V*np.sqrt(1-B)) - (0.5*np.arctan(np.sqrt((gamma+B)/(1-B)))) - (0.5*np.arctan(np.sqrt((B)/(1-B)))) - (0.5*m*pi)
        B_initial_guess = 0.9
        if V < m+1:
            tempSolution = 0
        else:
            tempSolution = fsolve(func, B_initial_guess)
        B_one_mode_solution.append(tempSolution)
    V = normalizedFreq[0]
    B_all_modes_solution.append(B_one_mode_solution)
    # plt.plot(B, func(B))
    # plt.xlabel("B")
    # plt.ylabel("exp value")
    # plt.grid()
    # plt.show()
    B_one_mode_solution = [] # clear the list of one mode
    
# problem : V gets bigger every loopstep, need to cut off the lower part. - solution! cut off wavelengths / frequency
                       
# Plot it
plt.plot(normalizedFreq, B_all_modes_solution[0], normalizedFreq, B_all_modes_solution[1], normalizedFreq, B_all_modes_solution[2])
plt.xlabel("V")
plt.ylabel("B")
plt.grid()
plt.show()



