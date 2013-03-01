'''
@author Peter Organisciak

Using Google N-Gram Data, classify a text input based on the most likely year
of the text.
'''
from __future__ import unicode_literals
import os
import logging
from ngramtools import nGramReader
from sqlalchemy import (create_engine, Table, Column, Integer,
                        Unicode, MetaData, select)


def create_table(c, schema, name="ngrams"):
    # Create a table based on a provided scheme
    pass

if __name__ == '__main__':
    # Load logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                        level=logging.INFO)

    query = "this is a test"
    filepath = "../ngrams/year/"
    db = "onemillion.db"
    MAX_BUFFER = 500000
    schema = [("text", "term"), ("int", "year"),
              ("int", "match_count"), ("int", "page_count"),
              ("int", "volume_count")]
   # Limiting length to 20 characters, the length of
   #'uncharacteristically' (one of the longest common words:
   # http://en.wikipedia.org/wiki/Longest_word_in_English )
   # The limit doesn't have any notable effect on filesize.
    char_limit = 20

    # Determine if filepath is a single file, or directory of files
    if os.path.isfile(filepath):
        files = [filepath]
    else:
        files = os.listdir(filepath)
        files = [os.path.join(filepath, f) for f in files]
        files = [f for f in files if f[-3:] == '.gz']
        files = [f for f in files if os.path.isfile(f)]

    #Initialize SQL Engine
    engine = create_engine('sqlite:///'+db, echo=True)

    #Create Table
    metadata = MetaData()
    ngrams = Table('ngrams', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('term', Unicode(length=char_limit)),
                   Column('year', Integer),
                   Column('match_count', Integer),
                   Column('page_count', Integer),
                   Column('volume_count', Integer)
                   )
    metadata.create_all(engine)

    #Insert values
    conn = engine.connect()

    for f in files:
        logging.info("Starting processing of {0}".format(f))
        nreader = nGramReader(f, schema=[v for (k, v) in schema],
                              char_limit=char_limit)
        buffer = []
        for line in nreader.readlines():
            buffer += [line]
            if len(buffer) == MAX_BUFFER:
        #        # Dump buffer
                logging.info("dumping buffer")
                conn.execute(ngrams.insert(), buffer)
                buffer = []
        # Save the rest of the buffer
        conn.execute(ngrams.insert(), buffer)

    logging.info("Done Indexing")

    #Read output
    logging.info("Testing with Query 'Peter'")
    s = select([ngrams], ngrams.c.term == 'Peter')
    print s
    result = conn.execute(s)

    for row in result:
        print row
