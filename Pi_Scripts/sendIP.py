execfile("/home/pi/CC_Python/CCEmail.py")
execfile("/home/pi/CC_Python/CCNetwork.py")

ccn = CCNetwork()
cce = CCEmail()

while True:
    if ccn.internet_on():
        cce.server = '[Enter SMTP Server]'
        cce.port = [Enter Port]
        cce.password = '!{Enter Server Password'
        cce.fromaddr = '[Enter From Address]'
        cce.toaddr = '[Enter To Address]'
        cce.subject = "PI Local IP Is: " + ccn.getlocalip()
        cce.body = "PI Local IP Is: " + ccn.getlocalip()
        cce.body += '\n'
        cce.body += "PI External IP Is: " + ccn.getexternalip()
        cce.SendEmail()
        break