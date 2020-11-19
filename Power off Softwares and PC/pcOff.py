import os
import time

passw = ""#Enter your sudo password here


tm=input("Enter time to close in minutes:")
tm=float(tm)
tm=tm*60

print("Will close in " ,tm/60, " minutes")
x=20
for i in range(x):
	time.sleep(tm/x)
	left = ((tm/60)/x)*(x-i)	
	s = ("Will close in %.2f  minutes"%(left))
	print(s)


print("\n--------Closing now:----------")
task = "sudo shutdown"
os.popen("sudo -S %s"%(task),'w').write(passw+'\n')

time.sleep(2)

ask = input("Do you want to stop it just now? Press yes to stop boot now: ")
if(ask=='yes'):
	os.system("shutdown -c")
