# -*- coding: utf-8 -*-
#pip install opencv-python
import cv2
#colored image
img = cv2.imread("img1.jpeg")
print('image ', img)
print('type ',type(img))
print('shape ',img.shape)
cv2.imshow("IISC ",img)

# black and white (Gray scale)
img_1=cv2.imread("img1.jpeg",0)
print(img_1)
cv2.imshow("Image 2",img_1)
resized_image = cv2.resize(img_1,(650,500))
print('re sized image ',resized_image)
cv2.imshow("Resized",resized_image)

resized_image1 = cv2.resize(img_1,(int(img_1.shape[1]/2),int(img_1.shape[0]/2)))
print('resized image size',resized_image1.shape)
cv2.waitKey(0)
#cv2.waitKey(2000)
cv2.destroyAllWindows()