import re

text1=input("Text 1 ")
text2=input("Text 2 ")

exceptions=['i','a','an','the','and','or','is','was']

if(len(text1)==0):
	text1="What is that ML"
if(len(text2)==0):
	text2="What do you mean by ML"

text1.lower()
text2.lower()
print("\nStrings to be compared are:")
print(text1)
print(text2)


words1=text1.split()
words2=text2.split()

modwords1 = len(words1)
modwords2 = len(words2)

for x in exceptions:
	if x in words1:
		words1.remove(x)

for x in exceptions:
	if x in words1:
		words1.remove(x)

# matches=set(words1).intersection(set(words2))


# print("\nmatches = {}".format(len(matches)))
# print("Matches are:\n",matches)

# print("\nCosine Similarity is {}".format(len(matches)/(((modwords1**.5)*(modwords2**.5)))))	

similar=[]
for i in words1:
	for j in words2:
 		if j==i:
 			similar.append(i)

print(similar)
print("\nCosine Similarity is {}".format(len(similar)/(((modwords1**.5)*(modwords2**.5)))))	
