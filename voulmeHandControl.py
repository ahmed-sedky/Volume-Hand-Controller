import cv2
import numpy as np
import  time
import handTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volumeRange = volume.GetVolumeRange()
minVolume ,maxVolume = volumeRange[0],volumeRange[1]
vol =0 
volBar =0

cap =  cv2.VideoCapture(0)
widthCam ,heightCam = 640 , 480
cap.set(3 , widthCam)
cap.set(4 , heightCam)
previous_time = 0
detector = htm.HandDetector(detConfidence= 0.7)
while True:
    success ,img = cap.read()
    img = detector.findHands(img)
    landmarkList = detector.findPosition(img, draw=False)
    if len(landmarkList) !=0 :
        lineLength,img,line_info = detector.find_distance(img,4,8)
        vol = np.interp(lineLength , [8 , 270] , [minVolume ,maxVolume])
        volBar = np.interp(lineLength , [8 , 270] , [400 ,150])
        volPercentge = np.interp(lineLength , [8 , 270] , [0 ,100])
        volume.SetMasterVolumeLevel(vol, None)
        print(lineLength, vol)
        if(lineLength < 15):
            cv2.circle(img, (line_info[4],line_info[5]) , 8 ,(0 ,255 , 0) , cv2.FILLED)
        cv2.rectangle(img,(50,150) , (85 ,400) , (0,255,0), 3)
        cv2.rectangle(img,(50,int(volBar)) , (85 ,400) , (0,255,0), cv2.FILLED)
        cv2.putText(img, f'{int (volPercentge)}%',(50,450), cv2.FONT_HERSHEY_PLAIN , 2,(0,255,0) , 2)

    current_time = time.time() 
    fbs = 1 / (current_time - previous_time)
    previous_time = current_time
    cv2.putText(img, f'fbs: {int (fbs)}%',(10,30), cv2.FONT_HERSHEY_PLAIN , 2,(0,255,0) , 2)
    cv2.imshow("Image" , img)
    cv2.waitKey(1)