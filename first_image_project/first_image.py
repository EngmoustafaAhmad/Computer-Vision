
import cv2

print(cv2.__version__)

# Read image
img = cv2.imread(
    r'./apple.jpg',
    0
)

    
# Display image
cv2.imshow('First Image', img)

# Wait for keyboard input
k = cv2.waitKey(0)

if k == 27:  # ESC key
    cv2.destroyAllWindows()

elif k == ord('s'):  # Press S
    cv2.imwrite('sec_image.jpg', img)
    cv2.destroyAllWindows()
