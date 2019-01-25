
# This file represents the #hitsB which is the total query term frequency in the table body
# this json file demonstrates a test run and the output per work and character
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Frequency of words and char in the file : " + '\n',word_count("re_tables-0001.json"))
