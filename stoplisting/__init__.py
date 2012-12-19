'''
Python code

Example of word frequencies with and without stopwords.

Uses Natural Language Toolkit (NLTK) - Bird et al. 2009

bush.txt is from http://www.bartleby.com/124/pres66.html
obama.txt is from http://www.whitehouse.gov/blog/inaugural-address
'''

from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

def main():
	# Number of words to display
	count = 40

	# Open files as strings
	obama = open("obama.txt", "r").read()
	bush = open("bush.txt", "r").read()

	#Tokenize texts into words, then count frequencies for all words
	top_obama = FreqDist(word.lower() for word in word_tokenize(obama))
	top_bush = FreqDist(word.lower() for word in word_tokenize(bush))
	
	#Return top {count} most occurring words
	print "No stoplist".upper()
	print "Obama/2009\t".upper(), " ".join(item[0] for item in top_obama.items()[:count])
	print "Bush/2001\t".upper(), " ".join(item[0] for item in top_bush.items()[:count])

	#Return most occurring words that are not in the NLTK English stoplist
	print
	print "Stoplisted".upper()
	print "Obama/2009\t".upper(), " ".join([item[0] for item in top_obama.items() if not item[0] in stopwords.words('english')][:count])
	print "Bush/2001\t".upper(), " ".join([item[0] for item in top_bush.items() if not item[0] in stopwords.words('english')][:count])

if __name__ == '__main__':
    main()
