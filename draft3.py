import glob
import math

line = ''
s = set()

path = '/Users/naila/Desktop/WP_tables/tables_redi2_1/re_tables-0001.json'
files = glob.glob(path)
for name in files:
    tfile = open(name, "r")
    line = tfile.read()
    tfile.close()
    s = s.union(set(line.split(' ')))
    #s = sorted(s)

i = 0
ct = 0
tf_line = ''
doc_counts = []
for term in s:
    doc_counts.append(0)

    for fdoc in files:

        doc = open(fdoc)
        line = doc.read()
        doc.close()
        ct = line.count(str(term))
        tf_line += str(ct)+','
        if ct > 0:
            doc_counts[i] += 1
    i += 1
    tf_line = tf_line.strip()+'\n'
idf = []
weights = []
total_docs = len(files)

i = 0
for doc_count in doc_counts:
    idf.append(math.log(total_docs/doc_count))
    weights.append(idf[i]*doc_count)
    i += 1

final_line = 'TERM' + ','
i = 1
for f in files:
    final_line += 'D' + str(i) + ' ' + ','
    i += 1
final_line += ',' + 'IDF' + ',' + 'TF-IDF\n'

tf_arr = tf_line.split('\n')

i = 0
for term in s:
    final_line += term + "," + tf_arr[i] + ',' + str(round(idf[i], 2)) + ',' + ' ' + str(round(weights[i], 2)) + ',' + '\n'
    i += 1

fdoc = "/Users/naila/Desktop/tftables.txt"
outfile = open(fdoc, "w")
outfile.write(final_line)
outfile.close()

print("DONE")



