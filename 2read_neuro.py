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

# print read_data("pubmed_result.txt")
# pp(format_brain("mesh_brain3.txt")[0:20])
# pp(format_scale("mmy_index.txt")[0:10])
# print "="*100
# pp(format_scale3("mmy_index.txt")[0:10])
# pp(len(format_scale("mmy_index.txt")))

s = """BACKGROUND: Substance dependence and antisocial psychopathology, such as a
history of childhood conduct disorder (HCCD), are associated with impulsive or
disadvantageous decision making and reduced working memory capacity (WMC).
Reducing WMC via a working memory load increases disadvantageous decision making 
in healthy adults, but no previous studies have examined this effect in young
adults with substance dependence and HCCD.
METHOD: Young adults with substance dependence (SubDep; n=158, 71 female),
substance dependence and HCCD (SubDep+HCCD; n=72, 24 female), and control
participants (n=152, 84 female) completed a test of decision making (the Iowa
Gambling Task; IGT) with or without a concurrent working memory load intended to 
tax WMC. Outcomes were (i) net advantageous decisions on the IGT, and (ii)
preferences for infrequent- versus frequent-punishment decks.
RESULTS: SubDep+HCCD men made fewer advantageous decisions on the IGT than
control men without a load, but there were no group differences among women in
that condition. Load was associated with fewer advantageous decisions for
SubDep+HCCD women and control men, but not for men or women in the other groups. 
Participants showed greater preference for infrequent-punishment, advantageous
decks under load as well.
CONCLUSIONS: There are gender differences in the effects of substance dependence,
HCCD, and working memory load on decision making on the IGT. Decision making by
control men and SubDep+HCCD women suffered the most under load. Load increases
preferences for less-frequent punishments, similar to a delay discounting effect.
Future research should clarify the cognitive and neural mechanisms underlying
these effects."""
print len(s)