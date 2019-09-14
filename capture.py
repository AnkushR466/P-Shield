#for this first install cv2 library
#and your system device camera must be connect
#check it in the top left- Devices-Webcam

import cv2
import subprocess as sp

cap = cv2.VideoCapture(0)
ret, photo = cap.read()

cv2.imwrite("/var/www/html/security/ph.jpg",photo)

cap.release()

sp.getoutput("ansible-playbook /var/www/html/security/mailfile.yml")
