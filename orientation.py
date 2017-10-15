#This function adjusts PMP determined by the intensity_duration function for orientation

import matplotlib.pyplot as plt
from math import log
from matplotlib import pylab
import numpy as np
import math
from scipy.optimize import curve_fit

#orientation formula
def orientation(orientation,preferred_orientation,storm_area,PMP_intensity_duration):
    diff = abs(orientation - preferred_orientation)
    #calculation of C1
    if diff <= 40:
        c1 = 0
    elif diff > 40 and diff <= 65:
        c1 = (diff - 40)/25
    else:
        c1 = 1
    #calculation of C2
    if storm_area <= 300:
        c2 = 0
    if storm_area > 300 and storm_area < 3000:
        c2 = (storm_area - 300)/2700
    else:
        c2 = 1
    adj = 1 - (0.15*c1*c2)
    PMP_intensity_duration_edited = []
    for i in range(0,len(PMP_intensity_duration)):
        PMP_intensity_duration_edited.append(PMP_intensity_duration[i]*adj)
    return PMP_intensity_duration_edited
