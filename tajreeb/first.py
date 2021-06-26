from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import os


# read files from corpus folder + tokenize
def read_files_from_corpus():
    dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'

    all_tokens_without_sw = []

    for document in os.listdir(dir_path):
        with open(dir_path + document, "r") as reader:
            text = reader.read()

            # --------
            text = text.replace('.', ' ').replace(',', ' ')
            text = text.replace(':', ' ').replace('?', ' ').replace('!', ' ')
            text = text.replace('  ', ' ')  # convert double space into single space
            text = text.replace('"', ' ').replace('``', ' ')
            text = text.strip()  # remove space at the end

            # ------
            text_tokens = word_tokenize(text)

        all_tokens_without_sw = all_tokens_without_sw + text_tokens

    return all_tokens_without_sw


# print(read_files_from_corpus())

# return stop word list
def get_stop_words():
    stop_words_list = stopwords.words('english')
    additional_stopwords = []

    with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
        for word in file:
            if not word.isspace():
                # word = word.lower()
                word = word.split('\n')
                additional_stopwords.append(word[0])

    stop_words_list += additional_stopwords
    return stop_words_list


# print(get_stop_words())

# return files without stop words
def get_files_without_stop_words():
    corpus = read_files_from_corpus()
    stop_words_list = get_stop_words()
    files_without_sw = []
    for word in corpus:
        if word not in stop_words_list:
            files_without_sw.append(word.upper())
    return files_without_sw


# print(get_files_without_stop_words())


# make stemming
def read_corpus_files_and_stemming():
    file_with_stemming = []
    corpus_without_sw = get_files_without_stop_words()
    ps = PorterStemmer()
    with open("../Files/stemming_request.txt", "a+") as stemFile:
        for stemWord in corpus_without_sw:
            stemFile.write(stemWord)
            stemFile.write(":")
            stemFile.write(ps.stem(stemWord))
            stemFile.write('\n')
            file_with_stemming.append(ps.stem(stemWord))

    return file_with_stemming


print(read_corpus_files_and_stemming())
