import os
import shutil
import time

os.rename("/home/pi/image.jpg", "/var/www/html/image.jpg")
shutil.copy("/home/pi/image.jpg", "/var/www/html/image.jpg", follow_symlinks=True)
time.sleep(1)