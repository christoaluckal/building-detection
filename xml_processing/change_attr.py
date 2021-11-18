from lxml import etree as et
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

def append_element(xml_name,location,values):
    parser = et.XMLParser(remove_blank_text=True)
    tree = et.parse(xml_name, parser)

    last_loc = tree.xpath(xpath_dict[location])[-1]

    object = et.Element("object")

    name = et.SubElement(object,"name")
    name.text = values[0]

    pose = et.SubElement(object,"pose")
    pose.text = values[1]

    truncated = et.SubElement(object,"truncated")
    truncated.text = values[2]

    difficulty = et.SubElement(object,"difficulty")
    difficulty.text = values[3]

    bndbox = et.SubElement(object,"bndbox")

    xmin = et.SubElement(bndbox,"xmin")
    xmin.text = values[4]

    ymin = et.SubElement(bndbox,"ymin")
    ymin.text = values[5]

    xmax = et.SubElement(bndbox,"xmax")
    xmax.text = values[6]

    ymax = et.SubElement(bndbox,"ymax")
    ymax.text = values[7]

    last_loc.addnext(object)
    tree.write(xml_name,pretty_print=True)
    pass

def read_element_value(tree,item):
    for x in tree.xpath(xpath_dict[item]):
        print(x.text)

def change_attribute(xml_name,vals): 
    append_element(xml_name,'object',vals)
# print(pretty_xml)