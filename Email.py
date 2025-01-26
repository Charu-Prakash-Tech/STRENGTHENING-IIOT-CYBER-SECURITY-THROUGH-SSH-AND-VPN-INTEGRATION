import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = "charusam3011@gmail.com"
recipient_email = "charusam3011@gmail.com"
smtp_server = "smtp.gmail.com"
smtp_port = 587 
username = "charusam3011@gmail.com"
password = "Password"
subject = "Test Email"
body = "Message"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, recipient_email, message.as_string())
print("Email sent successfully!")
