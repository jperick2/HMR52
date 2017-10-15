#This functions determines an unadjusted PMP for each storm duration (6hrs, 12hrs, 24hrs, 48hrs, 72hrs)
# area -> refers to the area of the storm
# coeff_6hrs -> coefficients determined from depth, area linear regression (exponential - best_fit function) for 6hr storm
# coeff_12hrs -> coefficients determined from depth, area linear regression (exponential - best_fit function) for 12hr storm
# coeff_24hrs -> coefficients determined from depth, area linear regression (exponential - best_fit function) for 24r storm
# coeff_48hrs -> coefficients determined from depth, area linear regression (exponential - best_fit function) for 48hr storm
# coeff_72hrs -> coefficients determined from depth, area linear regression (exponential - best_fit function) for 72hr storm

import matplotlib.pyplot as plt
from math import log
from matplotlib import pylab
import numpy as np
import math
from scipy.optimize import curve_fit

def intensity_duration(area,coeff_6hrs,coeff_12hrs,coeff_24hrs,coeff_48hrs,coeff_72hrs):
    PMP = {}
    PMP[6] = math.log(area/coeff_6hrs[0])/coeff_6hrs[1]
    PMP[12] = math.log(area/coeff_12hrs[0])/coeff_12hrs[1]
    PMP[24] = math.log(area / coeff_24hrs[0]) / coeff_24hrs[1]
    PMP[48] = math.log(area / coeff_48hrs[0]) / coeff_48hrs[1]
    PMP[72] = math.log(area / coeff_72hrs[0]) / coeff_72hrs[1]
    x = []
    y = []
    for key,val in PMP.items():
        x.append(key)
        y.append(val)
    x_log = [log(i) for i in x]
    coeffs = np.polyfit(x_log, y, 1)  # generates coefficients for linear regression of x_log and y
    results = {}
    results['ln_fit'] = coeffs.tolist()  # retrieves (in the form of a list) coefficients for linear regression results
    a = results['ln_fit'][0] # coefficient in y(x) = a*ln(x) + b
    b = results['ln_fit'][1]  # coefficient in y(x) = a*ln(x) + b
    x_fit = np.array(range(6,78,6))
    def f(z):
        return (a*math.log(z))+b
    PMP_increment_cumulative = [f(j) for j in x_fit]
    PMP_increment = []
    for k in range(0,len(PMP_increment_cumulative)):
        if k == 0:
            PMP_increment.append(PMP_increment_cumulative[k])
        else:
            PMP_increment.append(PMP_increment_cumulative[k]-PMP_increment_cumulative[k-1])
    return PMP_increment
