import csv, urllib2, os, operator, string, itertools, re, json
from pprint import pprint as pp
from nltk.corpus import stopwords
from collections import Counter


def freq_dic(fname):
    my_file = open(fname, "r")
    lines = my_file.read().translate(string.maketrans("",""), string.punctuation).lower().split("\n\n\n")
    my_file.close()
    bterms = format_brain("mesh_brain3.txt")
    sterms = format_scale2("mmy_index.txt")
    formatted = [[l.replace("\n", " ") for l in line.split("\n\n")[1::]] for line in lines]
    form2 = [list(operator.itemgetter(0, 3, -1)(line)) for line in formatted if len(line) > 3]

def format_brain(fname):
    my_file = open(fname, "r")
    read_file = my_file.read()
    my_file.close()
    return list(set(read_file.lower().split("\n")))

def format_scale(fname):
    my_file = open(fname, "r")
    lines = list(set(my_file.read().lower().split("\r")))
    my_file.close()
    return [line.split(',')[0] for line in lines]

def read_data(fname):
    my_file = open(fname, "r")
    read_file = my_file.read().lower()
    lines = read_file.split("\n\n\n")
    my_file.close()

    bterms = set(format_brain("mesh_brain3.txt"))
    sterms = set(format_scale("mmy_index.txt"))
    snbterms = set(format_brain("mesh_brain3.txt") + format_scale("mmy_index.txt"))
    stop = stopwords.words('english')

    formatted = [" ".join([l for l in re.sub(r'\W+', ' ', line).split() if len(l) > 5]) for line in lines]
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
# pp(read_data("pubmedsmall.txt"))
# pp(len(read_data("pubmedsmall.txt")))
