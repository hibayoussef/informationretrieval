
wordnet_lemmatizer = WordNetLemmatizer()





# ------------------------------
# remove stop words from files and save the files in directory
# def remove_stop_word_from_files():
#     stop_words_list = get_stop_words()
#     dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'
#     save_dir = "C:/Users/Super/Desktop/IR/homework/Files_Without_SW/"
#
#     all_tokens_without_sw = []
#
#     for document in os.listdir(dir_path):
#         with open(dir_path + document, "r") as reader:
#             save_file = open(save_dir + document, 'w')
#             text = reader.read()
#             text_tokens = word_tokenize(text)
#             tokens_without_sw = [word.replace(',', '').replace('.', '') for word in
#                                  text_tokens if (word not in stop_words_list)]
#             save_file.writelines(["%s " % item.replace(',', '').replace('.', '') for item in
#                                   tokens_without_sw])
#
#         all_tokens_without_sw = all_tokens_without_sw + tokens_without_sw
#
#     return all_tokens_without_sw
#
#
# print(remove_stop_word_from_files())
# with Handling . and ,

# print(remove_stop_word_from_files())

# -------------------------------


# stemming function
def stem():
    ps = PorterStemmer()
    file_words = remove_stop_word_from_files()
    with open("../Files/v.txt", "a+") as stemFile:
        for stemWord in file_words:
            stemFile.write(stemWord)
            stemFile.write(":")
            stemFile.write(ps.stem(stemWord))
            stemFile.write('\n')

    return stemFile


# stem()
#
# files = remove_stop_word_from_files()
# punctuations = "?:!.,;"
# marks = "''``"
# for word in files:
#     if word in punctuations and  word in marks:
#         files.remove(word)
#         files.remove(word)
#
# files
# print("{0:20}{1:20}".format("Word", "Lemma"))
# for word in files:
#     print("{0:20}{1:20}".format(word, wordnet_lemmatizer.lemmatize(word)))

