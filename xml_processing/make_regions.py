import image_sel as isel
import change_attr as ca
import os

def make_new(tag,location):
    img_list = sorted([x for x in os.listdir(location) if x.endswith('.jpg')])
    xml_list = sorted([x for x in os.listdir(location) if x.endswith('.xml')])
    for x,y in zip(img_list,xml_list):
        rectangle_list = isel.image_sel_method(x)
        if len(rectangle_list)!=0:
            for rect_old in rectangle_list:
                for rect in rect_old:
                    xmin,ymin,xmax,ymax = rect[0][0],rect[0][1],rect[1][0],rect[1][1]
                    vals = [tag,'Unspecified','0','0',str(xmin),str(ymin),str(xmax),str(ymax)]
                    ca.append_element(y,'object',vals)
        del rectangle_list[:]
        # isel.poly_list.clear()

make_new('not building','.')
