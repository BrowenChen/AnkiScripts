# For samir
import webbrowser
import pdfminer
from pattern.web import URL
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




scoreSheet(65, 80)