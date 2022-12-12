# LinkedIn Scrapper with Python
ref: https://pypi.org/project/linkedin-jobs-scraper/

## Steps:
1. Just install the required library using: pip3 install linkedin-jobs-scraper
2. This scrapper also needs you to have Chrome drivers, just ping me if there is any issue in runnning it. Simply test the code once with: python3 scape.py
3. If everything is fine, then let's run this in authenticated manner. Just go to cookies and fetch the value of the key 'li_at'...simply google how to get cookies in your particular browser
4. One you get this cookie value, just run this command: LI_AT_COOKIE="your li_at cookie value here" python3 scrape.py
5. Voila! Now all the data would now be stored in the data field!

### Note: If you may use pip instead of pip3 and python instead of python based on your OS.
