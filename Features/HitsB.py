
# This file represents the #hitsB which is the total query term frequency in the table body
# this json file demonstrates a test run and the output per work and character

import sys
import os

file = open('re_tables-0001.json', 'r')
book = file.read()


def tokenize():
        if book is not None:
                words = book.lower().split()
                return words
        else:
                return None


def map_book(tokens):
        hash_map = {}

        if tokens is not None:
                for element in tokens:
                        # Remove Punctuation
                        word = element.replace(",","")
                        word = word.replace(".","")

                        # Word Exist?
                        if word in hash_map:
                                hash_map[word] = hash_map[word] + 1
                        else:
                                hash_map[word] = 0

                return hash_map
        else:
                return None

# Tokenize the file
words = tokenize()
word_list = ['the','life','situations','since','day', 'sky']


# Create a Hash Map (Dictionary)
map = map_book(words)

#class BreakIt(Exception): pass
# Show Word Information
while True:
        for word in word_list:
                flag = False
                try:
                        arr_counter = 0
                        # check if end of list has been reached
                        if (arr_counter+1) != len(word_list):
                                #put all your code here
                                print('Word: [' + word + '] Frequency: ' + str(map[word]))
                                pass
                                # increment the array counter
                                arr_counter += 1
                        flag = True

                except:
                #The append() method adds a single item to the existing list.
                # It doesn't return a new list; rather it modifies the original list.
                        word_list.append([word,1])
                        pass

                else:
                        continue

