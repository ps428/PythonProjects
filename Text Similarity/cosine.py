import re

text1=input("Text 1 ")
text2=input("Text 2 ")

if(len(text1)==0):
	text1="Julie loves me more than Linda loves me"
if(len(text2)==0):
	text2="Jane likes me more than Julie loves me"

text1.lower()
text2.lower()
print("\nStrings to be compared are:")
print(text1)
print(text2)

words1=text1.split()
words2=text2.split()

matrix1 = {}
for word in words1:
	if word not in matrix1.keys():
		matrix1[word]=0
	matrix1[word]+=1
	
matrix2 = {}
for word in words2:
	if word not in matrix2.keys():
		matrix2[word]=0
	matrix2[word]+=1

modwords1 = 0	
modwords2 = 0

for reps in matrix1.values():
	modwords1 = reps**2 + modwords1

for reps in matrix2.values():
	modwords2 = reps**2 + modwords2

modwords1 = modwords1**.5
modwords2 = modwords2**.5

print('\nWords in each sentance are:')
print(matrix1)
print(matrix2,'\n')

dot=0
matches = {}
for x,a in matrix1.items():
	for y,b in matrix2.items():
		if x == y:
			dot += a*b
			print('{} \t  {}*{} = {}'.format(y,a,b,a*b))

print('------------------')
print("|Dot Product \t{}|".format(dot))
print('------------------')

##****For {n:12.2f}, n is position of variable in format block.
print("\nCosine Similarity is {0}/({1:2.2f}*{2:2.2f}) = {3:2.2f} ".format(dot,modwords1,modwords2,dot/(((modwords1)*(modwords2)))))	
