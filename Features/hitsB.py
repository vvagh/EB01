# This file represents the #hitsB which is the total query term frequency in the table body
# this json file demonstrates a test run and the output per work and character
import json
import QT_ID


sourceFile = open('corpus.json', 'r')
jsonData = json.load(sourceFile)
json_data = jsonData.replace("_", " ")

fname = 'STR.txt'

with open(fname) as f:
        content = f.readlines()
query_words = []
for line in content:
        sline = line.split()
        tid = sline[2]

        # Counts number of null cells in Data portions of table
        counting = []
        sumResults = []
        for entry in json_data[tid]["data"] or json_data[tid]["pgTitle"] or json_data[tid]["title"] or json_data[tid]["caption"] or json_data[tid]["secondTitle"]:
            query = QT_ID.query_list[0].split(' ')
            # print(query[2])

            counting.append(entry.count("capita"))
            sum_result = sum(counting)
            sumResults = sum_result
        query_words.append(sum_result)
print(query_words)
