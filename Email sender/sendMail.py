import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

html = '''Enter The Body'''

emailFrom = 'your email'
emailPass = 'password'

#emailList = [your mail list] # or add mail.txt to your emails line by line

file = open('mail.txt','r')
read = file.readlines()

emailList = []
for line in read:
    if not line.strip() in emailList:
        emailList.append(line.strip())

for email in emailList:
    emailTo = email
    try:
        emailMessage = MIMEMultipart()
        emailMessage['From'] = formataddr((str(Header('Enter header text', 'utf-8')), emailFrom))
        emailMessage['To'] = emailTo
        emailMessage['Subject'] = 'Enter subject'

        emailMessage.attach(MIMEText(html,'html'))

        emailString = emailMessage.as_string()

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
            server.login(emailFrom,emailPass)
            server.sendmail(emailFrom,emailTo,emailString)
            print(f'[+] {emailTo} sent')
    except:
        print(f'[-] {emailTo} send email failed')
