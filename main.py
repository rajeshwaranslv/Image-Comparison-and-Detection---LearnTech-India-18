#import lib
import cv2 as cv
import numpy as np

coc_img= cv.imread('coc.PNG',cv.IMREAD_UNCHANGED)
coc_cannon_img= cv.imread('coc cannon.PNG',cv.IMREAD_UNCHANGED)

found= cv.matchTemplate(coc_img, coc_cannon_img,cv.TM_CCOEFF_NORMED)#match template function used to match 2 pic

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(found)#for perfect match we use minmax function

print('best top left match:%s' %str(max_loc))
print('best match confidence: %s' % max_val)

threshold=0.8#threshold to take perfect match
if max_val >= threshold:
    print('found')

    cannon_w = coc_cannon_img.shape[1] #with for bottom right
    cannon_h = coc_cannon_img.shape[0] #height for bottom right

    top_left=max_loc
    bottom_right= (top_left[0]+ cannon_w,top_left[1]+cannon_h)

    #this line to make box search part of whole img
    cv.rectangle(coc_img,top_left,bottom_right,color=(255,0,0),thickness=2,lineType=cv.LINE_4)

    #imshow function used to display the result image
    cv.imshow('RESULT',coc_img)
    #waitkey is used to hold the pic ,until we press some key
    cv.waitKey()

else:
    print('NOT FOUND')
