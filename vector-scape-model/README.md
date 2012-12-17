#Vector Space Model
This is an R implementation of the vector space model examples in chapter 6 of Manning et al. 2008 (see online http://nlp.stanford.edu/IR-book/pdf/06vect.pdf).

The vector space model (Salton et al. 1975) is a classic information retrieval model the represents documents as vectors in large multi-dimensional planes.  Most basically, vectors represent words as features, with their occurrance count as the values. You can have other features, as well as ways to weigh the values, but consider this basic case for now.

To understand the vector space model, imagine a very simple set of documents, where all we look at is the occurrances of the words *car* and *safety*. If you counted up all these in three documents, you might find that D1=(1,3), Doc2=(4,2), and Doc3=(6,5). This is easy to imagine, because there are two dimensions. For example:

Car
 |          *
 |
 | *
 |      *
  _ _ _ _ _ _ Safety

(Note that these are vectors, not points, I wasn't going to try to draw ASCII lines).

With documents represented like this, we can measure similarity between the vectors. Essentially: which ones are closer together? If we increase the complexity to 3-dimensions (looking at three words) you can still visualize them, and the calculations stay the same. This keeps going into larger dimensions until you're representing each document as a vector of how many times each possible word occurs. Even though you can no longer visualize this, similarity measures still hold.

Since you can measure similarity between documents, the vector space model proves to be valuable for information retrieval. If a user submits a query, that query *can also be represented as a vector*, and documents can be returned based on how close they are to the query vector.

This script shows a simple case, where we're representing documents only by a few words. The vector values are represented by TFIDF scores (i.e a word's term frequency in the given document multiplied by the inverse count of that word in all the documents), the vector lengths are normalised, and a cosine similarity measure is used to calculate similarity. As noted above, I was merely representing in code the examples from Manning et al, so look there for more context.

----
Manning, Christopher D., Prabhakar Raghavan, and Hinrich Schütze. 2008. Introduction to Information Retrieval. Cambridge University Press. http://nlp.stanford.edu/IR-book/.
Rocchio, J. J. 1971. “Relevance Feedback in Information Retrieval.” http://www.citeulike.org/group/1710/article/919439.
Salton, G., A. Wong, and C. S. Yang. 1975. “A Vector Space Model for Automatic Indexing.” Commun. ACM 18 (11) (November): 613–620. doi:10.1145/361219.361220.
