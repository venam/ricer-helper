
def getName():
    print ("bbcode")

def output(state,information):
    categories = information.listCategories()
    selections = state.selected
    # testing the output by printing it to stdout 

    firstOne = True
    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection] :
                    found += 1
                    if found == 1:
                        if not firstOne:
                            print( "[/list]")
                        print ("\n[size=9]" + category + "[/size]\n[list]\n")
                        firstOne = False
                    print( "[*][size=5]"+ selection+"[/size]")
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines :
                        print ("    "+line)
    print "[/list]"

