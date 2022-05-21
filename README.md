# Eye_Tracker
It combined Python and LabVIEW in this project to manipulate the keyboard and mouse through eyes and voice control. Our concept was to firstly catch the eyes, or more specifically the eye pupils, to locate the cursor (arrow) of the mouse. This section was implemented by LabVIEW in case that it contained many models dealing with embedded cameras. Subsequently, the cursor location would be transferred to coordinates (2D) and recorded in a .txt file. We utilized Python as the interface to visualize where we were watching at. Some simple keyboard instructions, e.g. enter, space, and language translation (in English), are included in the final model to make the dream of being a couch potato comes true.

## Eye Catching
We compared the color contrast in the area near eye pupils to classify where was the center of each eye. In the following, calculated the middle point of eyes (pupils) and project it to the screen. Here, it utilized 3D projection angle to measure the approximately location of our sight. Followed by was that recorded the coordinate projecting to the screen in a .txt file for subsequent processing tasks done by Python.

## Mouse Simulation & Voice Control
It attempted to visualize the cursor location through the coordinates from .txt file. In case that the .txt file was recursively overwritten, the coordinates could update at a response time of about 1 second. In addition, we included some else instructions to make this project more like computer accessories. Blink, nod, and some simple upper-body language meant to replace the instructions of enter, escape, and etc. Except them, we put voice control inside with Pyautogui, which enabled typing according to voice recognition. 

## File Description
- *.vi are LabVIEW files designed by Wei-Che Chung is responsible for eye catching task
- Test_Mouse.py are two files trying to locate pupils and visualize the mouse cursor in two different ways
- Voice_Text_Transfer.py implements typing through voice recognition
- Tracker_with_Voice_Controll.py is the main file and involve the functions mentioned above.

## Operation
Execute the LabVIEW files (.vi) and then the type **Python Tracker_with_Voice_Control.py** to fully perform this project.

## Contact Info
Author: Chun-Sheng Wu, MS student in Computer Engineering @ Texas A&M University  
Email: jinsonwu@tamu.edu  
LinkedIn: https://www.linkedin.com/in/chunshengwu/

*This project was in collaboration with Wei-Che Chung and Tzu-Yang Hung at National Chiao Tung University, 2018*
