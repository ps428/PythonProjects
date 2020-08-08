Hello there! This repository has various Python projects made during my learning.

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
			I have also added some exceptions at line 7 in the code, these words will be excluded from set of words reserved for comparision. 

