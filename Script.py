# -*- coding: utf-8 -*-

from selenium import webdriver #minimum needed to webscrap - more info are available on more complex projects, cf. EPN infocentre scraping
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pickle






##Begin The text Extraction
'''topfile = open('ELEMENTS.txt', 'rb')
totaltext = ""
def search_string_in_file(file_name, string_to_search):
    filename = 'ELEMENTS.txt'
    line_number = -1
    list_of_results = []


    file = open(filename, 'rb')

    for line in file:
        line_number += 1
        if string_to_search in line:
            list_of_results.append(line_number)


    return list_of_results


matched_lines = search_string_in_file('ELEMENTS.txt', 'NOTE Confidence')

lines = topfile.readlines()
for line in matched_lines:
    totaltext = totaltext + (lines[line + 4]).rstrip() + " "

document = Document()
document.add_paragraph(totaltext)
document.save('demo2.docx')'''

myfile = 'demo3.txt';
myIndexListFile = "list.txt"
originalFile = open('ELEMENTS.txt','a+')
contents = originalFile.readlines()
newContnent = ""
translatedTextt = ""
globalIndex = 13
#print contents
chrome_options = Options()
chrome_options.add_extension('C:\Users\Oussama\PycharmProjects\BilelScript\AdBlock.crx')

driver = webdriver.Chrome(executable_path='C:\Users\Oussama\PycharmProjects\BilelScript\chromedriver',chrome_options=chrome_options)
driver.set_window_size(1536,864)
driver.switch_to.window(driver.window_handles[0])
time.sleep(8)
driver.get("https://www.reverso.net/traduction-texte#sl=eng&tl=ara")

with open(myIndexListFile, 'rb') as f:
    indexListFromFile = pickle.load(f)
with open(myfile) as file:
    myTxtLines = file.readlines()
#f =  open("ELEMENTS.txt", "w")
print("this is indexListFromFile", indexListFromFile)
firstIndex = 0
numberOfLinesOfOriginalPhrase = 0
def listToString(s):
    # print(s);
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))
def addToThisLine(line,wordsAddedForThisLine):
    global newContnent
    global contents
    print ("this one " , contents[line - 1])
    str1 = ' '.join(wordsAddedForThisLine)
    # str1 = str1.decode("utf8")
    # contents = contents + str1 + '\n'
    contents.insert(line, "\n")
    contents.insert(line, str1)
    whatThat = listToString(contents)

    with open(myIndexListFile, 'wb') as f:
        f.write(whatThat)

    # print ("content" , contents)

