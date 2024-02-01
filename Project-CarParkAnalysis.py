import cv2
import pickle
import numpy as np 

#Importing video
vid=cv2.VideoCapture('D:\Data Science\Python Assignment\Computer Vision\Data\CarPark Detection\carPark.mp4')

#Importing the car park rectangle positions
with open('D:\Data Science\Python Assignment\Computer Vision\Data\CarPark Detection\CarParkPosition','rb') as f:
    positionList=pickle.load(f)
#Rectangle features
width, height= 108,45

#This function is designed to crop each parking space
def checkParkSpace(frameProcessed):
    freeSpaceCounter=0
    for pos in positionList:
        x,y=pos
        imageCrop=frameProcessed[y:y+height,x:x+width]
        # cv2.imshow(str(x*y),imageCrop)
        #Counting number of none zero pixels to decide whethere it's empty parking space or not
        count=cv2.countNonZero(imageCrop)
        #image,text,coordination,font,font scale,color in BGR, thickness
        cv2.putText(frame,str(count),(x,y+height-3),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255, 0, 0),2,cv2.LINE_AA)

        #we check all the rectangles' pixel counts then we came up with this numbers
        #empty space
        if count<800:
            #red
            color=(0,255,0)
            thickness=5
            freeSpaceCounter+=1
            

        #Full space
        else:
            color=(0,0,255)
            thickness=2
        #Creating rectangles based on new conditions
        #start/end points,color and thickness
        cv2.rectangle(frame,pos,(pos[0]+width,pos[1]+height),color,thickness)
    #Showing free space count
    cv2.putText(frame,f'Free Space:{freeSpaceCounter}/{len(positionList)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),5,cv2.LINE_AA)




while True:
    #if the current number of frame is equal to the total number of frames
    if vid.get(cv2.CAP_PROP_POS_FRAMES)==vid.get(cv2.CAP_PROP_FRAME_COUNT):
        #reset the video
        vid.set(cv2.CAP_PROP_POS_FRAMES,0)


    #ret:A boolean value indicating whether the frame was successfully read (True if successful, False if not).
    ret,frame=vid.read()

    greyFrame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #kernel size, sigma (standard deviation). Gaussian blurring is highly effective in removing Gaussian noise from an image
    blurFrame= cv2.GaussianBlur(greyFrame,(3,3),1)
    
    #the algorithm determines the threshold for a pixel based on a small region around it
    # InputArray, maxValue, adaptiveMethod,thresholdType,blockSize,C 
    adaptiveFrame=cv2.adaptiveThreshold(blurFrame,250,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)

    #To reduce noises we use median blur
    #kernel size
    medianFrame=cv2.medianBlur(adaptiveFrame,5)

    #This operations consists of convolving an image A with some kernel (B)
    #his maximizing operation causes bright regions within an image to "grow" 
    #A kernel(a matrix of odd size(3,5,7) is convolved with the image.
    #A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel are 1, otherwise, it is eroded (made to zero).
    kernel=np.ones(3,np.uint8)
    dilateFrame=cv2.dilate(medianFrame,kernel=kernel,iterations=1)
       
    #Crop parking spaces
    checkParkSpace(dilateFrame)

    # #Creating the saved car park rectangles in frames
    # for pos in positionList:
    #     #start/end points,color and thickness
    #     cv2.rectangle(frame,pos,(pos[0]+width,pos[1]+height),(255,0,0),2)


    cv2.imshow('Frame',frame)
    # cv2.imshow('Frame',blurFrame)
    # cv2.imshow('Thresh Frame',adaptiveFrame)
    # cv2.imshow('Median Frame',medianFrame)
    # cv2.imshow('Dilate Frame',dilateFrame)
    key=cv2.waitKey(1)

    # Break the loop if the 'ESC' key is pressed
    if key==27:
        break