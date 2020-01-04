import cv2
vid = cv2.VideoCapture(r"C:\Users\cttc\Desktop\ADITYA AI&ML COURSE\testvideo1.mp4")

face_cascade = cv2.CascadeClassifier(r"C:\Users\cttc\Desktop\ADITYA AI&ML COURSE\Datasets\data\haarcascades\haarcascade_frontalface_alt.xml")

ret,frame = vid.read()

#ret- it is a boolean variable that returns true if the frame is available
#frame - it is an image array captured based on the frames per second

while vid.isOpened(): # o to open the particular video
    ret,frame= vid.read()
    
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray) 
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    cv2.imshow('img',frame)
    key=cv2.waitKey(30)
    if key == ord('q'): #getting the ascii value of 'q'
        break
    
vid.release() #to release the video or else it will run infinitely
cv2.destroyAllWindows()
      