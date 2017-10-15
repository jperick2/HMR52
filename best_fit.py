#This performs a linear regression to determine the relationship between PMP depth and storm area.
# The output of this function is coefficients that are used to determine a PMP depth that is not adjusted.
# x = PMP determined from Figures 18-47 in the HMR-52 Manual
# duration = storm duration in hours. This will be either 6, 12, 24, 48, or 72.
# plot_show -> enter "Y" to plot results of the linear regression

import matplotlib.pyplot as plt
from math import log
from matplotlib import pylab
import numpy as np
import math
from scipy.optimize import curve_fit

def best_fit(x, duration, plot_show):
    Area_sq_mi = [10, 200, 1000, 5000, 10000, 20000] #storm area ins square miles
    y = Area_sq_mi
    y_log = [log(i) for i in y]  # semilogy plot - taking natural log of each element in y
    coeffs = np.polyfit(x, y_log, 1)  # generates coefficients for linear regression of x and y_log
    results = {}
    results['exp'] = coeffs.tolist()  # retrieves coefficients for linear regression results
    a = math.exp(results['exp'][1])  # coefficient in y(x) = a*exp(b*x)
    b = results['exp'][0]  # coefficient in y(x) = a*exp(b*x)
    coeff_final = [a, b]

    ##Calculating R-Squared
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y_log) / len(y_log)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y_log - ybar) ** 2)
    results['r_squared'] = ssreg / sstot

    # Plotting on a graph
    x = np.array(x, dtype=float)
    minx = int(math.floor(np.min(x)))
    maxx = int(math.ceil(np.max(x)))
    x_curve = np.array(range(minx, maxx))
    y_curve = eval(str(a) + '* np.exp(' + str(b) + '* x_curve)')
    plt.figure()
    plt.plot(x, y, 'ko', label="Data Points")  # plots raw data
    plt.plot(x_curve, y_curve, '-r', label="Curve")  # plots best fit curve
    plt.xlabel('PMP, (in)')
    plt.ylabel('Area (sq mi)')
    plt.title("Depth-Area Curve for " + str(duration) + "hrs")
    plt.text(0.5 * maxx, (np.max(y_curve) - 6000), '$R^2 = %0.2f$' % results['r_squared'], fontsize=16)
    plt.text(0.5 * maxx, 0.9 * (np.max(y_curve) - 6000), '$y(x) = %0.0fe^{%0.3fx}$' % (a, b), fontsize=16)
    plt.legend()
    if plot_show == "Y":
        plt.show()
    return coeff_final
