import os
import signal

fp = open('restPID.txt', 'r')
line = fp.readline()
print(line)
os.kill(int(line), signal.SIGTERM)
fp.close()
