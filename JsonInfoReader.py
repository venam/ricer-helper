# -*- coding: utf-8 -*-

import sys
import json

class JsonInfoReader:
    def __init__(self,infoFile, updater):
        self._infoFile = infoFile
        self._allInfo  = json.load(open(infoFile,'r'))
        self._updater  = updater

    def refresh(self):
        self._allInfo = json.load(open(infoFile,'r'))

    def update(self):
        if self._updater.hasNewInfo(self._infoFile):
            try:
                self._updater.fetchNewInfo()
                self.refresh()
            except Exception:
               sys.exit() 

    def listCategories(self):
        categories = []
        for info in self._allInfo:
            categories.append(info)
        return categories

    def listInsideCategories(self,categorie):
        if categorie not in self._allInfo:
            return ""
        for info in self._allInfo[categorie]:
            print( info)

    def getInfo(self,name):
        categorie = self.getCategorie(name)
        if categorie not in self._allInfo:
            return ""
        if name not in self._allInfo[categorie]:
            return ""
        return self._allInfo[categorie][name]

    def getCategorie(self,name):
        thecategorie = ""
        for categorie in self._allInfo:
            for info in self._allInfo[categorie]:
                if name == info:
                    thecategorie = categorie
                    break
            if thecategorie != "":
                break
        return thecategorie

    def update(self):
        print ("updating from server using Updater...")

"""
if __name__ == "__main__" :
    test = JsonInfoReader("info.json")
    test.listCategories()
    print "\n\n"
    test.listInsideCategories("raw")
    print "\n\n"
    print test.getInfo("Shell")
    print "\n\n"
    print test.getCategorie("IM")
    print "\n\n"
"""
