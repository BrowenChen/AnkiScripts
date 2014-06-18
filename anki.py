
"""
Owen Chen
Anki parser
--------------
How to reformat a note file by text. Bolded text is the front of the card, unbolded text is tab delimited for the 
back of the Anki Flashcard

v1.0
-bugs
Implement error checking. If the card has any instance of ":", then error will occur.


"""

import sys

front = True
faceCard = []
backCard = []
curCard = ""
 
f = open(sys.argv[1], "r")
lines = f.readlines()



# print lines	
#Strip function takes away whatever is passed in the argument. 
lines = [line.strip('1234567890.') for line in lines]

#Now remove all white lines in the text to reformat
newLine = []
for line in lines:
	if not line.isspace():
		newLine.append(line)

lines = newLine


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

#Write a function that removes all of the white space lines as well

# print lines
# print faceCard
# print backCard

f.close()
 
# #New output for Anki with tab delimited. 
output = ""
 
for i in range(len(faceCard)):
     output += faceCard[i] + "\t" + backCard[i] + "\n"
 


open(sys.argv[2], "w").write(output)

