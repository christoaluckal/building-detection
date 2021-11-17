import xml.etree.ElementTree as ET
import os
xml_list = [x for x in os.listdir('../dataset') if x.endswith('xml')]
print(xml_list)
for xml_file in xml_list:
    xmlTree = ET.parse('../dataset/'+xml_file)
    rootElement = xmlTree.getroot()
    #Iterate Through All Books
    for element in rootElement.findall("folder"):
        #Check if title contains the word Python
        # path_name = element.text
        # path_name = path_name.split('/')
        # path_name = '/'+path_name[1]+'/'+path_name[2]+'/'+path_name[3]+'/'+path_name[4]+'/'+'dataset/'+path_name[6]
        # element.text = path_name
        element.text = 'dataset'
    xmlTree.write('../dataset/'+xml_file)
