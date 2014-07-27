from urllib import URLopener
#if python3
#from urllib import request
import time
import md5

class Updater:
    def __init__(self,server,infoFile):
        self._server = server
        self._infoFile = infoFile
        self.br = URLopener()
        #if python3
        #self.br = request

    def hasNewInfo(self):
        f = open(self._infoFile,'r').read()
        m = md5.new(f).hexdigest()
        response = self.br.open(self._server+'/hash').read()
        #if python3
        #response = self.br.urlopen(self._server+'/hash').read()
        response = response.replace("\n","")
        print(response)
        print(m)
        return (m!=response)

    def generateTimeStamp(self):
        return str(time.gmtime().tm_year)+"_"+str(time.gmtime().tm_mday)+"_"+str(time.gmtime().tm_hour)+"_"+str(time.gmtime().tm_min)

    def fetchNewInfo(self):
        print ("fetching Info")
        response = self.br.open(self._server+'/info.json').read()
        #if python3
        #response = self.br.urlopen(self._server+'/info.json').read()
        oldInfo = open(self._infoFile,'r').read()
        open(self._infoFile+"."+self.generateTimeStamp(),'w').write(oldInfo)
        open(self._infoFile,'w').write(response)

