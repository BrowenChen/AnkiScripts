
"""
Anki parser
--------------
How to reformat a note file by text. Bolded text is the front of the card, unbolded text is tab delimited for the 
back of the Anki Flashcard


"""

import sys

front = True
faceCard = []
backCard = []
curCard = ""
 
f = open(sys.argv[1], "r")
lines = f.readlines()



print lines	
#Strip function takes away whatever is passed in the argument. 
lines = [line.strip('1234567890.') for line in lines]

#Parses text into two dictionaries, frontCard and backCards.

for line in lines:

	if len(curCard) != 0:
		faceCard.append(curCard) if front == True else backCard.append(curCard)
		front = not front
		curCard = ""

	for letter in line:
		curCard += letter
		if letter == ":":
			curCard = curCard[:-1]
			faceCard.append(curCard) if front == True else backCard.append(curCard)
			front = not front
			curCard = ""


if len(curCard) != 0:
	faceCard.append(curCard) if front == True else backCard.append(curCard)
	front = not front
	curCard = ""

print lines
print faceCard
print backCard

f.close()
 
# #New output for Anki with tab delimited. 
output = ""
 
for i in range(len(faceCard)):
     output += faceCard[i] + "\t" + backCard[i] + "\n"
 


open(sys.argv[2], "w").write(output)

