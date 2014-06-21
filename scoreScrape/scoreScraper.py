# For samir
import webbrowser

url = "http://google.com"

def open():
	return webbrowser.open("http://google.com", new=2, autoraise=True)

# webbrowser.open_new(url)
webbrowser.open_new_tab(url)

# scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + num + ".pdf"

def scoreSheet():
	for x in range(65, 80):
		scoreUrl = "http://openeducationchallenge.eu/sites/default/files/Phase3Results/OECPhase3Results_" + str(x) + ".pdf"
		webbrowser.open_new_tab(scoreUrl)



