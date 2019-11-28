import cv2 

  
# capture frames from a video 

cap = cv2.VideoCapture(r'C:\Users\Michael Wibisono\Documents\progrems\piton\DSCN3194.AVI') 
count = 0
  
# Trained XML classifiers describes some features of some object we want to detect 

car_cascade = cv2.CascadeClassifier(r'C:\Users\Michael Wibisono\Documents\progrems\piton\cars.xml') 

  
# loop runs if capturing has been initialized.


# draws rectangle and add frames to car
def passCar():
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,0),2) 
        testing = int('0')
        xint = int('6')
        yint = int('350')
        counter = int('0')
        while(y<=386):    
            counter = counter + 1
#            print(pixelValue)
            if xint == x &  yint == y:
                testing = int('1')
                x=x+1
                break
#            print(pixelValue, testing)
            if counter == 10:
                y=y+1
                counter=int('0')

while True: 

    # # reads frames from a video 
    # while True:
    

    ret, frames = cap.read() 
    
    #     if ret:
    #         cv2.imwrite("frame%d.jpg".format(count), frame)
    #         count += 30
    #         cap.set(1, count)
    #     else:
    #         cap.release()
    #         break

    # convert to gray scale of each frames 

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 

   # Display frames in a window  
    passCar()
    cv2.line(frames,(6,350),(366,386),(0,0,255),3) 
    cv2.line(frames,(238,278),(434,294),(255,0,0),2) 
    cv2.imshow('video2', frames)

      

    # Wait for Esc key to stop 

    if cv2.waitKey(33) == 27: 
        break




# De-allocate any associated memory usage 
cv2.destroyAllWindows()
