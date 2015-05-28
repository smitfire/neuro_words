import csv, urllib2, os, operator, string, itertools
from pprint import pprint as pp
from nltk.corpus import stopwords

cached_stops = stopwords.words("english")

def read_data(fname):
    my_file = open(fname, "r")
    lines = my_file.read().translate(string.maketrans("",""), string.punctuation).lower().split("\n\n\n")
    my_file.close()
    bterms = format_brain("mesh_brain3.txt")
    sterms = format_scale2("mmy_index.txt")
    formatted = [[l.replace("\n", " ") for l in line.split("\n\n")[1::]] for line in lines]
    form2 = [list(operator.itemgetter(0, 3, -1)(line)) for line in formatted if len(line) > 3]
    with open("nw2.csv", "wb") as neuro_words:
        writer = csv.writer(neuro_words)
        header = ['title', 'content', 'pmid', 'scales', 'bregions']
        writer.writerow(header)
        for index, row in enumerate(form2):
            # if index == 500:
            #     break
            bregions = ' | '.join(list(set([bterm for bterm in bterms if bterm in row[1]])))
            scales = ' | '.join(list(set([sterm for sterm in sterms if sterm in row[1]])))
            print "====================BRAIN REGIONS==============================="
            pp(bregions)
            print "=====================PSYCH SCALES=============================="
            pp(scales)
            print "=====================  END  ==============================\n\n"
            if len(scales) > 1 and len(bregions) > 1:
                row = row + [scales] + [bregions]
                writer.writerow(row)
    return "Write complete"

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
    return list(set(read_file.translate(string.maketrans("",""), string.punctuation).lower().split("\n")))

def format_scale(fname):
    my_file = open(fname, "r")
    read_file = list(set(my_file.read().translate(string.maketrans("",""), string.punctuation).lower().split("\r")))
    my_file.close()
    key_words = ' '.join([word for word in read_file.split(" ") if word not in cached_stops])
    lines = list(set(key_words.split("\r")))
    # " ".join(filter(lambda word: word not in stop_words, line.split()))
    # lines2 = ' '.join([word for word in text.split() if word not in cached_stops])
    # scales_only = [line.split(',')[0] for line in lines if line.split(',')[0].split(' ') not in cached_stops]
    # [ " ".join(filter(lambda word: word not in stop_words, line.split())) for line in scales_only ]
    return [line.split(',')[0] for line in lines]

def format_scale2(fname):
    my_file = open(fname, "r")
    lines = list(set(my_file.read().lower().split("\r")))
    my_file.close()
    return [line.split(',')[0] for line in lines]


def format_scale3(fname):
    my_file = open(fname, "r")
    lines = list(set(new_lines.translate(string.maketrans("",""), string.punctuation).lower().split("\r")))
    # lines = list(set(my_file.read().lower().split("\r")))
    my_file.close()
    new_lines = ' '.join([line.split(',')[0] for line in lines])

print read_data("pubmed_result.txt")
# pp(format_brain("mesh_brain3.txt")[0:20])
# pp(format_scale("mmy_index.txt")[0:10])
# print "="*100
# pp(format_scale3("mmy_index.txt")[0:10])
# pp(len(format_scale("mmy_index.txt")))

