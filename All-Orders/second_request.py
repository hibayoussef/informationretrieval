import nltk
from modifyFirstOrder import remove_stop_word_from_files
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()


# def lemma_files():
files = remove_stop_word_from_files()
punctuations = "?:!.,;"
marks = "''``"
for word in files:
    if word in punctuations and  word in marks:
        files.remove(word)
        files.remove(word)

files
print("{0:20}{1:20}".format("Word", "Lemma"))
for word in files:
    print("{0:20}{1:20}".format(word, wordnet_lemmatizer.lemmatize(word)))



# print(lemma_files)