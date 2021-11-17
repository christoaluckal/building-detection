import numpy as np
# import xml.etree.cElementTree as ET
from lxml.etree import tostring
import lxml.etree as ET



# Get the main image metadata
def getAnnotatedData(tree,tag):
    xpath_dict = {}
    xpath_dict["annotation"] = '/annotation'
    xpath_dict["folder"] = '/annotation/folder'
    xpath_dict["filename"] = '/annotation/filename'
    xpath_dict["path"] = '/annotation/path'
    xpath_dict["source"] = '/annotation/source'
    xpath_dict["size"] = '/annotation/size'
    xpath_dict["width"] = '/annotation/size/width'
    xpath_dict["height"] = '/annotation/size/height'
    xpath_dict["depth"] = '/annotation/size/depth'
    xpath_dict["segmentation"] = '/annotation/segmentation'
    xpath_dict["object"] = '/annotation/object'
    xpath_dict["name"] = '/annotation/object/name'
    xpath_dict["pose"] = '/annotation/object/pose'
    xpath_dict["truncated"] = '/annotation/object/truncated'
    xpath_dict["difficulty"] = '/annotation/object/difficulty'
    xpath_dict["bndbox"] = '/annotation/object/bndbox'
    xpath_dict["xmin"] = '/annotation/object/bndbox/xmin'
    xpath_dict["ymin"] = '/annotation/object/bndbox/ymin'
    xpath_dict["xmax"] = '/annotation/object/bndbox/xmax'
    xpath_dict["ymax"] = '/annotation/object/bndbox/ymax'
    op = {}
    # tree = ET.parse(xml_path)
    for x in tag:
        statlist = tree.xpath(xpath_dict[x])
        op[x] = statlist[0].text
    return op

def YoloFormat(file_xml,input_dir,output_dir):
    tags_to_search = ['folder','filename','path','width','height']
    # createAnnoatationXML()
    print(input_dir+file_xml)
    tree = ET.parse(input_dir+'/'+file_xml)


    base_data = getAnnotatedData(tree,tags_to_search)
    width = int(base_data["width"])
    height = int(base_data["height"])
    root = tree.getroot()
    xmins = root.findall('object/bndbox/xmin')
    xmaxs = root.findall('object/bndbox/xmax')
    ymins = root.findall('object/bndbox/ymin')
    ymaxs = root.findall('object/bndbox/ymax')
    for a,b,c,d in zip(ymins,xmins,ymaxs,xmaxs):
        y_min,x_min,y_max,x_max = int(a.text),int(b.text),int(c.text),int(d.text)
        cent_x = (x_min+x_max)/(2*width)
        cent_y = (y_min+y_max)/(2*height)
        yolo_height = (y_max-y_min)/height
        yolo_width = (x_max-x_min)/width
        with open('./dataset/'+file_xml[:-3]+"txt",'a') as writer:
            writer.write("0 "+str(cent_x)+" "+str(cent_y)+" "+str(yolo_width)+" "+str(yolo_height)+"\n")

import sys
import os
args = sys.argv[1:]
input_dir = args[0]
output_dir = args[1]
input_files = os.listdir(input_dir)
input_xmls = []
input_jpgs = []
for x in input_files:
    if x.endswith(".xml"):
        input_xmls.append(x)

for x in input_xmls:
    YoloFormat(x,input_dir,output_dir)

