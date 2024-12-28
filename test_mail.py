import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "kevin.yang5871@gmail.com"
receiver = ["kevin5871.yang@gmail.com","kevin.yang5871@gmail.com"]
passwd = "ytzl uutn geik qryt"

for i in receiver:    
    msg = MIMEMultipart()
    msg["from"] = sender
    msg["to"] = i
    msg["Subject"] = Header("test send email","utf-8").encode()
              
    body = "This is send by python\nhow are u?"

    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
        server.login(sender,passwd)
        server.sendmail(sender,i,msg.as_string())
    print("success send mail")