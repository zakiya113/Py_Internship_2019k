import PyPDF2


file = open('C:\\Users\\minds9\\PycharmProjects\\Internship_2019\\TestPDF\\MOM 17-09.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())

pageobj = pdfreader.getPage(0)
print(pageobj.extractText())

file.close()


