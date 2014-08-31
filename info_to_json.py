import json

my_file = open("pad_info",'r').readlines()

section    = -1
category   = -1
sections   = []
categories = []
dico       = {}
tmp_dico   = {}
output     = ""

for line in my_file:
    if line.startswith("!!!"):
        sections.append(line.replace("!!!","").rstrip())

for line in my_file:
    if line.startswith("##"):
        categories.append(line.replace("##","").rstrip())

for i in range(len(my_file)):
    if my_file[i].startswith("!!!"):
        if section != -1:
            dico[sections[section]] = tmp_dico
        section  += 1
        tmp_dico  = {}
    elif my_file[i].startswith("##"):
        if category != -1:
            tmp_dico[categories[category]] = output
        category += 1
        output    = ""
    else:
        output += my_file[i].replace('"','\"')
        #output = output.replace("\n","\\n")
        if i+1 != len(my_file) and my_file[i+1].startswith("!!!"):
            tmp_dico[categories[category]] = output
        elif i+1 == len(my_file):
            dico[sections[section]] = tmp_dico



print json.JSONEncoder().encode(dico)
    

