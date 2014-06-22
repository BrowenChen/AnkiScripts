# # For samir
# import webbrowser
# import pdfminer
# from pattern.web import URL
# #open up the url's
# def scoreSheet(x, y):
# 	for x in range(x, y):
# 		store(x)
# 		scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(x) + ".pdf"
# 		webbrowser.open_new_tab(scoreUrl)


# #Now download and store them into samples/ folder

# def store(num):
# 	scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(num) + ".pdf"

# 	url = URL(scoreUrl)
# 	f = open("OED" + str(num) + ".pdf", 'wb')
# 	f.write(url.download(cached=False))
# 	f.close()
# 	print("Finished downloading " + str(num))
# 	#

# #These are stored in the same folder as scoreScraper.py

# #Parse the data




# scoreSheet(65, 80)


# For samir
import webbrowser
import pdfminer
from pattern.web import URL

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

import re

#open up the url's
def scoreSheet(x, y):
	for x in range(x, y):
		store(x)
		scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(x) + ".pdf"
		webbrowser.open_new_tab(scoreUrl)


#Now download and store them into samples/ folder

def store(num):
	scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(num) + ".pdf"

	url = URL(scoreUrl)
	f = open("OED" + str(num) + ".pdf", 'wb')
	f.write(url.download(cached=False))
	f.close()
	print("Finished downloading " + str(num))
	#

#These are stored in the same folder as scoreScraper.py

#Parse the data



def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()

    info = [0] * 10

    info = re.findall(r"[-+]?\d*\,\d+|\d+", str)

    #company name
    data = (str.splitlines()[0])

    #global
    info[1] = re.sub(',', '.', info[1])
    data = data + ', ' + (info[1])

    #Idea and context
    info[2] = re.sub(',', '.', info[2])
    data = data + ', ' + (info[2])
    #tech
    info[3] = re.sub(',', '.', info[3])
    data = data + ', ' + (info[3])
    #Businesmodel
    info[4] = re.sub(',', '.', info[4])
    data = data + ', ' + (info[4])
    #Team
    info[5] = re.sub(',', '.', info[5])
    data = data + ', ' + (info[5]) + "\n"

    f = open('workfile.csv', 'a')

    f.write(data);


def mineData(x,y):

	# str = "awefaewf,awefawe"
	# str = re.sub(',', '.', str)
	# print str

	for i in range(x, y):
		print('converting: ' + str(i))
		convert_pdf_to_txt('OED' + str(i) + '.pdf')
scoreSheet(1, 80)
mineData(1,80)