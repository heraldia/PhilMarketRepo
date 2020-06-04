# -*- coding: utf-8 -*-
"""
Created on Sun May 20 16:27:11 2018

@author: user
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils
import pandas as pd
def position_determine(x,y,img_shape):
    if x>0 and x<=img_shape[1]/3:
        if y>0 and y<=img_shape[0]/3:
            return 1
        elif y>img_shape[0]/3 and y<=img_shape[0]*2/3:
            return 4
        else:
            return 7
    if x>img_shape[1]/3 and x<=img_shape[1]*2/3:
        if y>0 and y<=img_shape[0]/3:
            return 2
        elif y>img_shape[0]/3 and y<=img_shape[0]*2/3:
            return 5
        else:
            return 8
    else:
        if y>0 and y<=img_shape[0]/3:
            return 3
        elif y>img_shape[0]/3 and y<=img_shape[0]*2/3:
            return 6
        else:
            return 9
#standard
#5 class
standard_0 = cv2.imread('C:/Users/user/Desktop/background.jpg',cv2.IMREAD_COLOR)
img0= cv2.imread('C:/Users/user/Desktop/item.jpg',cv2.IMREAD_COLOR)
#standard_1 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/original/standard_1.jpg',cv2.IMREAD_COLOR)
#standard_2 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/original/standard_2.jpg',cv2.IMREAD_COLOR)
#standard_3 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/original/standard_3.jpg',cv2.IMREAD_COLOR)
#standard_4 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/original/standard_4.jpg',cv2.IMREAD_COLOR)
#standard_5 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/original/standard_5.jpg',cv2.IMREAD_COLOR)
#standard_6 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/original/standard_6.jpg',cv2.IMREAD_COLOR)
#human detection
img_shape=standard_0.shape


    #5 class
for i in range(1,76):
    img0= cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i),cv2.IMREAD_COLOR)
    img1= cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i+1),cv2.IMREAD_COLOR)
    img2 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i+2),cv2.IMREAD_COLOR)
    img3 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i+3),cv2.IMREAD_COLOR)
    img4 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i+4),cv2.IMREAD_COLOR)
    img5 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i+5),cv2.IMREAD_COLOR)
    img6 = cv2.imread('C:/Users/user/AppData/LocalLow/DefaultCompany/screenshots/screen_1280x960_{0}.jpg'.format(7*i+6),cv2.IMREAD_COLOR)

    dst0 = cv2.addWeighted(img0,1,standard_0,-1,255)
    dst1 = cv2.addWeighted(img1,1,standard_1,-1,255)
    dst2 = cv2.addWeighted(img2,1,standard_2,-1,255)
    dst3 = cv2.addWeighted(img3,1,standard_3,-1,255)
    dst4 = cv2.addWeighted(img4,1,standard_4,-1,255)
    dst5 = cv2.addWeighted(img5,1,standard_5,-1,255)
    dst6 = cv2.addWeighted(img6,1,standard_6,-1,255)

    #img to gray
    img2gray0 = cv2.cvtColor(dst0,cv2.COLOR_BGR2GRAY)
    img2gray1 = cv2.cvtColor(dst1,cv2.COLOR_BGR2GRAY)
    img2gray2 = cv2.cvtColor(dst2,cv2.COLOR_BGR2GRAY)
    img2gray3 = cv2.cvtColor(dst3,cv2.COLOR_BGR2GRAY)
    img2gray4 = cv2.cvtColor(dst4,cv2.COLOR_BGR2GRAY)
    img2gray5 = cv2.cvtColor(dst5,cv2.COLOR_BGR2GRAY)
    img2gray6 = cv2.cvtColor(dst6,cv2.COLOR_BGR2GRAY)

    #GaussianBlur
    blurred0 = cv2.GaussianBlur(img2gray0, (5,5), 0)
    blurred1 = cv2.GaussianBlur(img2gray1, (5,5), 0)
    blurred2 = cv2.GaussianBlur(img2gray2, (5,5), 0)
    blurred3 = cv2.GaussianBlur(img2gray3, (5,5), 0)
    blurred4 = cv2.GaussianBlur(img2gray4, (5,5), 0)
    blurred5 = cv2.GaussianBlur(img2gray5, (5,5), 0)
    blurred6 = cv2.GaussianBlur(img2gray6, (5,5), 0)
    #threshold
    thresh0= cv2.threshold(blurred0,253, 255, cv2.THRESH_BINARY)[1]
    thresh1= cv2.threshold(blurred1,253, 255, cv2.THRESH_BINARY)[1]
    thresh2= cv2.threshold(blurred2,250, 255, cv2.THRESH_BINARY)[1]
    thresh3= cv2.threshold(blurred3,250, 255, cv2.THRESH_BINARY)[1]
    thresh4= cv2.threshold(blurred4,250, 255, cv2.THRESH_BINARY)[1]
    thresh5= cv2.threshold(blurred5,250, 255, cv2.THRESH_BINARY)[1]
    thresh6= cv2.threshold(blurred6,250, 255, cv2.THRESH_BINARY)[1]
    thresh0 = cv2.bitwise_not(thresh0)
    thresh1 = cv2.bitwise_not(thresh1)
    thresh2 = cv2.bitwise_not(thresh2)
    thresh3 = cv2.bitwise_not(thresh3)
    thresh4 = cv2.bitwise_not(thresh4)
    thresh5 = cv2.bitwise_not(thresh5)
    thresh6 = cv2.bitwise_not(thresh6)
    cX_list=[]
    cY_list=[]

    thresh=[thresh0,thresh1,thresh2,thresh3,thresh4,thresh5,thresh6]
    # find contours in the thresholded image
    for threshi in thresh: 
        cnts = cv2.findContours(threshi.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]          
        if len(cnts)!=0:
            x_list=[]
            y_list=[] 
            for c in cnts:
                # compute the center of the contour
                M = cv2.moments(c)
                if(M["m00"]==0):
                    cX = int(M["m10"] / (M["m00"]+0.01))
                    cY = int(M["m01"] / (M["m00"]+0.01))
                else:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                        # draw the contour and center of the shape on the image
                cv2.drawContours(threshi, [c], -1, (255, 0, 0), 2)
                cv2.circle(threshi, (cX, cY), 7, (139,62, 47), -1)
                x_list.append(cX)
                y_list.append(cY)
                cv2.putText(threshi, "center", (cX - 20, cY - 20),
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            while 0 in x_list:
                x_list.remove(0)
            while 0 in y_list:
                y_list.remove(0)
            if len(x_list)>1:
                x_list.pop()
            if len(y_list)>1:
                y_list.pop()
            X=int(np.sum(x_list)/len(x_list))
            Y=int(np.sum(y_list)/len(y_list))
            cX_list.append(X)
            cY_list.append(Y)  
        else:
            cX_list.append(0)
            cY_list.append(0)  
    # find contours in the thresholded image----clustering
    class_photo=position_determine(cX_list[5],cY_list[5],img_shape)
    feature=[cX_list[0],cY_list[0],cX_list[1],cY_list[1],cX_list[2],cY_list[2],cX_list[3],cY_list[3]
    ,cX_list[4],cY_list[4],cX_list[6],cY_list[6],class_photo]
      
    df.loc[i]=feature      
    #df=pd.DataFrame(data=[feature],columns=['camera0_x', 'camera0_y',
                           #    'camera1_x','camera1_y',
                           #      'camera2_x', 'camera2_y',
                           #   'camera3_x','camera3_y',
                            #       'camera4_x','camera4_y',
                            #      'camera6_x','camera6_y',
                              #     'class'])
#df.to_csv('C:/Users/user/Desktop/train.csv',index=False)