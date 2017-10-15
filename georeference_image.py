import numpy as np
from scipy.interpolate import griddata
import linecache

#function that returns the index of value in array closest to given value
def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx

#funcation that returns the PMP value based on the georeferenced image
def find_PMP_value(filename,coord_x,coord_y):
    grid_values = np.array(np.loadtxt(filename, skiprows=6))
    num_col = int(linecache.getline(filename, 1)[6:])
    num_row = int(linecache.getline(filename, 2)[6:])
    xLL = float(linecache.getline(filename, 3)[10:])
    yLL = float(linecache.getline(filename, 4)[10:])
    cell_size = float(linecache.getline(filename, 5)[9:])
    neg_cell_size = cell_size * -1
    xR = xLL + (cell_size * num_col)
    yR = yLL + (cell_size * num_row)
    grid_x, grid_y = np.mgrid[yR:yLL:neg_cell_size, xLL:xR:cell_size]
    #convert grid_x into a column to get unique values
    grid_x_to_column = grid_x[:,0]
    #find value closest to user defined x-coordinate
    grid_x_to_column_index = find_nearest(grid_x_to_column,coord_x)
    #convert grid_y into a row to get unique values
    grid_y_to_row = grid_y[0,:]
    #find value closest to user defined y-coordinate
    grid_y_to_row_index = find_nearest(grid_y_to_row,coord_y)
    #use above info to find PMP in the PMP values grid derived from .asc
    value = grid_values[grid_y_to_row_index,grid_x_to_column_index]
    return(value)

print(find_PMP_value("C:/Users/jperi/Downloads/HMR_51_Grids/PMP_6hr_10sqmi.asc",31.75,-98.25))

#41,-102 --> 25.1020278931