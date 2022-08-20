import os
import signal
import time

#Shuts down the RestAPI process and then restarts it
fp = open('restPID.txt', 'r')
line = fp.readline()
print(line)
os.kill(int(line), signal.SIGTERM)
fp.close()

time.sleep(1)

os.system('python restapi.py &')
