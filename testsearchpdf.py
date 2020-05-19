# import packages
import PyPDF2
import re

# open the pdf file
object = PyPDF2.PdfFileReader("test.pdf")
writer = PyPDF2.PdfFileWriter()

# get number of pages
NumPages = object.getNumPages()

# define keyterms
String = "crud"

# extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    print("this is page " + str(i)) 
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(String.lower(), Text.lower())
    if ResSearch:
                writer.addPage(PageObj)
                with open('output.pdf', 'wb') as outfile:
                    writer.write(outfile)
                print(ResSearch)