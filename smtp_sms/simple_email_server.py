import smtplib

email_domain = input('Email please: ')
pw = input('Password Please: ')



smtpObj = smtplib.SMTP('smtp.gmail.com')
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(email_domain, pw)
smtpObj.sendmail(email_domain, 'email_domain, 'Heyo, this is a test')
smtpObj.quit()