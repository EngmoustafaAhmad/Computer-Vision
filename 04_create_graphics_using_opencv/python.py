import numpy as np
import cv2 as cv

img = np.zeros((600,900,3) , dtype= np.uint8 )
cv.rectangle(img, (0,0) , (900,500) , (255,255,85) , -1)
cv.rectangle(img, (0,500) , (900,600) , (75,180,70) , -1)

cv.circle(img,(200,150),60,(0,255,255),-1)
cv.circle(img,(200,150),75,(220,255,255),10)

cv.line(img, (710,500) , (710,420) , (30,65,155) ,15)

triangle = np.array([[640,460],[780,460],[710,200]], dtype=np.int32)
cv.fillPoly(img , [triangle] , (75,180,70))

cv.imwrite("tree.png", img)
cv.imshow("tree",img)

cv.waitKey(0)
cv.destroyAllWindows()