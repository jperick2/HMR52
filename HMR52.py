import matplotlib.pyplot as plt
from math import log
from matplotlib import pylab
import numpy as np
import math
from scipy.optimize import curve_fit
from best_fit import *
from linear_interpolation import *
from isohyet_areas import *
from isohyet_increment import *
from intensity_duration import *
from orientation import *
from geometric_properties import *
from isohyet_values import *

#numbers from figures
Duration_6hr_PMP = [29.8, 22.3, 16.2, 9.3, 7.2, 5.2]
Duration_12hr_PMP = [36.2, 27.4, 21.2, 13.1, 10.4, 8.2]
Duration_24hr_PMP = [41.8, 33, 26.8, 18.1, 14.9, 11.7]
Duration_48hr_PMP = [46.7, 37.5, 31, 22.6, 18.8, 15.4]
Duration_72hr_PMP = [49.8, 41.4, 34.5, 25.9, 21.0, 18.4]

#Determining coefficients to use in intensity_duration function
coeff_6hr = best_fit(Duration_6hr_PMP, 6,"Y")
coeff_12hr = best_fit(Duration_12hr_PMP, 12,"Y")
coeff_24hr = best_fit(Duration_24hr_PMP, 24,"Y")
coeff_48hr = best_fit(Duration_48hr_PMP, 48,"Y")
coeff_72hr = best_fit(Duration_72hr_PMP, 72,"Y")

#Determining PMP
PMP_intensity_duration = intensity_duration(3000, coeff_6hr, coeff_12hr, coeff_24hr, coeff_48hr, coeff_72hr)
print(PMP_intensity_duration)

#Adjusting PMP based orientation
adj_orientation = orientation(208, 314, 3000, PMP_intensity_duration)
print(adj_orientation)


isohyet_values(42, largest_increment)
isohyet_values(42, second_largest_increment)
isohyet_values(42, third_largest_increment)
isohyet_values(42, fourth_largest_increment)

# counter-clockwise
x_coor = [5, 6, 4, 1, 1]
y_coor = [0, 4, 5, 5, 0]

# clockwise
x = [1, 1, 4, 6, 5]
y = [0, 5, 5, 4, 0]

#geometric_properties(x, y)


