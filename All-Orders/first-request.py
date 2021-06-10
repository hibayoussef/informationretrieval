from nltk.corpus import stopwords
import os

stop_words_list = stopwords.words('english')
additional_stopwords = []

with open("C:/Users/Super/Desktop/IR/homework/Lab4/IR Homework/stop words.txt", 'r') as file:
    for word in file:
        word = word.split('\n')
        additional_stopwords .append(word[0])

stop_words_list += additional_stopwords

dir_path = 'C:/Users/Super/Desktop/IR/homework/Lab4/corpus/corpus/'
save_dir = "C:/Users/Super/Desktop/IR/homework/Files_Without_SW/"

for document in os.listdir(dir_path):
    with open(dir_path + document, "r") as reader:
        save_file = open(save_dir + document, 'w')
        text = reader.read()
        cleaned = [word for word in text.split() if (word not in stop_words_list)]
        save_file.writelines(["%s\n" % item for item in cleaned])


