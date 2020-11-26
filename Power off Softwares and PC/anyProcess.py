import os
import time

passw = ""#Enter your sudo password here

prc = input("Enter the process name: ")
tm = input("Enter time to close in minutes:")
tm = float(tm)
tm = tm*60

print("Will close ",prc," in " ,tm/60, " minutes")
x = 20
for i in range(x):
	time.sleep(tm/x)
	left = ((tm/60)/x)*(x-i)	
	s = ("Will close ", prc," in %.2f  minutes"%(left))
	print(s)


print("\n--------Closing now:----------")
task = "sudo pkill "+prc
os.popen("sudo -S %s"%(task),'w').write(passw+'\n')

time.sleep(2)

os.system(task)

print("\n--------Closed:----------")
