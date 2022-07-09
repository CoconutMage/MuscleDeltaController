import threading
import os

def RestAPI():
	threading.Timer(5.0, RestAPI).start()
	#print("Hello World")

fp = open('restPID.txt', 'w')
fp.write(str(os.getpid()))
fp.close()
RestAPI()
