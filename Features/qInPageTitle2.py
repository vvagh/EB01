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

k = 0
l = 0

for key, v in querydict.items():
    # print (key + " ")
    # print len(v['query'])
    # print(v['tableid'])
    # print(v['tableid'])
    count = 0
    for x in v['tableid']:
        titledata = json_data[x]["pgTitle"]
        tdSplit = titledata.split()
        # print ( x + " " + titledata)
        # print(tdSplit)
        k = 0
        l = 0

        while k < len(v['query']):
            l = 0
            while l < len(tdSplit):

                qr = v['query'][k]
                ptitle = tdSplit[l]

                # print ("  query" + key)

                searchObj = re.search(qr, ptitle, re.M | re.I)
                if searchObj:
                    count += 1
                    print(
                    "Query: " + key + " Table ID :" + x + " Matching query Word: ", searchObj.group() + " Count: ",
                    count/60.0)
                l += 1
                # print("query: " + key + "  Ratio: ", count / 60.0)

            k += 1

    # print("query: " + key + "  Ratio: ", count/60.0)
