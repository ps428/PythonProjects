import os
import time
a=int(input("Enter duration for checking ram usage in seconds: "))

while(True):
	os.system("free")
	time.sleep(3)
	a-=3
	if(a==0):
		break