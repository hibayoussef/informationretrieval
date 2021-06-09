from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os
stopwords = []
# file is object of file
with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
    for word in file:
        word = word.split('\n')
        stopwords.append(word[0])

print('stopwords', stopwords)

# import os
#
# with os.scandir('../Files/stop words.txt') as entries:
#     for entry in entries:
#         stopwords.append(entry[0])
#         print(entry)
