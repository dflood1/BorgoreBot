import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime

datelist = []
today = datetime.date.today()
datelist.append(today)

fromaddr = "borgorebot@gmail.com"
toaddr = "borgorebot@googlegroups.com"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = str(datelist[0])
body = "test email from python script"
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"sugardaddy")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()

print "Email sent!"
