# -*- coding: utf-8 -*-
from docx import Document
import pickle

##Begin The text Extraction
topfile = open('ELEMENTS.txt', 'rb')
myIndexListFile = "list.txt"
totaltext = ""
lines = topfile.readlines()
def search_string_in_file(file_name, string_to_search):

    line_number = -1
    list_of_results = []
    lineIndex = 0

    file = open(file_name, 'rb')

    for line in file:
        line_number += 1
        if string_to_search in line:
            list_of_results.append((line_number + 4, lineIndex))
            if("." in (lines[line_number + 4])) or ("?" in (lines[line_number + 4])):
                lineIndex += 1
                #print ((lines[line_number + 4]))
    print (list_of_results)
    with open(myIndexListFile, 'wb') as f:
        pickle.dump(list_of_results, f)
    with open(myIndexListFile, 'rb') as f:
        indexListFromFile = pickle.load(f)
    firstIndex = 11
    numberOfLinesOfOriginalPhrase = 0
    for index in indexListFromFile[firstIndex:]:
        if (index[1]) == firstIndex:
            print (index[1])
            numberOfLinesOfOriginalPhrase += 1
    print (numberOfLinesOfOriginalPhrase)

    return list_of_results


'''  print (indexListFromFile[len(indexListFromFile)-1][0])
    print (len(indexListFromFile))'''


matched_lines = search_string_in_file('ELEMENTS.txt', 'NOTE Confidence')


#print (lines[line_number])
for line in matched_lines:
    print ("lets see",len(matched_lines))
    totaltext = totaltext + (lines[line[0]]).rstrip() + " "
    if ("." in lines[line[0]]) or ("?" in lines[line[0]]):

        totaltext = totaltext + "\n"

document = Document()

document.add_paragraph(totaltext)

document.save('bileltest.docx')

