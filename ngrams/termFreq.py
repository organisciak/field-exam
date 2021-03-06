'''
Python class / command-line tool
Created on Nov 10, 2012

@author: Peter Organisciak

Lookup frequency data in Google N-Grams data. Includes a class for individual lookups,
    a class for multiple lookups, and a command-line interface.
    
Requires zgrep on the OS (included in Mac OS and Linux).

###COMMAND-LINE USAGE###
usage: termFreq.py [-h] [--split_alpha ALPHA_SPLIT] [--split_year YEAR_SPLIT]
                   [--year YEAR] [--count_regex COUNT_REGEX] [--tally TALLY]
                   
###CLASS USAGE###
Instantiate the googleLockup class with :
    g = googleLookup(infile[, split_alpha=False, split_year=False])
    PARAMETERS
        infile: the directory where the gz files are kept or, if there is only one file,
                the path to that file.
        split_year: whether the files are split by their year. e.g. infile/year.gz
        split_alpha: whether the files are split by the first character of the alphabet. e.g.
                infile/A.gz (if split_year is False) or infile/A/YEAR.gz
                
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
    
EXAMPLES
    g = googleLookup("year", split_year=True) 
    #print g.query("test", tally=False)              # Error, need year
    print g.query("test", year=1990, tally=False)
    g = googleLookup("year/1990.gz", split_year=False)
    print g.query("test", tally=True, count_regex="\d{5,10}")
    print g
    print g.get_last()
    
'''
import os
import subprocess
import csv

class googleLookup(object):
    '''
    Return the collection frequencies for a term in a given year.
    
    The query is case insensitive, so 'CAT' and 'cat' are added together.
    
    For performance, zgrep is used. As a result, on *nix systems are supported.
    '''

    def __init__(self, infile, split_alpha=False, split_year=False):
        '''
        Constructor
        '''
        self.input = os.path.join(os.getcwd(), infile) #Either the gz file being queried or the top level folder
        
        #Structure of archives. If split_alpha and split_year are off, it searches a file specified in self.inpit.
        #If split_year is one, it searches in YEAR.gz, within either self.input/ (if split_alpha is off) or self.input/X/
        self.split_alpha = split_alpha  #Whether the archives are split by alphabet.
        self.split_year = split_year    #Whether the archives are split by year
    
    def _path(self, q, year=None):
        if self.split_alpha and self.split_year:
            # e.g. input/q/1990.gz
            return os.path.join(self.input, q[0], str(year)+".gz")
        elif self.split_alpha and not self.split_year:
            # e.g. input/q.gz
            return os.path.join(self.input, q[0]+".gz")
        elif not self.split_alpha and self.split_year:
            # e.g. input/1990.gz
            return os.path.join(self.input, str(year)+".gz")
        elif not self.split_alpha and not self.split_year:
            # e.g. input.gz // Assumes that a filename was given for input
            return self.input
            
    def _lookup(self, q, year=None, count_regex=None, count_POS=False):
        if q != "[^\s:]*?":
            q = q.translate(None,'''.'"()?[]{}+''')
        if q is not None:
            regex = '^'+q+("(_.*?)" if count_POS else "")+'\t' #Note that count POS will double count
        else:
            regex = '^.*?\t'
        if year is not None:
            regex = regex + str(year) + "\t"
        else:
            regex = regex + "\d{4}\t"
        if count_regex is not None:
            regex = regex + count_regex
            
        path = self._path(q, year)
        
        p = subprocess.Popen(["zgrep", "-P", "-i", regex, path], stdout=subprocess.PIPE)
        out = p.communicate()[0]
        
        if out == "" or out is None:
            return None
        else:
            return out
    
    def _count_results(self, out, q="NONE", year="NONE"):
        out = out.strip().split("\n")
        freqs = dict(term=q, year=year, freq=0, volume_freq=0, lines=0)
        reader = csv.reader(out, dialect='excel-tab', skipinitialspace=True)
        for r in reader:
            freqs["lines"] += 1     #Count of case-insensitive lines found
            freqs["freq"] += int(r[2])
            freqs["volume_freq"] += int(r[3])
        return freqs
    
    def query(self, q, year=None, count_regex=None, tally = True):
        if self.split_year and year is None:
            raise TypeError('If split_year is on, a year is needed.')
        out = self._lookup(q, year, count_regex)
        self._last = {"q":q, "year":year, "count_regex": count_regex, "out":out}
        if out == "" or out is None:
            return None
        elif tally:  
            return self._count_results(out, q=q, year=year)
        else:
            return out   
    
    def get_last(self, tally = True):
        last = self._last
        if tally:
            return self._count_results(last["out"], last["q"], last["year"])
        else:
            return last["out"]
    
    def __repr__(self):
        return "<googleLookup %s>" % self.input

class multipleLookup(googleLookup):
    '''
    Same as googleLookup, but takes a list of queries or years.
    '''
    def query(self, queries, years=None, count_regex=None, tally = True):
        if self.split_year and years is None:
            raise TypeError('If split_year is on, a year is needed.')
        
        out = ""
        if queries is None:
            queries = ["[^\s:]*?"]
        
        if years is None:
            for q in queries:
                new_out = self._lookup(q, None, count_regex)
                if new_out is not None:
                    out = out + new_out
        elif years is not None:
            for q in queries:
                for year in years:  
                    new_out = self._lookup(q, year, count_regex)
                    if new_out is not None:
                        out = out + new_out
        self._last = {"q":q, 
                      "year":year, 
                      "count_regex": count_regex, 
                      "out":out}
        if out == "" or out is None:
            return None
        elif tally:  
            return self._count_results(out, 
                                       q="%s...%s" % (queries[0], queries[-1]) if queries is not None and queries != ["[^\s:]*?"] else "NONE", 
                                       year="%s...%s" % (years[0], years[-1]) if years is not None  and queries != ["[^\s:]*?"] else "NONE"
                                       )
        else:
            return out 
    
def total_freqs(infile):
    total_counts = open(infile, "r").read()
    return dict([(b.split("\t")[0], b.split("\t")[1:4]) for b in total_counts.splitlines()])

if __name__ == '__main__':  
    #m = multipleLookup("year", split_year=True)
    #print m.query(None, range(1790,2001, 10), count_regex="\d{4,10}", tally=False)
    
    ## This class can be run directly from the command-line
    import argparse
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(dest="infile",   help="directory of gz files, or path to single file")
    parser.add_argument(dest="query", help="term to search for")
    parser.add_argument("-sa", "--split_alpha", dest="split_alpha", help="whether files are split by the first character of a term", action='store_true')
    parser.add_argument("-sy", "--split_year", dest="split_year", help="whether files are split by the year", action='store_true')
    parser.add_argument("-y", "--year", dest="year", type=int, default=None, help="year to query")
    parser.add_argument("-re", "--count_regex", dest="count_regex", type=str, default=None, help="regex on the count field")
    parser.add_argument("-t", "--tally", dest="tally", type=bool, default=True, help="whether to add up frequencies")

    args = parser.parse_args()
    
    g = googleLookup(args.infile, split_alpha=args.split_alpha, split_year=args.split_year) 
    print g.query(args.query, year=args.year, tally=args.tally, count_regex=args.count_regex)
