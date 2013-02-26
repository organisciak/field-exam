#Google Books corpus-based term frequencies.
##Overview
The following scripts are included here:
 * [NGram.sh](#ngramsh) - Split Google's English One Million dataset into compressed year by year files, making lookups easy.
 * [ngrams/termFreq.py](#termfreqpy) - Look up the the number of occurrances of a term in ngram export data.

##NGram.sh
ngram.sh parses the Google English One Million ngram dataset into a more manageable collection of compressed gzip files, separated by year. 

This enables more efficient lookups against Google's large ngrams data. This is due to two reason: first, by having a large number of smaller files, looking up ngram data for a specific year doesn't need to process multiple gb of data. Secondly, by compressing the files with GZip, one can perform faster searches on Linux or Unix systems (including Mac OS) using zgrep.

Download the Google One Million NGram dataset for processing here:
http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

###Usage:
 ./ngram.sh IN START END OUT
       IN - folder where the zip files are kept. This script reads all of them
       START - First year to process
       END - Last year to process
       OUT - Output folder.

 e.g.
       ./ngram.sh ~/Downloads 1789 2009 year

To run the script, you point it at a folder where the 1-gram zip files are. Note that the script assumes that there are no other .zip files in the input folder.
You also specify the folder where the final gzips will go and the start and end dates to create archives for. The output folder needs to already exist.

###Output
The output of the files will be a series of gz files in the output folder, named by year: e.g. 1990.gz.

You don't need to decompress gz files to search within them. For example, to find the frequencies for "church" in 1990:

 zgrep -P "^church\t" 1990.gz 

###Additional Notes
Since the 1-grams of the English One Million corpus are .zip and the 2-5 grams are gz, this script will not work on those. 
The script creates in intermediary unzipped file, for performance. Keeping it in memory was too slow and piping it meant unzipping files more than one. 

##termFreq.py##
Lookup frequency data in Google N-Grams data. Includes a class for individual lookups, a class for multiple lookups, and a command-line interface.
    
Requires zgrep on the OS (included in Mac OS and Linux).

###COMMAND-LINE USAGE###
usage: termFreq.py [-h] [--alpha_split ALPHA_SPLIT] [--year_split YEAR_SPLIT]
                   [--year YEAR] [--count_regex COUNT_REGEX] [--tally TALLY]
                   
###CLASS USAGE###
Instantiate the googleLockup class with :
    g = googleLookup(infile[, alpha_split=False, year_split=False])
    PARAMETERS
        infile: the directory where the gz files are kept or, if there is only one file,
                the path to that file.
        year_split: whether the files are split by their year. e.g. infile/year.gz
        alpha_split: whether the files are split by the first character of the alphabet. e.g.
                infile/A.gz (if year_split is False) or infile/A/YEAR.gz
                
Lookup a query with:
    g.query(query, year=None, count_regex=None, tally = True)
    
        query: specifies the word(s) to find. If you provide None then all words 
                are returned.
        year: specifies what year should be queried. If no year is specified, all 
            years will be returned.
        count_regex: lets you specific a regex for the corpus frequency field
            (e.g. \d{5,13} to find 5-13 digit frequencies).
        tally: Whether frequencies are counted up, or whether the raw row matches 
            are returned.
    
####EXAMPLES
    g = googleLookup("year", year_split=True) 
    #print g.query("test", tally=False)              # Error, need year
    print g.query("test", year=1990, tally=False)
    g = googleLookup("year/1990.gz", year_split=False)
    print g.query("test", tally=True, count_regex="\d{5,10}")
    print g
    print g.get_last()

