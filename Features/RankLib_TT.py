import QT_ID
import NumRows_NumColumns
import NullCells
import featureCSV

targetList = QT_ID.qrel
qID = featureCSV.query_id
numRowsList = NumRows_NumColumns.rows
numColList = NumRows_NumColumns.columns
nullCellList = NullCells.null_cells

file = open("train.txt", "w")
for index in range(len(numColList)):
    file.write("qid:" + str(qID[index]) + " " + "1:" + str(numRowsList[index]) + " " + "2:" + str(numColList[index]) + " " + "3:"
                + str(nullCellList[index]) + "\n")
file.close()
