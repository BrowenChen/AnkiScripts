Anki parser

http://archive.wired.com/medtech/health/magazine/16-05/ff_wozniak?currentPage=all

Convert notes from evernote into Anki-readable import files to make learning easier through spaced repitition algorithms. Bolded text will be the front of the flash card while the rest of the text is the back. Cards are seperated by pressing enter, and front and back is seperated by a color. 

Works by converting every line into tab delimited lines that is readable by Anki. 
Updated to account for empty blank line skips in your notes.

Next step would be to be able to feed in an article from Wikipedia and parse that into Anki-readable flashcards. 

<<<<<<< HEAD
TODO:
Create a standalone app for this using py2App. 
=======

HOW TO USE

1) Write notes in evernote in this format:
Face card with the topic : Definition or answer

(1) front of the card (2) : <-- is the seperator (3) is the definition or answer (4) pressing enter for new line is for new card. Note that even if the sentence gets automatically split into a new line, the parser doesnt recognize this as new line so it will still go on the previous card until you hit enter. 

python anki.py <filename> <outputFile>

Then import <outputFile> into an anki deck. Works perfectly if you follow the format. 
>>>>>>> FETCH_HEAD
