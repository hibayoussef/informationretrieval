from firstRequest import read_corpus_file_and_delete_stop_words;

corpus = read_corpus_file_and_delete_stop_words();
# print(corpus)

z = []
irregular_verbs = []


def read_irregular_verbs():
    with open('C:/Users/Super/PycharmProjects/pythonProject/Files/irregular_verbs.txt', 'r') as file:
        for line in file:
            for word in line.split():
                irregular_verbs.append(word)

    return irregular_verbs


# print(read_irregular_verbs())


irregular_verbs_file = []


def access_irregular_verbs():
    irregular_verbs_list = read_irregular_verbs()
    for t in irregular_verbs_list:
        for words in corpus:
            for word in words:
                if t != word[0]:
                    continue
                else:
                    with open('../Files/irregular_verbs_output.txt', 'a+') as irregular_file:
                        irregular_file.write(t)

    return irregular_verbs_list


print(access_irregular_verbs())


import nltk
# from modifyFirstOrder import remove_stop_word_from_files
# from nltk.stem import WordNetLemmatizer
#
# wordnet_lemmatizer = WordNetLemmatizer()
#
#
# # def lemma_files():
# files = remove_stop_word_from_files()
# punctuations = "?:!.,;"
# marks = "''``"
# for word in files:
#     if word in punctuations and word in marks:
#         files.remove(word)
#         files.remove(word)
#
# files
# print("{0:20}{1:20}".format("Word", "Lemma"))
# for word in files:
#     print("{0:20}{1:20}".format(word, wordnet_lemmatizer.lemmatize(word)))
#
#

# print(lemma_files)
