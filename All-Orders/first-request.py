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
words_In_document = []
totalDocuments = 0
for document in documents:
    with open(document, 'r') as doc:
        for line in doc:
            # print the content of each alone file as line
            print('document name:', document.name, line)
            for word in line.split():
                # print words that found in all files without separates
                words_In_document.append(word)

    totalDocuments += 1

# The contents of all files without separates
print('words_In_document:', words_In_document)
print('totalDocuments:', totalDocuments)
