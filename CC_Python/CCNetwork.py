import socket
from requests import get
import urllib


class CCNetwork:

    def __init__(self):
        pass

    # Gets the machines local ip address
    def getlocalip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        localip = s.getsockname()[0]
        s.close()
        return localip

    # Gets the machines external ip address
    def getexternalip(self):
        try:
            ip = get('https://api.ipify.org').text
            return ip
        except:
            return "0.0.0.0"

    # Tests if there is currently an internet connection
    def internet_on(self):
        try:
            ip = get('https://api.ipify.org').text
            return True
        except:
            return False
