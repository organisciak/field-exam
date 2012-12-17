# Peter Organisciak
#
#Plyr library used for some examples, not necessary
library(plyr)

## Term frequency sample
# Figure 6.9 from Manning et al. 2008
tf <- data.frame(row.names=c("car", "auto", "insurance", "best"), doc1=c(27,3,0,14), doc2=c(4,33,33,0), doc3=c(24,0,29,17))

## Document frequency from Reuters collection.
# Figure 6.8 from Manning et al. 2008
df <- data.frame(row.names=c("car", "auto", "insurance", "best"), df=c(18165,6723,19241,25235))

# Size of Reuters collection
N <- 806791

# Add an idf column
df$idf <- log10(N/df$df)

#Make a tf*idf dataframe
tfidf <- tf*df$idf

#Calculate a basic document score by summing tf*idf scores (needs plyr)
doc.scores <- colwise(sum)(tfidf)

## Vector Space Model
#Make columns globally available (e.g. call with col rather than df$col)
attach(tf)

#Calculate dot product (sum of all vector products) between two documents 
dot.product <- function(x,y) sum(x*y)

#Example
dot.product(doc1, doc2)

#Calculate the Euclidean length for a document
euclid <- function(x) sqrt(sum(x^2))
#Example
euclid(doc1)

#Calculate Euclidean lengths for all columns (required plyr)
euclidean.lengths <- colwise(euclid)(tf)

#Normalize all term-frequencies by euclidian length
# Figure 6.11 from Manning et al. 2008
tf.euclid <- tf/c(euclidean.lengths)

# Two ways to get the cosine similarity:
#	Equation 6.10 from Manning et al. 2008 
dot.product(doc1, doc2)/(euclidean.lengths$doc1*euclidean.lengths$doc2)
# Or, since we have the normalized vector calculated, the simplified equation:
#	Equation 6.11 from Manning et al. 2008 
dot.product(tf.euclid$doc1, tf.euclid$doc2)
