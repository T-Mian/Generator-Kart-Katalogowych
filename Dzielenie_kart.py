import pdb
import csv
from PyPDF2 import PdfFileReader, PdfFileWriter
list = []
with open('bazy_csv/dla2_2021.csv', 'rt',encoding='utf8') as plik:
	spamreader = csv.reader(plik, delimiter=';', quotechar='|')
	for row in spamreader:
		list.append(row[0])
pdf_file = open('dla2_2021.pdf','rb')
pdf_reader = PdfFileReader(pdf_file)
pdf_writer = PdfFileWriter()
global strona;
global pozycja;
strona = 0
pozycja = 0
for index in range (0,len(list)-1):

	pdf_writer.addPage(pdf_reader.getPage(strona))
	pdf_writer.addPage(pdf_reader.getPage(strona+1))
	nazwa = 'wyniki/'+list[pozycja+1]+'.pdf'
	split_file = open(nazwa,'wb')
	print(nazwa+' ok')
	pdf_writer.write(split_file)
	pdf_writer = None
	pdf_writer = PdfFileWriter()
	split_file.close()
	strona += 2
	pozycja += 1
pdf_file.close()
