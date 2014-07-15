import urllib
import md5

class Updater:
    def __init__(self,server):
        self.server = server

    def hasNewInfo(self,infoFile):
        f = open(infoFile,'r').read()
        m = md5.new(f).hexdiget()
        return False

    def fetchNewInfo(self):
        print "fetching Info"

