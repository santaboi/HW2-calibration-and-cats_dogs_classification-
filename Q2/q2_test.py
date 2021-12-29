import cv2
import numpy as np
import glob
import sys
import os

data_path = "../Q2/Q2_Image"

"""img = cv2.imread(data_path)
h, w = img.shape[: 2]
img = cv2.resize(img , (int(h/4) , int(w/4)))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

def get_chess_contour(data_path):

    # termination criteria
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    a = 11
    b = 8
    objp = np.zeros((b*a,3), np.float32)
    objp[:,:2] = np.mgrid[0:a,0:b].T.reshape(-1,2)

    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.


    img_folder = os.listdir(data_path)

    for fname in img_folder:
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

            # Draw and display the corners
            cv2.drawChessboardCorners(img, (a,b), corners, ret)
            cv2.imshow('img',img)
            cv2.waitKey(-1)
        

    cv2.destroyAllWindows()

get_chess_contour(data_path)