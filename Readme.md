# Volume Hand Control
Author: Ahmed Hossam Sedky
----
## Libraries versions
* numpy version **1.21.3**
* cv2 version **4.5.4-dev**
* pycaw version **20220416**
* mediapipe version **0.8.10.1**
-----
## Code architecture
* Hand Detection 
    * use mediapipe and cv2  to detect and track hand landmarks in the input image 

* Control Volume with tip and Thumb fingers
    * Use pycaw to set volume of the device 

## Output
![1st Example of output](https://raw.githubusercontent.com/ahmed-sedky/Volume-Hand-Controller/master/Images/output.PNG "1st Example Of Output")
