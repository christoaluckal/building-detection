import image_sel as isel
import change_attr as ca
import os
import sys

args = sys.argv[1:]

folder = args[0]

done = open('donelist.txt','r')
done_list = done.readlines()
done.close()
done = open('donelist.txt','a')


def make_new(tag,location):
    img_list = sorted([x for x in os.listdir(location) if x.endswith('.jpg')])
    xml_list = sorted([x for x in os.listdir(location) if x.endswith('.xml')])
    for x,y in zip(img_list,xml_list):
        if x+'\n' not in done_list:
            print(location+x)
            rectangle_list = isel.image_sel_method(location+x)
            if len(rectangle_list)!=0:
                for rect_old in rectangle_list:
                    for rect in rect_old:
                        xmin,ymin,xmax,ymax = rect[0][0],rect[0][1],rect[1][0],rect[1][1]
                        vals = [tag,'Unspecified','0','0',str(xmin),str(ymin),str(xmax),str(ymax)]
                        ca.append_element(location+y,'object',vals)
            del rectangle_list[:]
            done.write(x+'\n')
        # isel.poly_list.clear()

make_new('not building',folder)
