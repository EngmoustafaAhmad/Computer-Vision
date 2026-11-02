# OpenCV Drawing Shapes and Text

## Overview
This project demonstrates how to use OpenCV and NumPy to create an image and draw basic geometric shapes and text on it using Python.

It covers essential OpenCV drawing functions, including lines, arrows, rectangles, circles, and text.

## Technologies Used
- Python
- OpenCV (`cv2`)
- NumPy

## Features
- Create a blank 512×512 black image.
- Draw a green diagonal line.
- Draw a blue arrowed line.
- Draw a red rectangle.
- Draw a green circle.
- Add yellow text (`OpenCV`) to the image.

## OpenCV Functions
| Function | Description |
|---|---|
| `np.zeros()` | Creates a black image. |
| `cv2.line()` | Draws a straight line. |
| `cv2.arrowedLine()` | Draws an arrowed line. |
| `cv2.rectangle()` | Draws a rectangle. |
| `cv2.circle()` | Draws a circle. |
| `cv2.putText()` | Adds text to an image. |
| `cv2.imshow()` | Displays the image. |
| `cv2.waitKey()` | Waits for a keyboard event. |
| `cv2.destroyAllWindows()` | Closes all OpenCV windows. |

## Installation

Install the required libraries:

```bash
pip install opencv-python numpy
```

## How to Run

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd YOUR_PROJECT_DIRECTORY
```

3. Run the Python script:

```bash
python main.py
```

## Output

The program displays a 512×512 image containing different geometric shapes and the text "OpenCV".

## Learning Objectives
- Understand image creation using NumPy.
- Learn OpenCV coordinate systems.
- Practice drawing geometric shapes.
- Understand BGR color representation in OpenCV.
- Learn how to add text to images.

## Author
**Moustafa Ahmed**

Machine Learning Engineer | Computer Vision | AI