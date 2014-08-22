import JsonInfoReader
import State
import Outputer
import unittest

class RicerTest(unittest.TestCase):

    def testInfoReader(self):
        info = JsonInfoReader.JsonInfoReader("info.json")
        self.failUnless(len(info.listCategories())>1)
        self.failUnless(len(info.listInsideCategories("raw"))>1)
        self.failIf(len(info.listInsideCategories("Not Real Category"))>0)
        self.failUnless(len(info.getInfo("Bootloader"))>10)
        self.failIf(len(info.getInfo("Not Real Info"))>0)
        self.failUnless(info.getCategory("Bootloader")=="raw")
        self.failIf(info.getCategory("Not Real Category")=="raw")
        self.failIf(info.getCategory("Not Real Category")!="")

    def testState(self):
        state = State.State()
        state.addSelect("Bootloader")
        state.addComment("Bootloader","I use a magenta... blah blah")
        self.failUnless(len(state.comments) == 1)
        self.failUnless(len(state.selected) == 1)
        state.addSelect("Window manager")
        state.addComment("Window manager", "SuperWM ftw")
        self.failUnless(len(state.comments) == 2)
        self.failUnless(len(state.selected) == 2)
        state.addSelect("GUI")
        state.addComment("GUI", "gtk theme: a modified version of XXX that can be found here\nhttp://example.com")
        self.failUnless(len(state.comments) == 3)
        self.failUnless(len(state.selected) == 3)
        state.unComment("Not Real Comment")
        self.failUnless(len(state.comments) == 3)
        self.failUnless(len(state.selected) == 3)
        state.unComment("GUI")
        self.failUnless(len(state.comments) == 2)
        self.failUnless(len(state.selected) == 3)
        state.unSelect("GUI")
        self.failUnless(len(state.comments) == 2)
        self.failUnless(len(state.selected) == 2)
        state.comments = {}
        state.selected = []
        state.load("conf.json")
        self.failUnless(len(state.comments) > 0)
        self.failUnless(len(state.selected) > 0)

    def testOutputer(self):
        out = Outputer.Outputer()
        self.failUnless(len(out.getAvailable())>0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
