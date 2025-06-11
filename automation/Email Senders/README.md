# Bulk Email Sender

A collection of Python scripts for sending emails in bulk to multiple recipients.

## Features

- Send plain text emails to multiple recipients
- Send HTML-formatted emails with styling
- Send emails with file attachments
- Track sent emails in Excel spreadsheet

## Tools Included

### 1. bulkMail.py
Send plain text emails to multiple recipients from an Excel file.

**How it works:**
- Reads email addresses from an Excel spreadsheet (Column A)
- Connects to Gmail's SMTP server
- Sends personalized emails to each recipient
- Takes approximately 3-10 seconds per email

**Usage:**
```
python bulkMail.py
```

**Important Notes:**
- Do NOT rename this file to 'email.py' (will cause import conflicts)
- Make sure to enable "Less secure apps" in your Gmail settings
- Daily limit is approximately 500 emails
- Enter your email and password in the script variables

### 2. bulkMailAttachments.py
Send emails with file attachments to multiple recipients.

**How it works:**
- Reads email addresses from an Excel spreadsheet
- Attaches specified files to each email
- Tracks sent emails by marking them in the spreadsheet
- Takes approximately 10-20 seconds per email

**Usage:**
```
python bulkMailAttachments.py
```

**Important Notes:**
- Keep attachment files in the same directory as the script
- Daily limit is approximately 500 emails
- Automatically saves tracking information to 'Mailing List.xlsx'

### 3. Better Version (mail2.py)
Enhanced email sender with HTML formatting capabilities.

**How it works:**
- Allows rich text formatting using HTML
- Customize colors, fonts, and styles in your emails
- Reads email addresses from an Excel spreadsheet

**Usage:**
```
python mail2.py
```

## Requirements
- Python 3.x
- openpyxl library (`pip install openpyxl`)
- smtplib (included in Python standard library)
- ssl (included in Python standard library)
- Gmail account with "Less secure apps" enabled

## Security Warning
This tool requires your email password. Never share your scripts or commit them to public repositories with your credentials included.