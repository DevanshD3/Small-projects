# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import matplotlib.pyplot as plt
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
camera.capture(rawCapture, format="rgba")
image = rawCapture.array

# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
if image.shape[2] == 3:
    print("No alpha channel!")
if image.shape[2] == 4:
    red, green, blue, alpha = pic.split()
    print("the transparency of the image is:" )
    print(alpha)
# cv2.imwrite(rockpic.png, image) 
cv2.waitKey(0)