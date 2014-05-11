
"""
Anki parser
--------------
How to reformat a note file by text. Bolded text is the front of the card, unbolded text is tab delimited for the 
back of the Anki Flashcard


"""

import sys
 
f = open(sys.argv[1], "r")
lines = f.readlines()

#Takes away the first 3 spaces in each line. i.e  the Q: and A:  part of the line. Reformats it
#Strip function takes away whatever is passed in the argument. 
lines = [line[3:].strip() for line in lines]
f.close()
 
#New output for Anki with tab delimited. 
output = ""
 
for i in range(0, len(lines), 2):
    output += lines[i] + "\t" + lines[i + 1] + "\n"
 
open(sys.argv[2], "w").write(output[:-1])

