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

def CalculateComplexity(simple_count, complex_count, words):
	scount = 0
	ccount = 0
	for word in range(0, len(words)):
		if words[word] in simple_count:
			scount += simple_count[words[word]]
		if words[word] in complex_count:
			ccount += complex_count[words[word]]

	corp_complexity = ccount / scount
	return corp_complexity

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

# ############ Testing with a plethora of sentences #############

sent_s = open("./sentences/simple_sentences.txt", "r+")
sent_s_t = sent_s.read()

simple_sentences_d = {}
simple_sentences_d = ast.literal_eval(sent_s_t)

sent_s.close()

sent_c = open("./sentences/complex_sentences.txt", "r+")
sent_c_t = sent_c.read()

complex_sentences_d = {}
complex_sentences_d = ast.literal_eval(sent_c_t)

sent_c.close()

simple_sentences = []
complex_sentences = []

for value in simple_sentences_d.items():
	temp1 = [ value ]
	simple_sentences.append(temp1)

for value in complex_sentences_d.items():
	temp2 = [ value ]
	complex_sentences.append(temp2)

######################## Testing Ended ###############################
s_complexity = []
c_complexity = []

for i in range(0, len(simple_sentences)):
	given_sentence = simple_sentences[i][0][1]
	new_sentence = PreProcess(given_sentence)
	words = new_sentence.split(" ")
	s_complexity.append(CalculateComplexity(simple_count,complex_count,words))

for i in range(0, len(complex_sentences)):
	given_sentence = complex_sentences[i][0][1]
	new_sentence = PreProcess(given_sentence)
	words = new_sentence.split(" ")
	c_complexity.append(CalculateComplexity(simple_count,complex_count,words))

print("Simple", "\t\t\t", "Complex")
for i in range(0, len(s_complexity)):
	print(s_complexity[i], "\t", c_complexity[i])




		