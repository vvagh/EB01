import json

sourceFile = open('corpus.json', 'r')
json_data = json.load(sourceFile)


fname = 'STR.txt'

with open(fname) as f:
    content = f.readlines()
rows = []
columns = []
for line in content:
    sline = line.split()
    tid = sline[2]
    # number of data rows
    tR = json_data[tid]["numDataRows"]
    # number of data columns
    tC = json_data[tid]["numCols"]
    rows.append(tR)
    columns.append(tC)
