
# This file represents the #hitsB which is the total query term frequency in the table body
# this json file demonstrates a test run and the output per work and character
import json

sourceFile = open('/Users/fatimapeygumbari/EB01/Corpus_Data/corpus.json', 'r')
json_data = json.load(sourceFile)

fname = '/Users/fatimapeygumbari/EB01/Corpus_Data/STR.txt'

with open(fname) as f:
        content = f.readlines()
null_cells = []
for line in content:
        sline = line.split()
        tid = sline[2]

        # Counts number of null cells in Data portions of table
        counting = []
        sumResults = []
        for entry in json_data[tid]["data"]:
                counting.append(entry.count("World"))
                sum_result = sum(counting)
                sumResults = sum_result
        null_cells.append(sum_result)

print(null_cells)