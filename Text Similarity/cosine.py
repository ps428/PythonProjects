#Cosine Similarity by Pranav Soni
import re

text1=input("Text 1 ")
text2=input("Text 2 ")

exceptions=['i','a','and','or','is','was']

if(len(text1)==0):
	text1="What is that ML"
if(len(text2)==0):
	text2="What do you mean by ML"

text1.lower()
text2.lower()
print(text1)
print(text2)

#text1.remove(exceptions)
#text2.remove(exceptions)

words1=text1.split()
words2=text2.split()

words1f  = [word for word in re.split("\W+",words1) if word.lower() not in exceptions]
words2f  = [word for word in re.split("\W+",words2) if word.lower() not in exceptions]


similars=0

for i in words1f:
	for j in words2f:
		if i==j:
			similars+=1

matches=set(words1f).intersection(set(words2f))

print(text1)
print(text2)
print("similars = {}".format(similars))
print("matches = {}".format(len(matches)))

print("Cosine Similarity is {}".format(similars/((len(words1)**.5)*(len(words2)**.5))))	
print("Cosine Matches is {}".format(len(matches)/((len(words1)**.5)*(len(words2)**.5))))	

