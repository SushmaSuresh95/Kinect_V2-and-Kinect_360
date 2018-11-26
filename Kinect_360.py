import freenect
import cv2
import numpy as np
import os
#RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

#depth image from kinect
def get_depth():
    array,_ = freenect.sync_get_depth()
    array = array.astype(np.uint8)
    return array
#IR image from kinect
def get_irvideo():
    array,_ = freenect.sync_get_video(0,freenect.VIDEO_IR_8BIT)
    return array

if __name__ == "__main__":
    i = 0
    while 1:
        #frame from RGB camera
        frame = get_video()
        #frame from depth sensor
        depth = get_depth()
	#frame from IR sensor
	ir = get_irvideo()
        #RGB image
        cv2.imshow('RGB image',frame)
        #depth image
        cv2.imshow('Depth image',depth)
	#IR image 
	cv2.imshow('IR image',ir)
	#write image to a folder
	#Parallel storage of multiple image 
	cv2.imwrite("Folder_RGB"+"RGB_"+str(i)+".png",frame)
        cv2.imwrite("Folder_depth/"+"Depth_"+str(i)+".png",depth)
	cv2.imwrite("Folder_ir/"+"IR_"+str(i)+".png",ir)
        i = i+1
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
        

    
