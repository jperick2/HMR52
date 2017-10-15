#geometric_properties
#function to check whether the points are clockwise or counter-clockwise
import numpy as np
import math

def geometric_properties(x_coordinates, y_coordinates):
    # checking whether the points are clockwise or counter-clockwise
    edge = []
    for point in range(0, len(x_coordinates) - 1):
        edge_calc = (x_coordinates[point + 1] - x_coordinates[point]) * (
        y_coordinates[point + 1] + y_coordinates[point])
        edge.append(edge_calc)
    sum_edge = np.sum(edge)  # negative indicates counter-clockwise and positive indicates clockwise
    print(sum_edge)
    if sum_edge <= 0:
        print("Points go counter-clockwise")
    else:
        print("Points go clockwise and should be reversed")
        x_coordinates_reverse = x_coordinates[::-1]
        y_coordinates_reverse = y_coordinates[::-1]
        print(x_coordinates_reverse)
        print(y_coordinates_reverse)