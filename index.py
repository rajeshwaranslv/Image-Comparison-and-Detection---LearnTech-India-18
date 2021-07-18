import cv2 as cv
import numpy as np
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

coc_img= cv.imread('coc.PNG',cv.IMREAD_UNCHANGED)
coc_cannon_img= cv.imread('coc cannon.PNG',cv.IMREAD_UNCHANGED)

found= cv.matchTemplate(coc_img, coc_cannon_img,cv.TM_CCOEFF_NORMED)
print(found)

threshold=0.60
locations = np.where(found>=threshold)
locations = list(zip(*locations[::-1]))
print(locations)

if locations:
    print('Found match')
    needle_w = coc_cannon_img.shape[1]
    needle_h = coc_cannon_img.shape[0]

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0]+needle_w,top_left[1]+needle_h)
        cv.rectangle(coc_img, top_left, bottom_right, color=(0,0,255),thickness=2,lineType=cv.LINE_4)
    
    cv.imshow('match', coc_img)
    cv.waitKey()

else:
    print('Not Found')