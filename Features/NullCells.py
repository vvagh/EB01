import json

sourceFile = open('corpus.json', 'r')
json_data = json.load(sourceFile)

fname = 'STR.txt'
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
        counting.append(entry.count(""))
        # count = entry.count("")
        sum_result = sum(counting)
        sumResults = sum_result
    null_cells.append(sum_result)




