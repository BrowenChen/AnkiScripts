
var natural = require('natural');


//For finding the root word stems.
stemmer = natural.PorterStemmer; 

var stem = stemmer.stem('stems');  
console.log(stem);  
stem = stemmer.stem('stemming');  
console.log(stem);  
stem = stemmer.stem('stemmed');  
console.log(stem);  
stem = stemmer.stem('stem');  
console.log(stem);  

stemmer.attach()
stem = "running".stem()

console.log(stem)


console.log("i am waking up to the sounds of chainsaws".tokenizeAndStem());
