import sys, Quandl,nltk, csv, urllib2, codecs, simplejson, decimal, string, json, re
import numpy as np
import pandas as pd
from pprint import pprint as pp
from operator import itemgetter
from random import randint


def split_keys(fname):
    # res, bs, scl = {"nodes": [], "links":[]}, [], []
    res, bs, scl = {"nodes": [], "bregions": [], "links":[] }, [], []
    with open(fname) as data_file:
        data = json.load(data_file)
        for key, val in data.items():
            if val > 50:
                bs.append(key.split(" | ")[1])
                scl.append(key.split(" | ")[0])
            # arr = key.split(" | ")+[randint(1,10)]
            # res["nodes"].append({"name": key, "group": randint(1,10) })

    comb = list(set(bs)) + list(set(scl))
    bs = list(set(bs))
    scl = list(set(scl))
    # c2 = []
    # for key, val in data.items():
    #     if key.split(" | ")[0] in comb:
    #         c2.append(key.split(" | ")[0])
    #         if key.split(" | ")[0] not in res["nodes"]:
    #             res["nodes"].append({"name": key.split(" | ")[0], "group": randint(1, 10)})
    #     if key.split(" | ")[1] in comb:
    #         c2.append(key.split(" | ")[1])
    #         if key.split(" | ")[1] not in res["bregions"]:
    #             res["bregions"].append({"name": key.split(" | ")[1], "group": randint(1, 10)})

    # c2 = list(set(c2))

    # for key, val in data.items():
    #     if key.split(" | ")[0] in scl:
    #         res["links"].append( {"source": scl.index(key.split(" | ")[0]), "target": bs.index(key.split(" | ")[1]), "value": val } )
    #     if key.split(" | ")[1] in bs:
    #         res["links"].append( {"source": bs.index(key.split(" | ")[1]), "target": scl.index(key.split(" | ")[0]), "value": val } )
    sc2 = []
    bs2 = []
    for key, val in data.items():
        if key.split(" | ")[0] in scl and key.split(" | ")[1] in bs:
            res["links"].append( {"source": scl.index(key.split(" | ")[0]), "target": bs.index(key.split(" | ")[1]), "value": val } )

    for item in scl:
        res["nodes"].append({"name": item, "group": randint(1,10) })

    for item in bs:
        res["bregions"].append({"name": item, "group": randint(1,10) })

    with open('names7.json', 'w') as fp:
        json.dump(res, fp)

    # for val in res["links"]:
    #     if val["source"] > 100:
    #         print val
    # print res
    print len(res["nodes"]) == len(scl), len(res["bregions"]) == len(bs), len(res["links"])
    print len(res["nodes"]), len(res["bregions"]), len(res["links"])


def assign_source():
    links = []
    with open("result.json") as data_file:
        data = json.load(data_file)
    # return data
    sep = split_keys("result3.json")
    # for index, val in sep["nodes"]:

    # for index, key, val in enumerate(data.items()):
    #     if key.split(" | ")[0] in sep["nodes"]:
    #         links.append( {"source": sep["nodes"][key.split(" | ")[0]], "target": , "value": } )
    #     if key.split(" | ")[1] in sep["nodes"]:
            # links.append( {"source":  } )

    # for index, item in enumerate(sep["nodes"]):


def get_keys(fname):
    with open(fname) as data_file:
        data = json.load(data_file)
        for val in data:
            print val

# {"source":55,"target":11,"value":19}

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


def json_keys(fname):
    with open(fname) as data_file:
        data = json.load(data_file)
    l = []
    for item in data['links']:
        if item["source"] > 40 or item["target"] > 40:
            l.append(item)
    l.sort()
    return l



pp(split_keys("result.json"))
# split_keys("result3.json")
# pp(get_keys("result3.json"))
# pp(json_keys("names6.json"))
# json_keys("mis.json")
# pp(len(format_brain("mesh_brain4.txt")))
# pp(len(format_scale("psych_scales.txt")))