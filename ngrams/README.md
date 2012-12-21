ngam.sh parse the Google English One Million ngram data into year by year gz files, making it easier an more efficient to do lookups in them.

Download the data here:
http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

 Usage:
 ./ngram.sh IN START END OUT
       IN - folder where the zip files are kept. This script reads all of them
       START - First year to process
       END - Last year to process
       OUT - Output folder.

 e.g.
       ./ngram.sh ~/Downloads 1789 2009 year

To run the script, you point it at a folder where the 1-gram zip files are. Note that the script assumes that there are no other .zip files in the input folder.
You also specify the folder where the final gzips will go and the start and end dates to create archives for. The output folder needs to already exist.

Output
The output of the files will be a series of gz files in the output folder, named by year: e.g. 1990.gz.

You don't need to decompress gz files to search within them. For example, to find the frequencies for "church" in 1990:

 zgrep -P "^church\t" 1990.gz 

Additional Notes
Since the 1-grams of the English One Million corpus are .zip and the 2-5 grams are gz, this script will not work on those. 
The script creates in intermediary unzipped file, for performance. Keeping it in memory was too slow and piping it meant unzipping files more than one. 
