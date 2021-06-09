from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os


# 1-Here we take words from stop words file and save it inside
stopwords = []
with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
    for stop_word in file:
        stop_word = stop_word.split('\n')
        stopwords.append(stop_word[0])

print('stopwords in file are:', stopwords)


# 2-read each file inside corpus dictionary and print the name of file and calculate the number of files
documents = os.scandir('C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus')
words = []
totalDocuments = 0
for document in documents:
    print('document name:', document.name)
    totalDocuments += 1

print('totalDocuments:', totalDocuments)
