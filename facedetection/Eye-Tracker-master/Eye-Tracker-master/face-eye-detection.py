# -*- coding: utf-8 -*-'
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
cam = cv2.VideoCapture(0)

while True:
    prv,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    detect_faces = face_cascade.detectMultiScale(gray)
    for(fx,fy,fw,fh) in detect_faces:
        print(fx,fy,fw,fh)
        cv2.imshow('faces',img)
    wk=cv2.waitKey(30) & 0xff
    if wk==27:
        break
cam.release()
cv2.destroyAllWindows()
