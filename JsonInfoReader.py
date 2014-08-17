# -*- coding: utf-8 -*-

import sys
import json
import Updater

class JsonInfoReader:
    def __init__(self,infoFile):
        self._infoFile = infoFile
        self._allInfo  = json.load(open(infoFile,'r'))
        #might want to read that host from a file
        self._updater  = Updater.Updater("http://venam.nixers.net", self._infoFile)

    def refresh(self):
        try:
            self._allInfo = json.load(open(self._infoFile,'r'))
        except Exception:
            print("cannot re-read file")

    def update(self):
        if self._updater.hasNewInfo():
            try:
                self._updater.fetchNewInfo()
                self.refresh()
                return 0
            except Exception:
                print("Problem Fetching new info")
                return -1
        return 2

    def listCategories(self):
        categories = []
        for info in self._allInfo:
            categories.append(info)
        return categories

    def listInsideCategories(self,category):
        if category not in self._allInfo:
            return ""
        for info in self._allInfo[category]:
            print( info)
        return self._allInfo[category]

    def getInfo(self,name):
        category = self.getCategory(name)
        if category not in self._allInfo:
            return ""
        if name not in self._allInfo[category]:
            return ""
        return self._allInfo[category][name]

    def getCategory(self,name):
        thecategory = ""
        for category in self._allInfo:
            for info in self._allInfo[category]:
                if name == info:
                    thecategory = category
                    break
            if thecategory != "":
                break
        return thecategory


"""
if __name__ == "__main__" :
    test = JsonInfoReader("info.json")
    test.listCategories()
    print "\n\n"
    test.listInsideCategories("raw")
    print "\n\n"
    print test.getInfo("Shell")
    print "\n\n"
    print test.getCategory("IM")
    print "\n\n"
"""
