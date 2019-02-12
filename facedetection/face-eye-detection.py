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
        print('face detected ' ,fx,fy,fw,fh)
        cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(0,0,255),2)
        face_gray=gray[fy:fy+fh,fx:fx+fw]
        face_color=img[fy:fy+fh,fx:fx+fw]
        
        detect_eyes=eye_cascade.detectMultiScale(face_gray)
        for (ex,ey,ew,eh) in detect_eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        
        detect_smile = smile_cascade.detectMultiScale(face_gray)
        for (sx,sy,sw,sh) in detect_smile:
            cv2.rectangle(face_color,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)
        
    
    cv2.imshow('faces',img)
    
    
    wk=cv2.waitKey(30) & 0xff
    if wk==27:
        break
cam.release()
cv2.destroyAllWindows()
