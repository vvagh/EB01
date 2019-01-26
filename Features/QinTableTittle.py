import json
import csv

# from itertools import zip_longest

sourceFile = open('/Users/vruti/PycharmProjects/new_corpus/venv/query40.json', 'r')
json_data = json.load(sourceFile)

# Ratio of the number of query tokens found in table title to total tokens
query = "Lake altitude"

query_str = []

query_str = (query.split())

# checking the query split
print(query_str)
print(query_str[0])
print(query_str[1])


count = 0
# checking for query in table title
for entry in json_data["table-1031-634"]["title"]:
    query_word1 = entry.find(query_str[0])
    query_word2 = entry.find(query_str[1])

    if query_word1 != -1:
        count += 1

    if query_word2 != -1:
        count += 1

print(count)
