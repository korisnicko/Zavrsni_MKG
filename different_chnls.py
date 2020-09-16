import cv2 as cv
import sys
import numpy as np 
import itertools
chnls = {'0':"B", "1":"G","2":"R"}
ims = {}

img = cv.imread(".\images\marvel.jpg")
if img is None:
    sys.exit()

h, w, c = img.shape 
cnt = 0
for cmb in list(itertools.combinations([x for x in range(c)], 2)):
    s = "BGR"
    cpy = np.copy(img)
    for c in cmb:
        cpy[:,:,c] = np.zeros([img.shape[0], img.shape[1]])
        s = s.replace(chnls[str(c)],'')
    ims[s] = cpy    
    cpy = np.copy(img)
    cpy[:,:,cnt] = np.zeros([img.shape[0], img.shape[1]])
    ims["BGR".replace(chnls[str(cnt)],'')] = cpy
    cnt = cnt + 1

for key, value in ims.items():
    cv.imshow(key,value)
    cv.waitKey(0)