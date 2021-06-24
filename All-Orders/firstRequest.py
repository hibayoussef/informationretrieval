from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os


def read_corpus_file_and_delete_stop_words():
    stop_words_list = stopwords.words('english')
    additional_stopwords = []

    with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
        for word in file:
            word = word.split('\n')
            additional_stopwords.append(word[0])

    stop_words_list += additional_stopwords

    dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'
    # save_dir = "C:/Users/Super/Desktop/IR/homework/Files_Without_SW/"

    files_without_sw = []
    for document in os.listdir(dir_path):
        with open(dir_path + document, "r") as reader:
            # save_file = open(save_dir + document, 'w')
            text = reader.read()

            text = text.replace('.', ' ').replace(',', ' ')
            text = text.replace(':', ' '). replace('?', ' ').replace('!', ' ')
            text = text.replace('  ', ' ')  # convert double space into single space
            text = text.replace('"', ' ').replace('``', ' ')
            text = text.strip()  # remove space at the end

            text_tokens = word_tokenize(text)
            tokens_without_sw = [word for word in text_tokens if
                                 (word not in stop_words_list)]
            # save_file.writelines(["%s " % item for item in tokens_without_sw])
            # print(document, ':', tokens_without_sw)
            files_without_sw.append(tokens_without_sw)

    return files_without_sw


print(read_corpus_file_and_delete_stop_words())


def read_corpus_files_and_make_stemming():
    stop_words_list = stopwords.words('english')
    additional_stopwords = []

    with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
        for word in file:
            word = word.split('\n')
            additional_stopwords.append(word[0])

    stop_words_list += additional_stopwords

    dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'
    save_dir = "C:/Users/Super/Desktop/IR/homework/Files_Without_SW/"

    for document in os.listdir(dir_path):
        with open(dir_path + document, "r") as reader:
            save_file = open(save_dir + document, 'w')
            text = reader.read()
            # -------------------
            text = text.replace('.', ' ').replace(',', ' ')
            text = text.replace(':', ' ').replace('?', ' ').replace('!', ' ')
            text = text.replace('  ', ' ')  # convert double space into single space
            text = text.replace('"', ' ').replace('``', ' ')
            text = text.strip()  # remove space at the end
            # ---------------

            text_tokens = word_tokenize(text)
            tokens_without_sw = [word for word in text_tokens if
                                 (word not in stop_words_list)]
            save_file.writelines(["%s " % item for item in tokens_without_sw])
            # print(document, ':', tokens_without_sw)
            ps = PorterStemmer()
            with open("../Files/nnnn.txt", "a+") as stemFile:
                for stemWord in tokens_without_sw:
                    stemFile.write(stemWord)
                    stemFile.write(":")
                    stemFile.write(ps.stem(stemWord))
                    stemFile.write('\n')

    return tokens_without_sw


read_corpus_files_and_make_stemming()
# print(read_corpus_files_and_make_stemming())
