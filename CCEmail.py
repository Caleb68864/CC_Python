import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class CCEmail:
    fromaddr = ""
    toaddr = ""
    subject = ""
    body = ""
    server = ""
    port = 0
    password = ""

    def __init__(self):
        pass

    # Sends the email with the settings from object
    def SendEmail(self):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        server = smtplib.SMTP(self.server, self.port)
        server.starttls()
        server.login(self.fromaddr, self.password)
        text = msg.as_string()
        try:
            server.sendmail(self.fromaddr, self.toaddr, text)
            print(msg)
        except:
            print("Failed To Send Email")

        server.quit()
