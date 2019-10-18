import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = 'example'

sender = 'sketcho@sketch.com'
# rec = 'gslesinger@gmail.com'
rec = 'taddes.korris@gmail.com'



s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
msg = MIMEMultipart()
msg['From'] = 'taddes.korris@gmail.com'
msg['To'] = 'taddes.korris@gmail.com'
msg['Subject'] = 'test'

s.send_message(msg)
del msg
# smptObj.sendmail(sender, rec, message)
# print('Sent message')
