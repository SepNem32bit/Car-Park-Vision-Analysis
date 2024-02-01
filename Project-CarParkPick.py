#This code is used to pick car park space in images manually for training models
import cv2
import pickle 



#Rectangle features
width, height= 108,45

#Checking if we have a saved car park position mask
try:
    with open('D:\Data Science\Python Assignment\Computer Vision\Data\CarPark Detection\CarParkPosition','rb') as f:
        positionList=pickle.load(f)
except:
    positionList=[]
#This function is created for adding rectangle by left click and removing one by right click
def mouseClick(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        positionList.append((x,y))
    if event==cv2.EVENT_RBUTTONDOWN:
        for idx, pos in enumerate(positionList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                positionList.pop(idx)
    #Saving the position list
    with open('D:\Data Science\Python Assignment\Computer Vision\Data\CarPark Detection\CarParkPosition','wb') as f:
        pickle.dump(positionList,f)



while True:
    #We import image in the loop because we need to regenerate the image after modifications
    img= cv2.imread('D:\Data Science\Python Assignment\Computer Vision\Data\CarPark Detection\carParkImg.png')
    for pos in positionList:
        #start/end points,color and thickness
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,0),2)
    
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',mouseClick)

    key=cv2.waitKey(1)
    # Break the loop if the 'ESC' key is pressed
    if key == 27:
        break