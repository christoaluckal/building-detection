from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
import math
import matplotlib.pyplot as plt
import cv2

def normalize(data,norm):
    np_data = np.int_(np.array(data)*norm)
    return np_data

def inside_poly(x1,x2,y1,y2,poly):
    # x1,y1,x2,y2 = mbr[0][0],mbr[0][1],mbr[1][0],mbr[1][1]
    buffer = 1e-10
    tl = Point(x1+buffer,y1-buffer)
    tr = Point(x2-buffer,y1-buffer)
    bl = Point(x1+buffer,y2+buffer)
    br = Point(x2-buffer,y2+buffer)
    polygon = Polygon(poly)
    return (polygon.contains(tl) and polygon.contains(tr) and polygon.contains(bl) and polygon.contains(br))

# points = []

def get_mbr(points):
    x_coordinates, y_coordinates = zip(*points)
    return min(x_coordinates), min(y_coordinates), max(x_coordinates), max(y_coordinates)

def check_inside(x1,y1,x2,y2,polygon,points):
    if inside_poly(x1,x2,y1,y2,polygon) is True:
        points.append([(math.floor(x1),math.floor(y1)),(math.floor(x2),math.floor(y2))])
        return
    else:
        width = abs(x2-x1)
        height = abs(y2-y1)
        if width > 100 and height > 100:
            mid_x,mid_y = (x1+x2)/2,(y1+y2)/2
            check_inside(x1,y1,mid_x,mid_y,polygon,points)
            check_inside(mid_x,y1,x2,mid_y,polygon,points)
            check_inside(x1,mid_y,mid_x,y2,polygon,points)
            check_inside(mid_x,mid_y,x2,y2,polygon,points)
        else:
            return


def make_trees(polygon):
    x1,y1,x2,y2 = get_mbr(polygon)
    points = []
    check_inside(x1,y1,x2,y2,polygon,points)
    return points