def getText(filename):
    global firstIndex
    global numberOfLinesOfOriginalPhrase
    global contents
    global translatedTextt
    global globalIndex
    #doc = docx.Document(filename)
    indexVariable = 0

    #print(myTxtLines)
    for paragraph in myTxtLines:
        if len(driver.find_elements_by_id("dapp-popup"))>0:
            driver.execute_script("document.querySelector('#dapp-popup > div.dapp-popup-right > div > div.dapp-button-wrapper > button').click()")
        driver.find_element(By.XPATH, '/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/textarea').send_keys(paragraph)
        time.sleep(3)
        try:
            try:
                transResult = driver.find_element_by_css_selector(".translation-input__result .sentence-wrapper").text
                translatedTextt = translatedTextt + transResult + " "
                driver.find_element_by_class_name("translation-input__main__close").click()
            except:
                time.sleep(3)
                transResult = driver.find_element_by_class_name(".translation-input__result .sentence-wrapper").text
                translatedTextt = translatedTextt + transResult + " "
                driver.find_element_by_class_name("translation-input__main__close").click()
        except:
            print("An exception occurred")
        print (translatedTextt)
        unicode_text = translatedTextt
        encoded_unicode = unicode_text.encode("utf8")
        # f= open("result.txt","wb")
        # f.write(encoded_unicode)

        translatedText = encoded_unicode
        translatedTextt = ""
        numberOfWordsTrans = len(translatedText.split())
        #print(numberOfWordsTrans)
        wordsTranslatedIntoList = translatedText.split()
        '''     document = Document()

        document.add_paragraph(translatedTextt)

        document.save('result.docx')
        for(i:1, i++, i<numberOfLines){
            line = indexListFromFile[i][0]
            wordsAddedForThisLine = wordsTranslatedIntoList[0:wordsTranslatedToAddedPerLine]
            def addToThisLine(line,wordsAddedForThisLine):

            for myLine in myTxtLines:
                if myLine  = line:
                    myTxtLines[myLine] = wordsAddedForThisLine + '\n'
            del wordsTranslatedIntoList[0:wordsTranslatedToAddedPerLine]
        }'''


        #Loop For Calculate The Number Of Lines of THE original phrase
        for index in indexListFromFile[firstIndex:]:
            if len(driver.find_elements_by_id("dapp-popup"))>0:
                driver.execute_script("document.querySelector('#dapp-popup > div.dapp-popup-right > div > div.dapp-button-wrapper > button').click()")
            if (index[1]) == firstIndex:
                #print(index[1])
                #print (index[0])
                numberOfLinesOfOriginalPhrase += 1
            """if (index[1]) == firstIndex:
                print index[1]
                print 'this is first index variable '
                print firstIndex
                numberOfLinesOfOriginalPhrase += 1
            print (numberOfLinesOfOriginalPhrase)
        wordsTranslatedToAddedPerLine = numberOfWordsTrans % numberOfLinesOfOriginalPhrase
        translatedTextToWordsList = translatedText.split()"""
        '''for wordsToAdd in translatedTextToWordsList:
            print (wordsToAdd)'''
        print (numberOfLinesOfOriginalPhrase)
        if(numberOfLinesOfOriginalPhrase == 0):
            print 'the problem here'
            continue
            #print (numberOfWordsTrans)
        if(numberOfLinesOfOriginalPhrase != 0):
            wordsTranslatedToAddedPerLine = divmod(numberOfWordsTrans, numberOfLinesOfOriginalPhrase)
            print (wordsTranslatedToAddedPerLine[1])
        #print wordsTranslatedToAddedPerLine[0]
        for x in range(numberOfLinesOfOriginalPhrase):
            if len(driver.find_elements_by_id("dapp-popup"))>0:
                driver.execute_script("document.querySelector('#dapp-popup > div.dapp-popup-right > div > div.dapp-button-wrapper > button').click()")
                # driver.find_elements_by_css_selector('').click()
            print("please",x,numberOfLinesOfOriginalPhrase,globalIndex)
            lineWhereToAdd = indexListFromFile[x][0] + 1
            if x == numberOfLinesOfOriginalPhrase - 1 and (wordsTranslatedToAddedPerLine[1] != 0):
                print("we are in the last line and we must add extra words here");
                wordsAddedForThisLine = wordsTranslatedIntoList[0:(wordsTranslatedToAddedPerLine[0] + wordsTranslatedToAddedPerLine[1])]
            else:
                wordsAddedForThisLine = wordsTranslatedIntoList[0:wordsTranslatedToAddedPerLine[0]]
                print('this wordsAddedForThisLine',wordsAddedForThisLine)

            addToThisLine(globalIndex,wordsAddedForThisLine)
            globalIndex = globalIndex + 8
            del wordsTranslatedIntoList[0:wordsTranslatedToAddedPerLine[0]]
        #print (wordsTranslatedToAddedPerLine)
        numberOfLinesOfOriginalPhrase = 0
        firstIndex += 1
        #print (contents)




mynewparagraph = getText(myfile)



# Driver code
whatThat = listToString(contents)

with open(myIndexListFile, 'wb') as f:
    f.write(whatThat)

print "this is the new content"
#print (contents)
#contents = "".join(contents)

def getArrayOfSubParag(parag):
    return parag.split(".")




