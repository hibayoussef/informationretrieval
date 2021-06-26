import string

import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import os

sw_nltk = stopwords.words('english')
print(sw_nltk)

print(len(sw_nltk))


# read files from corpus folder + tokenize
def read_files_from_corpus():
    dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'

    all_tokens_without_sw = []

    for document in os.listdir(dir_path):
        with open(dir_path + document, "r") as reader:
            text = reader.read()
            words = [word for word in text.split() if word.lower() not in sw_nltk]
            new_text = " ".join(words)
            # to be sure that the length is different before delete stop words and after delete
            print(new_text)
            print("Old length: ", len(text))
            print("New length: ", len(new_text))

        all_tokens_without_sw = all_tokens_without_sw + words

    return all_tokens_without_sw


read_files_from_corpus()


def get_tokens(text):
    read_corpus_files = read_files_from_corpus()
    lower = read_corpus_files.lower()
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lower.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens
