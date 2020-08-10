import PIL
from PIL import Image

basewidth=100

img = input('Enter Filename with extension: ')

while len(img)<1:	
	print('*******************Enter a valid filename***********************')
	img = input('Enter Filename with extension: ')

wpercent=(basewidth / float(img.size[0]))
hsize=int((float(img.size[1]) * float(wpercent)))
img=img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

out = input('Enter Output Filename or press Enter out.jpg: ')

if len(out)<1:
	img.save('resized_image3.jpg')
else:
	img.save(out+'.jpg')