# Camera Resolution and Grayscale Video Capture using OpenCV

## Overview
This project demonstrates how to access a webcam using **OpenCV**, retrieve and modify camera resolution, capture video frames, and convert the live video stream into grayscale.

## Features
- Access the webcam using `cv2.VideoCapture()`.
- Retrieve the camera's current frame height and width.
- Set custom camera resolution.
- Capture video frames in real time.
- Convert frames from BGR to Grayscale.
- Display the live grayscale video.
- Press `q` to exit the video window.

## Requirements
- Python 3.x
- OpenCV

Install OpenCV:

```bash
pip install opencv-python
```

## How It Works

### 1. Initialize the Camera
```python
cap = cv2.VideoCapture(0)
```
Opens the default webcam (camera index `0`).

### 2. Get Camera Resolution
```python
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
```
Retrieves the current frame height and width.

### 3. Set Camera Resolution
```python
cap.set(3, 3000)
cap.set(4, 3000)
```
Attempts to set the camera resolution to:
- Width: 3000 pixels
- Height: 3000 pixels

**Note:** The actual resolution depends on the webcam's supported resolutions and drivers. The camera may not accept the requested values.

### 4. Capture and Convert Frames
```python
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
Reads each frame and converts it from BGR color format to grayscale.

### 5. Display the Video
```python
cv2.imshow('frame', gray)
```
Displays the live grayscale video.

### 6. Exit and Release Resources
Press `q` to stop the video capture.

```python
cap.release()
cv2.destroyAllWindows()
```

## Run the Project

```bash
python main.py
```

## Technologies Used
- Python
- OpenCV (Computer Vision)
- NumPy

## Learning Objectives
- Understanding webcam access with OpenCV.
- Working with camera properties.
- Controlling video capture resolution.
- Understanding video frames.
- Applying color space conversion (BGR to Grayscale).
- Displaying real-time video using OpenCV.

---
**Author:** Moustafa Ahmed  
**Field:** Computer Vision & Machine Learning