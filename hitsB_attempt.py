import errno
import glob  # glob module finds all the path names matching a specified pattern


path = '/Users/fatimapeygumbari/Downloads/WP_tables/re_tables-0001.json'

files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:  # opens the files and read them
            corpus = f.read()

            def tokenize():
                if corpus is not None:
                    words = corpus.lower().split()
                    return words
                else:
                    return None

            def map_table(tokens):
                hash_map = {}

                if tokens is not None:
                    for element in tokens:
                        word = element.replace(",", "")
                        word = word.replace(".", "")

                        if word in hash_map:
                            hash_map[word] = hash_map[word] + 1
                        else:
                            hash_map[word] = 1
                    return hash_map
                else:
                    return None

 words = tokenize()
 word = ['title', 'me']

 map = map_table(words)

for word in word_list:
 print('Word: [' + word + '] Frequency: ' + str(map[word]))

