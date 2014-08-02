def getName():
    print ("html")

def output(state,information):
    categories = information.listCategories()
    selections = state.selected
    # testing the output by printing it to stdout 
    print """
<html>
    <head>
    </head>
    <body>
"""

    for category in categories:
        found = 0
        for selection in selections:
            if information.getCategory(selection) == category:
                if state.comments[selection] :
                    found += 1
                    if found == 1:
                        print( "\n</ul>\n<h2>" + category + "</h2>\n<ul>")
                    print( "\n<li>\n<h3>"+ selection+"</h3><br/>")
                    commentLines = state.comments[selection].split("\n")
                    for line in commentLines :
                        print (line+"<br/>")
    print "</ul>"
    print "</body>"
    print "</html>"

