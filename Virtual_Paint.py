import cv2
import numpy as np 



frameWidth = 640
frameHeight = 480 
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth) #width
cap.set(4,frameHeight) #height
cap.set(10,150) #brightness


myColors = [
    
    [10, 150, 150, 25, 255, 255],      # Orange
    [125, 50, 50, 155, 255, 255],     # Purple
    [40, 50, 50, 80, 255, 255],       # Green
    [100, 150, 50, 140, 255, 255]    # Blue
]#these the the color i want , in the form of [h_min,s_min,v_min,h_max,s_max,v_max]


myColorValues=[[0, 140, 255],
               [128, 0, 128],
               [0, 255, 0],
               [255, 0, 0]]

myPoints = [] #[x,y,colorID]

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>200: 
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri= cv2.arcLength(cnt,True)
            approx= cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #HSV is good for color detection 
    count =0
    newPoints=[]
    for color in myColors:

        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper) #converts the desired color range in white and rest color in black 
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints

# def drawOnCanvas(myPoints,myColorValues):
#     for point in myPoints:
#          cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)
def drawOnCanvas(myPoints, myColorValues):
    for i in range(1, len(myPoints)):
        x1, y1, colorID1 = myPoints[i-1]
        x2, y2, colorID2 = myPoints[i]
        
        # Only connect if same color
        if colorID1 == colorID2:
            cv2.line(imgResult, (x1, y1), (x2, y2), myColorValues[colorID1], 5)


while True:
    success,img = cap.read()
    img = cv2.flip(img, 1) #1 is for horizontal flip , 0 for vertical flip , -1 for both vertical and horizontal
    imgResult = img.copy()
    newPoints=findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
       drawOnCanvas(myPoints,myColorValues) 

    
    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break