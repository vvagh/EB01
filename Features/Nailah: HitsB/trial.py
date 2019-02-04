import json
from collections import Counter
import re
import string
import codecs
import itertools


sourceFile = open('corpus.json', 'r')
json_data = json.load(sourceFile)

fname = 'STR.txt'

with open(fname) as f:
        content = f.readlines()
query_words = []
for lines in content:
    sline = lines.split()
    tid = sline[2]
    dataList = []

    j = json_data[tid]["data"]
    print(tid)
    sumTable = []
    for entry in range(len(j)):
        data = j[entry]
        data = [p.replace('_', " ") for p in data]
        print(data)
        sumTotal = []
        sum2 = []
        for word in range(len(data)):
            di = data[word]
            String = "World interest rates"
            query = String.split()
            # print(query)
            summation = []
            results = {}
            for i in query:
                results[i] = di.count(i)
            sums = (sum(results.values()))
            summation = sums
            sumTotal.append(summation)
            sum2 = sum(sumTotal)
        print(sum2)
