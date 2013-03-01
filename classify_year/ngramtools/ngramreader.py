'''
A class for reading nGram export files.

Download data at
http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

Created February 28, 2013
@author: Peter Organisciak
'''
import gzip


class nGramReader(object):
    '''
    Class for representing a Google NGrame input file
    Defaults to Google One Million schema.
    '''

    def __init__(self, path, grams=None, bytes=0,
                 schema=["term", "year", "match_count",
                         "page_count", "volume_count"],
                 sep="\t", char_limit=None):
        self.schema = schema
        self.file = gzip.GzipFile(filename=path)
        self.loc = bytes
        self.sep = sep
        self.char_limit = char_limit

        if self.loc > 0:
            self.file.seek(self.loc)
        if grams is None:
            # Analyze first line of file
            self.grams = 1
        else:
            self.grams = grams
        self.lines = 0

    def next_line(self):
        line = self.file.readline()
        # Encode bytestring as UTF-8 and convert to unicode
        # And since every few months I forget, here's a reminder on
        # how unicode works: http://stackoverflow.com/a/370199/233577
        line = line.decode("ISO-8859-1")
        line = unicode(line)
        # If blank, assume EOF
        # Actual blank lines would have a trailing linebreak
        if line == "":
            return ""
        return self._parse_line(line)

    def _parse_line(self, line):
        # Remove trailing line break
        line = line[0:-1]
        # Name values
        values = line.split(self.sep)
        if self.char_limit is not None:
            values = [value[:self.char_limit] for value in values]
        return dict(
            [(self.schema[i], val) for i, val in enumerate(values)]
        )

    def readlines(self):
        while True:
            line = self.next_line()
            if line == "":
                break
            yield line
        ## Slower version: reads full file into memory
        #for line in self.file.readlines():
        #    yield self._parse_line(line)
