#This file performs a linear interpolation between 2 values.

def linear_interpolation(x,x1,y1,x2,y2):
    y = y1 + (((y2-y1)*(x-x1))/(x2-x1))
    return y