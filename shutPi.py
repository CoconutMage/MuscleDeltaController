import os
import signal

#Shuts down the RestAPI process and turns off Pi
printf("Shutdown Pi")

fp = open('restPID.txt', 'r')
line = fp.readline()
print(line)
os.kill(int(line), signal.SIGTERM)
fp.close()

os.system('sudo shutdown')
