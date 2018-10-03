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

    def setFromAddress(self, address):
        self.fromaddr = address

    def setToAddress(self, address):
        self.toaddr = address

    def setSubject(self, subject):
        self.subject = subject

    def setBody(self, body):
        self.body = body

    def setServer(self, server):
        self.server = server

    def setPort(self, port):
        self.port = port

    def setPassword(self, password):
        self.password = password

    # Sends the email with the settings from object
    def SendEmail(self):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        server = smtplib.SMTP(self.server, self.port)
        server.starttls()
        if self.password != "":
            server.login(self.fromaddr, self.password)

        text = msg.as_string()
        try:
            server.sendmail(self.fromaddr, self.toaddr, text)
            print(msg)
        except:
            print("Failed To Send Email")

        server.quit()
