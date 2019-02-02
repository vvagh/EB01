import json
import csv
from itertools import zip_longest
import itertools
import NumRows_NumColumns
import NullCells
import QT_ID
import numpy as np

with open('Features.csv', 'w', encoding="ISO-8859-1", newline='') as myFile:
    # writer for csv file
    wr = csv.writer(myFile)
    # creating the headings for csv file
    wr.writerow(("query_id", "query", "table_id", "rows", "#columns", "nullCells"))

    i = (range(1, 61))
    query_id = list(itertools.chain.from_iterable(itertools.repeat(x, 20) for x in i))
    query = np.repeat(QT_ID.query_list, 20)
    table_id = QT_ID.tableId
    numRows = NumRows_NumColumns.rows
    numCols = NumRows_NumColumns.columns
    nullCount = NullCells.null_cells
    d = [query_id, query, table_id, numRows, numCols, nullCount]
    exported_data = zip_longest(*d, fillvalue='')
    wr.writerows(exported_data)
myFile.close()
