import cv2
import numpy as np
cap=cv2.VideoCapture(r"D:\Naresh it\My work\opencv projects\Object tracking from video\highway.mp4")

_,frame= cap.read()
cv2.imshow("Frame", frame)
cv2.waitKey(0)