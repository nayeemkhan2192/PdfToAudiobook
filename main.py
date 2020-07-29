

import pyttsx3
import PyPDF2

book = open('oop1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
Agent1 = pyttsx3.init()
for num in range(1,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    Agent1.say(text)
    Agent1.runAndWait()


"""
i=1
while i<2:
    Agent1.say('Khuda lagse')
    Agent1.say('Ki Khabo ajke')
    Agent1.runAndWait()
    i+=1 
"""


