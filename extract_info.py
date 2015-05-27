import sys
import csv, urllib2
import codecs
import numpy as np
from pprint import pprint as pp
import nltk
nltk.download()

our_file = sys.argv[1]

class PaperInfo(object):
    """docstring for PaperInfo"""
    def __init__(self, fname):
        self.paper_text   = open(fname, "r").read()
        self.meta_data    = self.paper_text.split("\n\n")[4].split("\n")
        self.dates        = self.paper_text.split("\n\n")[7]
        self.abstract        = self.paper_text.split("\n\n")[9]
        self.title        = self.meta_data[0]
        self.authors      = self.meta_data[1]
        self.universities = self.meta_data[2]


pinfo = PaperInfo(our_file)
# pp(pinfo.abstract)
