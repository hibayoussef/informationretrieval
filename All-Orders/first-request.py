from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stopwords=[]
# file is object of file
with open("../Files/stop words.txt", 'r') as file:
    for word in file:
        word = word.split('/n')
        stopwords.append(word[0])

