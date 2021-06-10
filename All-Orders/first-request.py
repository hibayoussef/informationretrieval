from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os

# 1-stop word processing
stop_words_list = stopwords.words('english')
additional_stopwords = []

with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
    for word in file:
        word = word.split('\n')
        additional_stopwords.append(word[0])

stop_words_list += additional_stopwords
# --------------

# 2-tokenize and stemming
dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'
save_dir = "C:/Users/Super/Desktop/IR/homework/Files_Without_SW/"

for document in os.listdir(dir_path):
    with open(dir_path + document, "r") as reader:
        save_file = open(save_dir + document, 'w')
        text = reader.read()
        text_tokens = word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if (word not in stop_words_list)]
        save_file.writelines(["%s " % item for item in tokens_without_sw])
        print(document, ':', tokens_without_sw)
        ps = PorterStemmer()
        with open("../Files/stemmer_words.txt", "a+") as stemFile:
            for stemWord in tokens_without_sw:
                stemFile.write(stemWord)
                stemFile.write(":")
                stemFile.write(ps.stem(stemWord))
                stemFile.write('\n')



