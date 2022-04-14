import face_recognition as fc
from cv2 import cv2
import os, time, pickle, json, sys, numpy
from PIL import Image, ImageDraw



def detect_person_in_video():
    data = pickle.loads(open("teacher_faces.pickle", "rb").read())
    video = cv2.VideoCapture(0)

    while True:
        reg,frame = video.read()
        locations = fc.face_locations(frame)
        try:
            left_top = (locations[0][3], locations[0][0])
            right_bottom = (locations[0][1], locations[0][2])
            cv2.rectangle(frame, left_top, right_bottom,[255,255,0])
        except:
            pass
        cv2.imshow('hello',frame)
        cv2.waitKey(1)
        
    
    
if __name__ == "__main__":
    detect_person_in_video()