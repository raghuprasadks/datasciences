#https://docs.opencv.org/3.2.0/dc/da5/tutorial_py_drawing_functions.html
#https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html
#https://www.superdatascience.com/opencv-face-detection/

import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
img = cv.imread('alpha.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(gray)
#cv.imshow('img',img)

faces = face_cascade.detectMultiScale(gray, 2.5, 2)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()


import cv2
import matplotlib.pyplot as plt
import numpy as np
face_image = cv2.imread('kaushalya.jpg')
grey_img =cv2.cvtColor(face_image,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(20,10))
plt.imshow(grey_img,cmap='gray')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print('face cascade ', face_cascade)
face_detect=face_cascade.detectMultiScale(grey_img,scaleFactor=1.1,minNeighbors=2)
print ('Face found : ',len(face_detect))



import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')



img = cv2.imread('kaushalya.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#faces = face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
    

from urllib.request import urlopen
import cv2 as cv
import numpy as np

url='http://192.168.1.9:8080/shot.jpg'

while True:
    imgResp=urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)



#Final
from urllib.request import urlopen
import cv2 as cv
import numpy as np
import time


url='http://192.168.1.9:8080/shot.jpg'

while True:
    imgResp=urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv.imdecode(imgNp,-1)
    # all the opencv processing is done here
    
    
#    cv.imwrite( "img.jpg");
    cv.imshow('test',img)
  #  time.sleep(20) # Wait for 5 seconds
    '''
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    print(gray)
    cv.imshow('img',img)

    faces = face_cascade.detectMultiScale(gray, 2.5, 2)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv.imshow('img',img)
    '''
    
    
    cv.waitKey(0)
    cv.destroyAllWindows()
    


#from ffnet import mlgraph, ffnet, tmlgraph, imlgraph
#import pylab
#import sys
import cv2 as cv
#import numpy
cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

def detect(image):
 image_faces = []
 bitmap = cv.fromarray(image)
 faces = cv.HaarDetectObjects(bitmap, cascade, cv.CreateMemStorage(0))
 if faces:
  for (x,y,w,h),n in faces:
   image_faces.append(image[y:(y+h), x:(x+w)])
   #cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),3)
 return image_faces

if __name__ == "__main__":
    cam = cv.VideoCapture(0)
    while 1:
        _,frame =cam.read()
        image_faces = []
        image_faces = detect(frame)
        for i, face in enumerate(image_faces):
           cv.imwrite("face-" + str(i) + ".jpg", face)

        #cv2.imshow("features", frame)
        if cv.waitKey(1) == 0x1b: # ESC
            print ('ESC pressed. Exiting ...')
            break



#Another
import cv2
#import sys

#cascPath = sys.argv[1]
#faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
   #     minSize=(30, 30),
    #    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)
 #   cv2.imwrite("face-" + str(i) + ".jpg", frame)
    cv2.imwrite("face-1" + ".jpg", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()



