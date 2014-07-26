import json


def save(saveLocation,state):
    #save the comments and selected to a json file
    saveOutput  = "{\n"
    saveOutput += '"comments":\n'
    saveOutput += json.JSONEncoder().encode(state.comments)+"\n"
    saveOutput += ',"selections":\n'
    saveOutput += json.JSONEncoder().encode(state.selected)+"\n"
    saveOutput += "}\n"
    open(saveLocation,'w').write(saveOutput)
    print (saveOutput)

def load(loadLocation, state):
    loaded         = json.load(open(loadLocation,'r'))
    state.comments = loaded['comments']
    state.selected = loaded['selections']

