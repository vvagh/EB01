import json
import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from collections import defaultdict
import re

porter = PorterStemmer()
lancaster = LancasterStemmer()

# Loading corpus data
corpusData = open('/Users/vruti/Documents/GitHub/EB01/Corpus_Data/corpus.json', 'r')
json_data = json.load(corpusData)

# loading queries files
fname = '/Users/vruti/Documents/GitHub/EB01/queries.txt'

with open(fname) as f:
    queriestxt = f.readlines()

# loading str file to get table id for query
fname1 = '/Users/vruti/Documents/GitHub/EB01/STR.txt'

with open(fname1) as f:
    strtxt = f.readlines()

# creating a dictionary to hold all the information
querydict = dict()
querynumber = 0

# First forloop to get queries from queries.txt
for line in queriestxt:
    sline = line.split()
    querynumber = sline[0]
    tid = sline[1:5]
    # print(tid)
    i = 0
    stem = ""
    # creating hierachy of dictionary
    querydict[querynumber] = {}
    # creating array for query to store individual stemmed words- easier for searching
    querydict[querynumber]['query'] = []

    # stemming words
    while i < len(tid):
        stem = porter.stem(tid[i])
        i += 1
        # adding to dictionary
        querydict[querynumber]['query'].append(stem)

    #     creating array for tabelid to store all 20 tableids from str.txt file to dictionary
    querydict[querynumber]['tableid'] = []
    for line1 in strtxt:
        dline = line1.split()
        tableid = dline[2]
        querynumfromstr = dline[0]

        # adding table ids to corresponding query
        if querynumfromstr == querynumber:
            querydict[querynumber]['tableid'].append(tableid)

# print querydict
# print("\n".join("{}\t{}".format(k, v) for k, v in querydict.items()))

#
# querydict = json.dumps(querydict)
# loaded_r = json.loads(querydict)
# type(querydict) #Output str
# type(loaded_r) #Output dict
#
# print(loaded_r)

# for a in json_data:
#   print(a,json_data[a])

# print (json_data['table-1488-888']['pgTitle'])

# k = 0
# l = 0
for key, v in querydict.items():
    count = 0
    # print (key + " ")
    # print(v['query'])
    # print(v['tableid'])
    k = 0
    l = 0
    for x in v['tableid']:
        # print ("  query" + key)
        # print(v['tableid'])
        # print(v['query'])
        titledata = json_data[x]["pgTitle"]
        tdSplit = titledata.split()
        # print(tdSplit)

        qr = v['query'][k]
        ptitle = tdSplit[l]

        qx = re.findall(qr, ptitle)
        count += 1
        # print(qx)

        searchObj = re.search(qr, ptitle, re.M | re.I)
        if searchObj:
            print ("  query" + key)
            print(x)
            print "search --> searchObj.group() : ", searchObj.group()
            count += 1
            print(x)
            print(count)
        else:
            print(qr)
            print "Nothing found!!"
            print(x)


        # if (v['query'][k]) == (tdSplit[l]):

        # print(v['query'][k])
        # print(tdSplit[l])
    k += 1
    l += 1

    # print(count)
    # Return a list containing every occurrence of "ai":

    # str = titledata
    # x = re.findall("v['query]", str)

# print(x)
# print(i)

# i = 0
#
# while i < len(v['query']):
#     querysearch = titledata.startswith(v['query'][i])
#     print(querysearch)
#     i += 1
#
# if querysearch != 0:
#     count = count + 1

# print(count)
# for tid in tableids:
#     tableids.get("pgTitle")
