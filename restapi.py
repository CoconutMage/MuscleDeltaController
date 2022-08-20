#This is a testing file to simulate the RestAPI program
#Running in the background
import threading
import os

def RestAPI():
	threading.Timer(5.0, RestAPI).start()
	#print("Hello World")

fp = open('restPID.txt', 'w')
fp.write(str(os.getpid()))
fp.close()
RestAPI()
