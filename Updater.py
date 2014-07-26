from urllib import URLopener
import time
import md5

class Updater:
    def __init__(self,server):
        self.server = server
        self.br = URLopener()

    def hasNewInfo(self,infoFile):
        f = open(infoFile,'r').read()
        m = md5.new(f).hexdiget()
        response = self.br.open(self.server+'/hash').read()
        return (m==response)

    def generateTimeStamp(self):
        return str(time.gmtime().tm_year)+"_"+str(time.gmtime().tm_mday)+"_"+str(time.gmtime().tm_hour)+"_"+str(time.gmtime().tm_min)

    def fetchNewInfo(self):
        print ("fetching Info")
        response = self.br.open(self.server+'/info.json').read()
        oldInfo = open("info.json",'r').read()
        open("info.json."+generateTimeStamp,'w').write(oldInfo)
        open("info.json",'w').write(response)

