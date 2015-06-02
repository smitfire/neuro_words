#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, urllib2, os, operator, string, itertools, re, json, codecs, nltk
from pprint import pprint as pp
from nltk.corpus import stopwords
from collections import Counter
from nltk.tag import pos_tag

def format_brain(fname):
    my_file = open(fname, "r")
    read_file = my_file.read().lower()
    my_file.close()
    return list(set([line.strip() for line in read_file.split("\n") if line]))

def format_scale(fname):
    my_file = codecs.open(fname, "r")
    read_file = my_file.read().lower()
    my_file.close()
    subbed_file = list(set([ "".join([l for l in re.sub(r"\W+(?<![\-.])", " ", line)]).strip() for line in read_file.split("\r") if line]))
    return [line for line in subbed_file if line]

def read_data(fname):
    my_file = open(fname, "r")
    lines = my_file.read().lower().split("\n\n\n")
    my_file.close()

    # stops = stopwords.words('english') + [string.punctuation.replace("-","")]
    bterms = set(format_brain("mesh_brain4.txt"))
    sterms = set(format_scale("psych_scales.txt"))

    print "TERMS ARE LOADED UP!!"

    lines2 = [re.sub(r"\W+(?<![\-.])", " ", line.decode('utf-8').split("\n\n")[4]) for line in lines if len(line.decode('utf-8').split("\n\n")[4])>500 ]

    print "SHIT HAS BEEN FORMATTED AND READY TO LOOP!!"

    my_hash = {}
    links = []
    for index, abstract in enumerate(lines2):
      print str(index)
      print "="*100
      for stindex, sterm in enumerate(sterms):
        if sterm in abstract:
          bees = [bterm for bterm in bterms if bterm in abstract]
          if bees:
            for bee in bees:
              links.append({"source":stindex,"target":11,"value":19})
              combined = sterm + " | " + bee
              if combined in my_hash:
                my_hash[combined] += 1
              else:
                my_hash[combined] = 1

    with open('result.json', 'w') as fp:
        json.dump(my_hash, fp)

    return my_hash


# scales_t = format_scale("psych_scales.txt")
# scales_t.sort()

# pp(read_data("pubmedsmall.txt"))
# print read_data("pubmedsmall.txt")
# pp(len(read_data("pubmedsmall.txt")))

# read_data("pubmed_result.txt")
pp(format_brain("mesh_brain4.txt")[:50])
