import cv2

alg= "haarcascade_frontalface_default.xml"

haar_cascade= cv2.CascadeClassifier(alg)

cam =cv2.VideoCapture (0)

while True:
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #CONVERTING CLR IMAGE TO GRAY
    face= haar_cascade.detectMultiScale(grayImg,1.3,4) #Getting coordinates
    for (x,y,w,h) in face:
         cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("FaceDetection", img)
    key = cv2.waitKey(10)
    print(key)
    if key==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
