import os
import signal

#Shuts down the RestAPI process and reboots the raspberry pi
fp = open('/home/itAdmin/MuscleDeltaController/restPID.txt', 'r')
line = fp.readline()
print(line)
os.kill(int(line), signal.SIGTERM)
fp.close()

os.system('sudo reboot')
