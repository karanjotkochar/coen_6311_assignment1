from ref_input import *
from emulator_output import test_coordinate
from geopy.distance import geodesic
import time


def get_distance(coordinates_one, coordinates_two):  # To calculate distance between reference and test coordinates
    ref_lat, ref_long = coordinates_one
    test_lat, test_long = coordinates_two

    if (ref_lat > 90.0 or ref_lat < -90.0) or (test_lat > 90.0 or test_long < -90.0):
        raise ValueError("Latitude out of range")
    elif (ref_long > 180.0 or ref_long < -180.0) or (test_long > 180.0 or test_long < -180.0):
        raise ValueError("Longitude out of range")
    elif len(coordinates_one) > 2 or len(coordinates_two) > 2:
        raise ValueError("Coordinates not in correct format")
    else:
        length = geodesic(coordinates_one, coordinates_two).m
        return length


def check_limit(dis, lim):  # To compare distance between coordinates with gps accuracy limit
    if type(dis) not in [int, float] and type(lim) not in [int, float]:
        raise TypeError("Values not in correct datatype")
    else:
        if dis < lim:
            print(f"Distance = {dis} No theft")
            return 1
        else:
            print(f"Distance = {dis} Theft alert")
            return 0


theft_status = False

while not theft_status:
    distance = get_distance(reference_coordinate(), test_coordinate())
    accuracy_limit = gps_accuracy_limit()

    if check_limit(distance, accuracy_limit) == 1:
        timer = set_timer()
        time.sleep(timer)
    else:
        theft_status = True


