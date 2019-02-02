import string
import codecs


fname = 'corpus.txt'

with codecs.open(fname, "rb",encoding='utf-8', errors='ignore') as fname:

    di = dict()
    for line in fname:
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        #print(line)
        for word in words:
            di[word]=di.get(word, 0) + 1
            #print(word)
String= "this is the best"

for k, v in di.items():
        #print(k,v)
        if k in String.split():
            print(k,v)



