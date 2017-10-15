from linear_interpolation import *

#function that interpolates to get the percent for 6-hour increment
def isohyet_values(storm_area, increment):
    isohyet_percent = []
    for i in range(0, 19):
        isohyet_increment_list = [10,17,25,35,50,75,100,140,175,220,300,360,450,560,700,850,1000,1200,1500,1800,2150,
                                  2600,3000,3800,4500,5500,6500,8000,10000,12000,15000,18000,20000]
        isohyet_list_for_min_storm_area = [i for i in isohyet_increment_list if i < storm_area]
        isohyet_list_for_max_storm_area = [i for i in isohyet_increment_list if i > storm_area]
        min_storm_area = max(isohyet_list_for_min_storm_area)
        max_storm_area = min(isohyet_list_for_max_storm_area)
        interpolate = linear_interpolation(storm_area, min_storm_area, increment[i][min_storm_area], max_storm_area,
                                           increment[i][max_storm_area])
        isohyet_percent.append(interpolate)
    print(isohyet_percent)