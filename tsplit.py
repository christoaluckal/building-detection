import os
import shutil
from sklearn.model_selection import train_test_split
import numpy as np
img_dir = np.array(sorted(['dataset/'+x for x in os.listdir('dataset') if x.endswith('jpg')]))
txt_dir = np.array(sorted(['dataset/'+x for x in os.listdir('dataset') if x.endswith('txt')]))

img_train,img_val,txt_train,txt_val = train_test_split(img_dir,txt_dir,test_size=0.2,random_state=0)

img_val,img_test,txt_val,txt_test = train_test_split(img_val,txt_val,test_size=0.5,random_state=0)

for x,y in zip(img_train,txt_train):
    shutil.copy(x,'dataset/train')
    shutil.copy(y,'dataset/train')

for x,y in zip(img_val,txt_val):
    shutil.copy(x,'dataset/validate')
    shutil.copy(y,'dataset/validate')

for x,y in zip(img_test,txt_test):
    shutil.copy(x,'dataset/test')
    shutil.copy(y,'dataset/test')