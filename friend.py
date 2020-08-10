value=input("Enter names 1 and 2: \n")
point=0
a='a,i,o'
b='r,n,s, '
c='p,h,r,v'

for word in value:
	if word in a:
		point+=1
	elif word in b:
		point+=1
	elif word in c:
		point+=1
	else:
		point+=0		

point = point/(len(value))*100

if point>80:
	print("Your Friendship Score is: ",point)				
	print('Congratulation! you both are best friends')

else:
	print("Your Friendship Score is: ",point)				