'''def translateSubPargas():
     translatedText = ""
     newlines = getArrayOfSubParag(mynewparagraph[0])
     chrome_options = Options()
     chrome_options.add_extension('C:\Users\Oussama\PycharmProjects\BilelScript\AdBlock.crx')

     driver = webdriver.Chrome(executable_path='C:\Users\Oussama\PycharmProjects\BilelScript\chromedriver',chrome_options=chrome_options)
     driver.set_window_size(1536,864)
     driver.switch_to.window(driver.window_handles[0])
     driver.get("https://www.reverso.net/traduction-texte#sl=eng&tl=ara")

     time.sleep(3)
     for newOn in newlines:
        print (newOn)
        driver.find_element(By.XPATH, '/html/body/app-root/app-translation/div/app-translation-box/div[1]/div[1]/div[2]/div[1]/div[1]/div/div[1]/textarea').send_keys(newOn)
        time.sleep(3)
        try:
            transResult = driver.find_element_by_class_name("sentence-wrapper_without-hover").text
            translatedText = translatedText + transResult + " "
            driver.find_element_by_class_name("translation-input__main__close").click()
        except:
            print("An exception occurred")
     print (translatedText)
     unicode_text = translatedText
     encoded_unicode = unicode_text.encode("utf8")
     f= open("result.txt","wb")
     f.write(encoded_unicode)
     document = Document()

     document.add_paragraph(translatedText)

     document.save('result.docx')
     unicode_text = u''
     encoded_unicode = unicode_text.encode("utf8")

     a_file = open("textfile.txt", "wb")
     a_file.write(encoded_unicode)
     return translatedText
'''
'''def addingTextAfterTranslate(file,line,index):
    with open(file, "r") as in_file:
        buf = in_file.readlines()

    with open(file, "w") as out_file:
        for line in buf:
            if line == "; Include this text\n":
                line = line + "Include below\n"
            out_file.write(line)

translateSubPargas()'''
#End The text Extraction


##Begin The text Translation


'''driver = webdriver.Chrome(executable_path='C:\Users\Oussama\PycharmProjects\BilelScript\chromedriver')
driver.set_window_size(1536,864)
driver.get("https://www.reverso.net/traduction-texte#sl=eng&tl=ara&text=dfdfdfsdfdsf")
time.sleep(3)

lang = driver.find_element_by_class_name('language-select').click()
ActionChains(driver) \
        .key_down(Keys.DOWN) \
        .key_up(Keys.DOWN) \
        .key_down(Keys.ENTER) \
        .key_up(Keys.ENTER) \
        .perform()
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count = count + 1
    text += pageObj.extractText()
    past = pyperclip.copy(text)
    print(text)
    text_area = driver.find_element_by_xpath('//*[@id="translationTools"]/div/div/div/div[2]/div/div[1]/div[1]/div/textarea')
    pyperclip.paste()
    text_area.send_keys(pyperclip.paste())

    time.sleep(5)
    #load_more = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="translateContent"]/div[2]/button[2]/a')))
    copyButton = driver.find_element_by_xpath('//*[@id="translateContent"]/div[2]/button[2]')
    driver.execute_script("arguments[0].scrollIntoView();", copyButton)
    copyButton = copyButton.click()
    resetButton = driver.find_element_by_xpath('//*[@id="translationTools"]/div/div/div/div[2]/div/div[1]/div[1]/div/div[2]/button').click()
    d = pyperclip.paste()
    paragraph = document.add_paragraph(d)
    document.save('demo.docx') # Save document
    time.sleep(2)
    text = ""

#End The text Translation

##Begin The Document Manipulation

#End The Document Manipulation
'''

'''
byteste = "hello oussama abdallah"
pyperclip.copy(byteste)
spam = pyperclip.paste()
print (spam)
driver = webdriver.Chrome(executable_path='C:\Users\Oussama\PycharmProjects\BilelScript\chromedriver')
driver.set_window_size(1536,864)
driver.get("https://translate.systran.net/translationTools/text?lang=fr")


time.sleep(5) # Pause to allow you to inspect the browser.
#document.querySelector('#translationTools > div > div > div > div:nth-child(2) > div > div.row > div:nth-child(1) > div > textarea').value="+ byteste + ";


driver.execute_script(
            "$('#translationTools > div > div > div > div:nth-child(2) > div > div.row > div:nth-child(1) > div > textarea').append('hello world');")





'''
















'''
pdf = FPDF()
pdf.add_page()

pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

text = u"""
Arabic:  
???? ??????????? ??????????
????? ??????????? ??????????
"""

for txt in text.split('\n'):
    pdf.write(8, txt[::-1])
    pdf.ln(8)

pdf.output("unicode.pdf", 'F')
'''





