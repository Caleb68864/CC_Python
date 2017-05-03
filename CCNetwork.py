import socket
from requests import get
import urllib


class CCNetwork:

    def __init__(self):
        pass

    def getlocalip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        localip = s.getsockname()[0]
        s.close()
        return localip

    def getexternalip(self):
        try:
            ip = get('https://api.ipify.org').text
            return ip
        except:
            return "0.0.0.0"

    def internet_on(self):
        try:
            ip = get('https://api.ipify.org').text
            return True
        except:
            return False