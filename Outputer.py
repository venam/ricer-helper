import importlib
import plugins
import pkgutil
import inspect

PLUGIN_PATHS = ["plugins"]

class Outputer:
    def lister(self):
        path = PLUGIN_PATHS
        availables = []
        for loader, modname, is_pkg in pkgutil.walk_packages(path):
            module = loader.find_module(modname).load_module(modname)
            good = 0
            for name, value in inspect.getmembers(module):
                if name.startswith('__'):
                    continue
                if name == "getName":
                    good += 1
                if name == "output":
                    good += 1
            #has the 2 functions getName and output, so it's a good plugin
            if good == 2:
                availables.append(modname)
        return availables

    def getAvailable(self):
        #availables = self.lister()
        #for available in availables:
        #    m = importlib.import_module('plugins.'+available)
        #    m.getName()
        return self.lister()

    def output(self, module, state, info, location):
         m = importlib.import_module('plugins.'+module)
         toSave = m.output(state,info)
         open(location, 'w').write(toSave)

"""
if __name__ == "__main__":
    output = Outputer()
    output.getAvailable()
"""

