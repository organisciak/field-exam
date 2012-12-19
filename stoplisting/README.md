#Stoplisting
This is a basic example of using stoplists in Python with NLTK (http://nltk.org/, Bird et al. 2009). 

Stoplists are meant to reduce noise by removing terms that have little discriminating power. This intuition, that not all words are equally useful in understanding a document, underlies many effective techniques in both text analysis and retrieval. With stoplists, words with low discrimination power are chosen a priori, possibly manually, and usually using commonality in the language as the proxy for discriminatory power. Since stopwords tend to have high prior probabilities, their removal returns probability mass to other terms.

Consider the comparison between two inaugural speeches in the output of the accompanying script (output seen below). If you are looking at the most common words, you don't see much difference between George Bush and Barack Obama; instead you see linguistic noise like *and*, *of*, and, *the*. Not all words are uniformly interesting to use, and looking at the most common words, we intuitely ignore this noise.

````
NO STOPLIST
OBAMA/2009	the and of to our we that a is in this for us are not but can it on they will have has who with be 's as nation or those you their america new so these all because been
BUSH/2001	and of the our we a to in is not will are that it this but for america by i nation story us with 's citizens do at can country every has its must no all an as be common

STOPLISTED
OBAMA/2009	us 's nation america new every must let people world common less work day generation know spirit time today crisis god greater long meet men power seek whether women across care carried children come economy end father force founding future
BUSH/2001	america nation story us 's citizens country every must common courage know many never new president americans best beyond children justice live power promise public sometimes time work yet affirm american called civility commitment compassion country. deep defend duty faith
````

A stoplist lets us outright remove such 'boring' words. In the stoplisted outright, it is much easier to get a sense of the similarities and differences between the two speeches.

The primary deficiency of stoplists is that they approximate information that should be inherent in the corpus. If the approximate heuristic for a stoplist is how commonly it occurs in the language or the corpus, then the same effect can be achieved in a more scalable way with corpus based term weighting, such as Inverse Document Frequency (IDF). Different corpora have different properties, and an automated method can represent the low discriminating terms better than a general stoplist and more efficiently than a custom stoplist. 

However, stopword lists are customizable and easy to use. A music specific stoplist be customized to keep occurrances of *Who* or *Yes*, for example. For the same reason, though, stopword list building is also an uneven process: it is difficult to be comprehensive without automation, yet – since stoplists outright remove rather than weight terms – it is difficult to be non-destructive without manual pruning. Many approaches will be biased by the decisions of the stoplist—Is the list specific to this corpus? What was incorrectly missed, and what what incorrectly added? At what point should a stoplist end? 

Stoplisting is an easy approach when the document being analyzed is not part of a larger corpus, or from a corpus of an insignificant size where corpus derived techniques are unfeasible. Then, general stoplists or manually crafted ones can remove noise in the absence of other effective approaches. It is also better suited for some tasks than others. For example, in stylistics the relative frequency of the 'boring' words seen in stoplists may hold indicators of an author's writing fingerprint.

----
Bird, Steven, Ewan Klein, and Edward Loper. 2009. Natural Language Processing with Python. O’Reilly Media, Inc.
