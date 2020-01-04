import cv2
 #load the cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\cttc\Desktop\ADITYA AI&ML COURSE\Datasets\data\haarcascades\haarcascade_frontalface_alt.xml")
 
 #Read the input image
img = cv2.imread(r"C:\Users\cttc\Desktop\ADITYA AI&ML COURSE\testimage4.jpg")
 
 #convert into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 #Detect faces
faces = face_cascade.detectMultiScale(gray)
 #Draw rectangle around the faces
for (x , y, w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w ,y+h),(255,0,0),2)
#Display the output
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()