import os
import shutil
import time

os.rename("/home/pi/image.jpg", "/var/www/html/image.jpg")
shutil.move("/home/pi/image.jpg", "/var/www/html/image.jpg")
time.sleep(1)