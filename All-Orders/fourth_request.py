import enchant

d = enchant.Dict("en_US")
word = input("Enter word:")
d.check(word)
print(d.suggest(word))
k = (" ").join(d.suggest(word))
with open("C:/Users/Super/PycharmProjects/pythonProject/Files/enchant_word.txt" , 'w+') as fw:
    fw.write(k)
