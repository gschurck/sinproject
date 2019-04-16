import paramiko, os

host = "192.168.43.13"
port = 22
username = "pi"
password = "raspberry"

# Connect to Android Device
print ('Start Connexion...')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password)
sftp = ssh.open_sftp()
print ('Connected.')


# raspistill -o /home/pi/image01.jpg
# scp image01.jpg pi@192.168.43.13:/var/www/html
# ...
# ...
# ...

# End Script
sftp.close()
ssh.close()