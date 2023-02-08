import PyPDF2, os
from pathlib import Path
import send2trash
# encrypts all files in a folder and its sub folders
folder_path = Path.cwd() / "paranoia"
num = 0
for foldername, subfolders, filenames in os.walk(folder_path):
    num += 1
    path = folder_path
    for filename in filenames:
        if filename.endswith(".pdf"):
           if num >= 1:
               path = folder_path / foldername / filename
               if filename.endswith(".pdf"):
                   try:
                       print(path)
                       pdf_file = open(path, 'rb')
                       pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                       pdf_writer = PyPDF2.PdfFileWriter()
                       for page_num in range(pdf_reader.numPages):
                           pdf_writer.addPage(pdf_reader.getPage(page_num))

                       pdf_writer.encrypt('cat')
                       resultPDF = open(str(path)[:-4] + "_encrypted.pdf", 'wb')
                       pdf_writer.write(resultPDF)
                       pdf_file.close()
                       send2trash.send2trash(path)

                   except:
                       print("unnable to encrypt " + filename)