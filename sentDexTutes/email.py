'''
Created on 25-Dec-2017

@author: sridi
'''
print("fdsfsdf")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

fromaddr = "sridineshkr008@gmail.com"
toaddr = "dineshkumareee001@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing"
 
body = "Simply Testing"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "br22murali")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()