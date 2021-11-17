from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np
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

points = []

def get_mbr(points):
    x_coordinates, y_coordinates = zip(*points)
    return [(min(x_coordinates), min(y_coordinates)), (max(x_coordinates), max(y_coordinates))]

def check_inside(x1,y1,x2,y2,polygon):
    if inside_poly(x1,x2,y1,y2,polygon) is True:
        points.append([(x1,y1),(x2,y2)])
        return
    else:
        width = abs(x2-x1)
        height = abs(y2-y1)
        if width > 0.05 and height > 0.05:
            mid_x,mid_y = (x1+x2)/2,(y1+y2)/2
            check_inside(x1,y1,mid_x,mid_y,polygon)
            check_inside(mid_x,y1,x2,mid_y,polygon)
            check_inside(x1,mid_y,mid_x,y2,polygon)
            check_inside(mid_x,mid_y,x2,y2,polygon)
        else:
            return

image = np.ones((800, 800)) * 0

# test_polygon = [(0,0),(1,0),(1,1)]
test_polygon = [(0.2,0.1),(0.6,0.2),(0.8,0.5),(0.5,0.7),(0.1,0.5)]
# polygon_draw = np.array(normalize(test_polygon,800),dtype=np.int32)
polygon_draw = np.array([(160,  80),(480, 160),(640, 400),(400, 560),(80, 400)])
cv2.polylines(image,[polygon_draw],1,(255,255,0),1)

mbr = get_mbr(test_polygon)
check_inside(0,1,1,0,test_polygon)

norm_points = np.int_(normalize(points,800))

for x in norm_points:
    cv2.rectangle(image,(x[0][0],x[0][1]),(x[1][0],x[1][1]),255,2)


cv2.imshow('test',image)
cv2.waitKey(0)