import JsonStateHandler

class State:
    def __init__(self):
        self.selected = []
        self.comments = {}

    def load(self, loadLocation):
        JsonStateHandler.load(loadLocation,self)

    def save(self, savelocation):
        JsonStateHandler.save(savelocation,self)

    def addComment(self, section,comment):
        self.comments[section] = comment

    def unComment(self, section):
        if section in self.comments:
            del(self.comments[section])

    def addSelect(self, section):
        if section not in self.selected:
            self.selected.append(section)

    def unSelect(self, section):
        if section in self.selected:
            self.selected.remove(section)


