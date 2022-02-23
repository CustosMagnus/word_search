from PyDictionary import PyDictionary

global fitting_terms
fitting_terms = []

def run(word, dic_list):
    o = open(dic_list, "r")
    word_list = o.read()
    o.close()
    word_list = word_list.split("\n")

    letters = "abcdefghijklmnopqrstuvwxyz"


    for f in range(len(word)):
        for i in range(len(letters)):
            word_new = list(word)
            word_new[f] = letters[i]
            word_new = "".join(word_new)
            for x in range(len(word_list)):
                if word_list[x] == word_new:
                    if word_new not in fitting_terms:
                        fitting_terms.append(word_new)


word = input("please enter word: ")
dic_list = ["corncob_lowercase.txt"]
for i in range(len(dic_list)):
    run(word, dic_list[i])

dictionary1 = PyDictionary()
for i in range(len(fitting_terms)):
    print(fitting_terms[i])
    print(dictionary1.meaning(fitting_terms[i]))