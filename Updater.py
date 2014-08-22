from urllib import request
from hashlib import md5
import time

class Updater:
    def __init__(self,server,infoFile):
        self._server = server
        self._infoFile = infoFile
        self.br = request

    def hasNewInfo(self):
        f = open(self._infoFile,'r').read()
        m = md5(open(f,'rb').read()).hexdigest()
        response = self.br.urlopen(self._server+'/hash').read()
        response = response.replace("\n","")
        return (m!=response)

    def generateTimeStamp(self):
        return str(time.gmtime().tm_year)+"_"+str(time.gmtime().tm_mday)+"_"+str(time.gmtime().tm_hour)+"_"+str(time.gmtime().tm_min)

    def fetchNewInfo(self):
        response = self.br.urlopen(self._server+'/info.json').read()
        oldInfo = open(self._infoFile,'r').read()
        open(self._infoFile+"."+self.generateTimeStamp(),'w').write(oldInfo)
        open(self._infoFile,'w').write(response)

