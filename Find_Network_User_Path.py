import os
import threading


# Searchs Network IPs for the path to a users folder. Needs to be run with admin rights
class Find_Network_User_Path:

    def __init__(self, user, locIPs):
        self.user = user
        self.locIPs = locIPs
        self.paths = []

        f = open('paths.txt', 'w')
        f.write("")
        f.close()

        downloadThreads = []
        for locip in self.locIPs:
            for i in range(1, 255):
                downloadThread = threading.Thread(target=self.checkUser, args=(self.user, locip, i))
                downloadThreads.append(downloadThread)
                downloadThread.start()

        for downloadThread in downloadThreads:
            downloadThread.join()

        f = open('paths.txt', 'a')
        for path in self.paths:
            f.write(path + "\n")
        f.close()
        print('All IPs Searched.')
        input("Press Enter to continue...")

    def checkUser(self, user, locIP, IP):
        path = "\\\\192.168.{}.{}\\C$\\Users\{}".format(locIP, IP, user)
        if os.path.isdir(path):
            self.paths.append(path)
            print("{} Exists".format(path))
        # else:
        #     print("{} Does Not Exists".format(path))
