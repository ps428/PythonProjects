Hello there! This repository has various Python projects made during my learning.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fps428%2FPythonProjects&count_bg=%2317DAED&title_bg=%23555555&icon=probot.svg&icon_color=%23E7E7E7&title=Views&edge_flat=false)](https://hits.seeyoufarm.com)

1) Email Senders:

	A)'bulkMail.py'

		Bulk email sender without attachments:
			
			This Python file can be used to send emails to different users in bulk. Primarily for this project, gmail is used to login, other services can also be used by making some changes. I have used smtplib and ssl libraries. 

			User must have openpyxl installed to use this. 

			IMPORTANT: TO USE THIS TOOL, TURN ON "LESS SECURE APPS" ON YOUR GMAIL ACCOUNT. GOOGLE IT FOR MORE INFO.

			CAUTION: DO NOT RENAME THIS PYTHON FILE AS 'email.py', ANYTHING ELSE IS JUST FINE.
			CAUTION: DO NOT USE .value() OR .value() OR .values at line 46. Only use .value for this as it is not a method.
			
			Keep a file names 'emails.py' in same directory.
			Else you can also enter the excel filename which has mails.
			Daily mail limit is 500 mails. 
			It takes about 3-10 seconds to send a mail.
			Make sure mails are in Column A only, doesn't matter if they are hyperlinks. Else edits can be made at line 37.
			Enter sender's email id and password in 'sender_email' {line 26} and 'password' {line 27} variables. 
			Enter your message from line 52 and Subject at line 50.



	B)'bulkMailAttachments.py'

		Bulk email sender with attachments:

			This Python file can be used to send emails with attachments to different users in bulk. Primarily for this project, gmail is used to login, other services can also be used by making some changes.I have used smtplib and ssl libraries. 
			
			User must have openpyxl installed to use this. 

			IMPORTANT: TO USE THIS TOOL, TURN ON "LESS SECURE APPS" ON YOUR GMAIL ACCOUNT. GOOGLE IT FOR MORE INFO.

				
			CAUTION: DO NOT RENAME THIS PYTHON FILE AS 'email.py', ANYTHING ELSE IS JUST FINE.
			CAUTION: DO NOT USE .value() OR .value() OR .values at line 45. Only use .value for this as it is not a method.

			Keep the attachment in same directory. Enter the name of attachment at line 70. If you don't want to keep file at same directory, then you may edit the directory location at line 72.
			Daily mail limit is roughly 500 mails. 
			Keep a file names 'emails.py' in same directory.
			Else you can also enter the excel filename which has mails.
			Make sure mails are in Column A only, doesn't matter if they are hyperlinks. Else edits can be made at line 44.
			It takes about 10-20 seconds to send a mail.Enter Mail id and Password at lines 30 and 31 respectively.
			Enter mail Subject and Body at lines 57 and 59 respectively.

	C)Better Version -> 'mail2.py':

		Same as 'bulkMail.py', but now we can format the text of mail using HTML.

2) Text similarity:

	A)'cosine.py'

		Cosine Similarity:
			In this program, I have used the concept of cosine similarity to compare similarity of two strings.
			
			Cosine Similarity: It is a method to calculate similarity between two strings. To find cosine similarity, firstly make a set of all the words used in the two strings, then we try to find the angle between the sets (vectors) by finding the dot product of the two sets.
			If two the sets of two strings are A and B,and angle between the two sets (vectors) is '@', then dot product of A and B is given by:

				=> A.B=|A|*|B|*cosine(@)
				=> cosine(@) = (A.B)/(|A|*|B|)

				Also, 
					|X| = sq.root(Sum X sub i)

			For more info on cosine similarity, check this out:
			https://www.machinelearningplus.com/nlp/cosine-similarity/

			Using the above explained concept, I have made this program to calculate cosine similarity. 
			This program is not case sensitive, but it can be made so with a few amendments.


3) 'friend.py'
		
		This Python program takes two names as input and give friendship index of the names.

3) 'ImageResizer.py'
		
		This program can be used to resize any image. This is very simple tools so please keep the image file in same directory as this program.

4) "Youtube playlist downloader"

	This is a youtube playlist downloader.
	To download a playlist from youtube,

	You will need "youtube-dl" installed to use this tool, "googleapiclient.discovery", BS4" and "openpyxl" should also be installed using pip/pip3.

	Firstly run the "urlExtracter.py" to get urls of each video of the playlist. You will need Youtube API key for this which is availabe for free with any Google account.

	After running the "urlExtracter.py", copy the links from the terminal to a word file and open the file using excel/ libreoffice and keep "'" as the delimiter to seperate the playlist names.

	In excel to arrange the urls in better way, copy all the urls and do a paste special->Transpose to  make it more readble and remove , by sorting the sheet.
	Now sheet should have the urls in column 1 and commas(",") should be removed by sorting and removing last cells with ",".

	Now run "downloader.py" to download the playlist from youtube using "youtube-dl" command, this programs works very efficiently.
	Just enter filename and no of video to be downloaded form the link.

5) 'Coursera Py4E Capstone'
	
	This directory has Python for everybody Capstone project (with honours content). 
	Contains code for py4e course, taught by Dr. Charles Severance.

...

7) Estimators:	
		i) PI estimator: Used random numbers to estimate the value of PI in Python Language. The basic idea is to find a ration of points generated inside 				    the circle to the points inside the square and equate that to the areas of the respective figures.
