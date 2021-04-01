import pyttsx3
import PyPDF2
book = open('object_oriented_python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

page_number = int(input("Enter the page number:"))
page_number = page_number-1

speaker = pyttsx3.init()
for num in range(page_number, pages):
    page = pdfReader.getPage(page_number)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()