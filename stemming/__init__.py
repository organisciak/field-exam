from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from  nltk.stem.snowball import EnglishStemmer
from  nltk.stem.wordnet  import WordNetLemmatizer
'''
 Test stemming for field exam 
'''

def main():
    #terms = ["policy", "policies", "police", "retrieval", "retrieved", "retriever"]
    #terms = ["go", "going", "goed", "went", "swim", "swam", "walked", "walking", "walk", "give", "gave"]
    #terms = ["geese", "goose", "octopuses", "octopi", "octopodes"]
    terms = ["batter", "battery", "batteries", "battered"]
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



