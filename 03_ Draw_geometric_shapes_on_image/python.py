import numpy as np
import cv2

img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img , (0,0) , (256,256) , (0,255,0) , 10)
img = cv2.arrowedLine(img , (512,0) ,(256,256) , (255,0,0),5)
img = cv2.rectangle(img , (384,0) , (510,128) , (0,0,255) , 10)
img = cv2.circle(img , (447,63) , 63 , (0, 255 , 0), 5 )
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCv', (10,210) , font , 4 , (0 , 255 , 255) , 10)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()