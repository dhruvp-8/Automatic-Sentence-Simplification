import os
import shutil
import ast
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def PreProcess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	return " ".join(filtered_words)

# Obtain Count Dictionary from simple_count.txt
sc = open("simple_count.txt", "r+")
st = sc.read()

simple_count = {}
simple_count = ast.literal_eval(st)

sc.close()

# Obtain Count Dictionary from complex_count.txt
cc = open("complex_count.txt","r+")
ct = cc.read()

complex_count = {}
complex_count = ast.literal_eval(ct)



given_sentence = "The cat sat on the mat"
new_sentence = PreProcess(given_sentence)
words = new_sentence.split(" ")

scount = 0
ccount = 0
for word in range(0, len(words)):
	if words[word] in simple_count:
		scount += simple_count[words[word]]
	if words[word] in complex_count:
		ccount += complex_count[words[word]]

corp_complexity = ccount / scount

print("Sentence Simplicity:", corp_complexity)
		