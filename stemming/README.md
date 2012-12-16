==Stemming==
This is a *very* trivial use of stemming, comparing Lancaster (Paice 1990), Porter (Porter 1981), and English Snowball (Porter 2001) stemmers, as well as a WordNet lemmatizer, all using the Natural Language Toolkit (http://nltk.org/, Bird et al. 2009). Code is in __init__.py, output is in out.txt. 

Stemmers and Lammatizers compress different word forms into a single word root. Oftentimes in information retrieval you are representing documents based on what words are within them, but something like stemming admits that different words can mean practically the same thing. For example, *walk* is, for many purposes, the same thing as *walking*, *walked*, and *walks*.

Stemmers reverse-engineer the form of a word based on patterns of the language, which can cause problems or inconsistencies. For example, irregular verbs or other atypical patterns can cause trouble for stemmers: while a stemmer may conflate *walked* with *walk* it won't do the same with *went* to *go*. 

Lemmatizers have the same purpose as stemmers, but they achieve it through a morphological analysis of the text. As seen in the output of this example script, they tend to be more successful, especially with nouns. 

Still, stemming tends to be a fairly low risk step in cleaning or analysing data, combining the probabilities of similar words without too much possibility for damage. (Although Singal (2001) has a good point that running into the occasional stemming failure is very annoying for users.

---
Bird, Steven, Ewan Klein, and Edward Loper. 2009. Natural Language Processing with Python. O’Reilly Media, Inc.
Paice, Chris D. 1990. “‘Another Stemmer.’” In , 24.3:56–61.
Porter, M. F. 1980. “An Algorithm for Suffix Stripping.” Program: Electronic Library and Information Systems 40 (3): 211–218. doi:10.1108/00330330610681286.
 ———. 2001. Snowball: A Language for Stemming Algorithms. http://snowball.tartarus.org/texts/introduction.html.
Singhal, A. 2001. “Modern Information Retrieval: A Brief Overview.” IEEE Data Engineering Bulletin 24 (4): 35–43.
