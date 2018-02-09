import os
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from collections import Counter

main_sentence = "The cat perched the mat"

class Simple_Sentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    def __iter__(self):
        for line in open(os.path.join(self.dirname, "simple.txt"), encoding="utf8"):
            yield line.split()



def PreProcess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	return " ".join(filtered_words)

def CountWords(words):
    word_count = dict(Counter(words))
    x = Counter(word_count)
    return word_count

def CheckWordInDict(word_arr, fin_word_count):
    #print(word_arr)
    count = 0
    keep_counts_of_words = {}
    for word in range(0, len(word_arr)):
        if word_arr[word] in fin_word_count:
            count += fin_word_count[word_arr[word]]
            keep_counts_of_words[word_arr[word]] = fin_word_count[word_arr[word]]
    return keep_counts_of_words, count

###########################################################################################
#                             Simple Sentence                                             #
#                              Calculation                                                #
###########################################################################################


sentences = Simple_Sentences(r'C:\\Users\\Meenakshi\\Desktop\\Notebooks\\text_simplify_c')

cleaned_sentence = []
words = []
s = 0
for sentence in sentences:
    sent = ''
    for t in range(2, len(sentence)):
        sent += sentence[t] + " "    
    del sentence[:]
    cleaned_sentence.append(sent)
    cleaned_sentence[s] = PreProcess(cleaned_sentence[s])
    temp = cleaned_sentence[s].split(" ")
    for i in range(0, len(temp)):
        words.append(temp[i])
    s = s + 1

    #if s > 6: 
        #print(CountWords(words))
        #fin_word_count = CountWords(words)
        #with open('simple_count.txt', 'w') as myFile:
            #myFile.write(str(fin_word_count))
        #break 

fin_word_count = CountWords(words)
with open('simple_count.txt', 'w') as myFile:
    myFile.write(str(fin_word_count))
word_dict = {}
given_sentence = "Plants grow in month of April" 
fine_sentence = PreProcess(given_sentence)
word_arr = fine_sentence.split(" ")
word_dict, simple_count = CheckWordInDict(word_arr, fin_word_count)
#print(word_dict, simple_count)


###########################################################################################
#                             Complex Sentence                                            #
#                              Calculation                                                #
###########################################################################################


class Complex_Sentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    def __iter__(self):
        for line in open(os.path.join(self.dirname, "normal.txt"), encoding="utf8"):
            yield line.split()

complex_sentences = Complex_Sentences(r'C:\\Users\\Meenakshi\\Desktop\\Notebooks\\text_simplify_c')

cleaned_sentence = []
words = []
s = 0
for sentence in complex_sentences:
    sent = ''
    for t in range(2, len(sentence)):
        sent += sentence[t] + " "    
    del sentence[:]
    cleaned_sentence.append(sent)
    cleaned_sentence[s] = PreProcess(cleaned_sentence[s])
    temp = cleaned_sentence[s].split(" ")
    for i in range(0, len(temp)):
        words.append(temp[i])
    s = s + 1

    #if s > 6: 
        #print(CountWords(words))
        #fin_word_count = CountWords(words)
        #with open('complex_count.txt', 'w') as myFile:
            #myFile.write(str(fin_word_count))
        #break 

fin_word_count = CountWords(words)
with open('complex_count.txt', 'w') as myFile:
    myFile.write(str(fin_word_count))
word_dict = {}
given_sentence = "Plants grow in month of April" 
fine_sentence = PreProcess(given_sentence)
word_arr = fine_sentence.split(" ")
word_dict, complex_count = CheckWordInDict(word_arr, fin_word_count)
#print(word_dict, complex_count)


if simple_count != 0:
    sentence_complexity = complex_count / simple_count
    print("Sentence Complexity:", sentence_complexity)
else:
    print("Cannot determine complexity")             