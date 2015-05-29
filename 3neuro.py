import csv, urllib2, os, operator, string, itertools, re, json
from pprint import pprint as pp
from nltk.corpus import stopwords
from collections import Counter

def format_brain(fname):
    my_file = open(fname, "r")
    read_file = my_file.read().lower()
    my_file.close()
    return list(set(read_file.split("\n")))

def format_scale(fname):
    my_file = open(fname, "r")
    read_file = my_file.read().lower()
    my_file.close()
    # lines = list(set(my_file.read().lower().split("\r")))
    # r"(\w)(\w+)(\w)"
    # subbed_file = [ re.sub(r'[^a-zA-Z0-9_]', ' ', line) for line in read_file.split("\r") if line]
    subbed_file = [ re.sub(r'\W+', ' ', line) for line in read_file.split("\r") if line]
    return list(set(subbed_file))
    # return [line for line in lines]

def read_data(fname):
    my_file = open(fname, "r")
    read_file = my_file.read()
    lines = read_file.split("\n\n\n")
    my_file.close()

    bterms = set(format_brain("mesh_brain3.txt"))
    # sterms = set(format_scale("mmy_index.txt"))
    sterms = set(format_scale("psych_scales.txt"))
    snbterms = set(format_brain("mesh_brain3.txt") + format_scale("mmy_index.txt"))
    stop = stopwords.words('english')
    lines2 = ["\n\n".join([l for l in line.split("\n\n")]) for line in lines]
    formatted = [" ".join([l for l in re.sub(r'\W+', ' ', line).split() if len(l) > 2]) for line in lines2]
    my_hash = {}
    for index, abstract in enumerate(formatted):
      # if index == 100:
      #   break
      for sterm in sterms:
        if sterm in abstract:
          bees = [bterm for bterm in bterms if bterm in abstract]
          if bees:
            for bee in bees:
              combined = sterm + " | " + bee
              if combined in my_hash:
                my_hash[combined] += 1
              else:
                my_hash[combined] = 1
          # if sterm in my_hash:
          #   my_hash[sterm] = my_hash[sterm] + [bterm for bterm in bterms if bterm in abstract]
          # else:
          #   my_hash[sterm] = [bterm for bterm in bterms if bterm in abstract]

    with open('result2.json', 'w') as fp:
        json.dump(my_hash, fp)

    return my_hash
    # with open("nw.csv", "wb") as neuro_words:
    #     writer = csv.writer(neuro_words)
    #     header = ['title', 'content', 'pmid', 'scales', 'brain regions']
    #     writer.writerow(header)
    #     for index, row in enumerate(form2):
    #         writer.writerow(row)
    # return "Write complete"




pp(read_data("pubmed_result.txt"))
# pp(format_scale("psych_scales.txt")[:100])
# pp(read_data("pubmedsmall.txt"))
# pp(len(read_data("pubmedsmall.txt")))
