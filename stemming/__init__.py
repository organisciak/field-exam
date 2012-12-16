from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from  nltk.stem.snowball import EnglishStemmer
from  nltk.stem.wordnet  import WordNetLemmatizer
'''
 Example of stemming when it works and when it doesn't. 
'''

def main():
    terms = ["policy", "policies", "police", "retrieval", "retrieved", "retriever", "go", "going", "goed", "went", "swim", "swam", "walked", "walking", "walk", "give", "gave", "geese", "goose", "octopuses", "octopi", "octopodes", "batter", "battery", "batteries", "battered"]
    stemmers = [LancasterStemmer(), PorterStemmer(), EnglishStemmer(ignore_stopwords=False), WordNetLemmatizer()]
    
    print "Stemmer".upper(), "\t", "\t".join(terms).upper()
    for st in stemmers:
        print st.__repr__(), "\t",
        for term in terms:
            if st.__repr__() == '<WordNetLemmatizer>':
                 print st.lemmatize(term), "\t", 
            else:
                print st.stem(term), "\t", 
        print
    
if __name__ == '__main__':
    main()



