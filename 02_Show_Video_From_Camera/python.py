
import cv2

# Open webcam
cap = cv2.VideoCapture(0)

# Define video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

print(cap.isOpened())

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Get frame dimensions
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Save original frame
        out.write(frame)

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display grayscale video
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
