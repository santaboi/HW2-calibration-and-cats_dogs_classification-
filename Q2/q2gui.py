import tkinter as tk
from cv2 import data
import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
import os


root = tk.Tk()
root.title('E94081107 opencv HW2 Q2')
root.geometry('360x360')

data_path = "../Q2/Q2_Image"
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
intrinsic_dict = {}
extrinsic_dict = {}
distortion_dict = {}
inputValue = 0 

def button_event1():
    global data_path 
    global objpoints , imgpoints
    global intrinsic_dict
    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    a = 11
    b = 8
    objp = np.zeros((b*a,3), np.float32)
    objp[:,:2] = np.mgrid[0:a,0:b].T.reshape(-1,2)

    # Arrays to store object points and image points from all the images.


    img_folder = os.listdir(data_path)

    count = 0
    for i , fname in enumerate(img_folder):
        fname = data_path + '/' + fname
        #fname = "../Q2/Q2_Image/7.bmp"
        img = cv2.imread(fname)
        #img = cv2.resize(img , dsize= (256 , 256))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret, corners = cv2.findChessboardCorners(gray, (a,b), None)
        print(fname, ret)

        # If found, add object points, image points (after refining them)
        if ret == True:
            objpoints.append(objp)

            cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            imgpoints.append(corners)
            rett2, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
            #print(mtx)
            #print("this is rvecs" , rvecs)
            #print("this is mtx" , mtx)

            ##########################################################################################################
            rotation_matrix = (rvecs[i][0][0] , rvecs[i][1][0] , rvecs[i][2][0])
            rotation_matrix = cv2.Rodrigues(rotation_matrix)[0]
            extrinsic = np.c_[rotation_matrix , tvecs[i]] #concate
            ##########################################################################################################

            intrinsic_dict[fname] = mtx
            extrinsic_dict[fname] = extrinsic
            distortion_dict[fname] = dist
            # Draw and display the corners
            cv2.drawChessboardCorners(img, (a,b), corners, ret)
            cv2.namedWindow('img', cv2.WINDOW_NORMAL)
            cv2.imshow('img',img)
            cv2.resizeWindow('img', 512 , 512)
            cv2.waitKey(500)
            """count += 1
        if count == 3 :
            break"""
    cv2.waitKey(-1)
    cv2.destroyAllWindows()
        
        


def button_event2():
    global intrinsic_dict
    #print(intrinsic_dict)
    for item in intrinsic_dict.items():
        print(item)
###########################################################################################################################
def retrieve_input():
    global inputValue 
    inputValue=textBox.get("1.0","end-1c") 
    print("get " , inputValue , ".bmp") 
###########################################################################################################################


def button_event3():
    global extrinsic_dict , inputValue 
    """for item in extrinsic_dict.items():
        print(item)"""
    file_name = "../Q2/Q2_Image/" + inputValue + ".bmp"
    print("corresponding extrinsic is \n" , extrinsic_dict[file_name])
    
    
def button_event4():
    global distortion_dict
    #print(intrinsic_dict)
    for item in distortion_dict.items():
        print(item)


def button_event5() :
    global intrinsic_dict , distortion_dict
    for item in distortion_dict.items():
        fname = item[0]
        img = cv2.imread(fname)
        h,  w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(intrinsic_dict[fname], distortion_dict[fname], (w,h), 1, (w,h))

        # undistort
        undistorted = cv2.undistort(img, intrinsic_dict[fname], distortion_dict[fname], None, newcameramtx)
        # crop the image
        x, y, w, h = roi
        undistorted = undistorted[y:y+h, x:x+w]
        cv2.namedWindow(fname, cv2.WINDOW_NORMAL)
        cv2.imshow(fname,undistorted)
        cv2.resizeWindow(fname, 512 , 512)
        cv2.waitKey(500)
    cv2.waitKey(-1)
    cv2.destroyAllWindows()
    


mybutton2_1 = tk.Button(root, text='2.1 Find Corners', command=button_event1)
mybutton2_1.pack()
mybutton2_2 = tk.Button(root, text='2.2 Find intrinsic', command=button_event2)
mybutton2_2.pack()


textBox=tk.Text(root, height=2, width=15)
textBox.pack()
buttonCommit=tk.Button(root, height=1, width=20, background= "cyan", activebackground= "green", text="Commit_for_(3. Test)", command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()


mybutton2_3 = tk.Button(root, text='2.3 Find extrinsic', background= "cyan" , activebackground= "green" , command=button_event3)
mybutton2_3.pack()
mybutton2_4 = tk.Button(root, text='2.4 Find Distortion', command=button_event4)
mybutton2_4.pack()
mybutton2_5 = tk.Button(root, text='2.5 Show Results', command=button_event5)
mybutton2_5.pack()


if __name__ == "__main__":
    root.mainloop()


