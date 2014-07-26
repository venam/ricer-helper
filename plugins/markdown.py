
def getName():
    print ("markdown")

def output(state,information):
    categories = information.listCategories()
    selections = state.selected
# testing the output by printing it to stdout 

    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection] :
                    found += 1
                    if found == 1:
                        print( "\n#" + category + "\n")
                    print( "* "+ selection)
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines :
                        print ("    "+line)

