import os
import shutil
curr_dir = os.getcwd()+"/"
print(curr_dir)
annot_dir = sorted(os.listdir('annotations'))
img_dir = sorted(os.listdir('broke'))
new_annot = []
new_img = []

for x in range(len(img_dir)):
    xml_name = img_dir[x][:-3]+'xml'
    if (xml_name in annot_dir):
        new_annot.append(curr_dir+'annotations/'+xml_name)
        new_img.append(curr_dir+'broke/'+img_dir[x])


for x,y in zip(new_annot,new_img):
    shutil.copy(x,curr_dir+'dataset')
    shutil.copy(y,curr_dir+'dataset')