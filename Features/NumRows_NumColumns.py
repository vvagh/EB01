import json
import csv
from itertools import zip_longest

sourceFile = open('Corpus/query_1.json', 'r')
json_data = json.load(sourceFile)

# number of data rows
tR_0370 = json_data["table-0370-614"]["numDataRows"]
# number of columns
tC_0370 = json_data["table-0370-614"]["numCols"]

# Counts number of null cells in Data portions of table
counting = []
for entry in json_data["table-0370-614"]["data"]:
    counting.append(entry.count(""))
    # count = entry.count("")
    sum_result = sum(counting)
print(sum_result)

with open('Features.csv', 'w', encoding="ISO-8859-1", newline='') as myFile:
    # writer for csv file
    wr = csv.writer(myFile)
    # creating the headings for csv file
    wr.writerow(("query_id", "query", "table_id", "row", "col", "nul", "in_link", "out_link", "pgCount", "tImp", "tPF",
                 "leftColhits", "secColHits", "bodyHits", "PMI", "qInPgTitle", "qInTableTitle", "yRank", "csr_score",
                 "idf"))

    query_id = ['1'] * 20
    query = ['world interest rates table'] * 20
    table_id = ["table-0370-614"]
    numRows = [tR_0370]
    numCols = [tC_0370]
    nullCells = [sum_results]
    d = [query_id, query, table_id, numRows, numCols, nullCells]
    exported_data = zip_longest(*d, fillvalue='')
    wr.writerows(exported_data)
myFile.close()
