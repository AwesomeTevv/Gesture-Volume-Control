import cv2
import time
import numpy as np
import HandTrackingModule as htm

cam_width = 1280
cam_height = 720

cap = cv2.VideoCapture(0)

cap.set(3, cam_width)
cap.set(4, cam_height)

current_time = 0
previous_time = 0

detector = htm.handDetector(detectionConfidence = 0.7)

while True:
    success, img = cap.read()
    
    img = detector.findHands(img)
    
    landmark_list = detector.findPosition(img, draw = False)
    if len(landmark_list) != 0:
        x1, y1 = landmark_list[4][1], landmark_list[4][2]
        x2, y2 = landmark_list[8][1], landmark_list[8][2]
        
        cv2.circle(img, (x1, y1), 10, (255, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 255, 0), cv2.FILLED)
        
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 3)
    
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    
    cv2.putText(img, f'fps: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)