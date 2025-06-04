import random

cases = input("Enter number of test cases: ")

def getDis(x,y):
	x_2 = x*x
	y_2 = y*y

	dis = pow(x_2+y_2,0.5)
	# print(dis)
	return dis

points_inside_circle = 0.0
points_inside_square = 0.0

for i in range(1,int(cases)):
	x = random.random()
	y = random.random()
	distance_from_origin = getDis(x,y)

	if(distance_from_origin<=1):
		points_inside_circle+=1
	points_inside_square+=1

# print(points_inside_square,points_inside_circle)

probablity_in_circle = 0.0
probablity_in_circle = 4*points_inside_circle/points_inside_square
print("Estimated value of pi is:",probablity_in_circle)

