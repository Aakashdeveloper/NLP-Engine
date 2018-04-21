import nltk
text="Mary had alittle lamb. Her fleece was white as snow"
from nltk.tokenize import word_tokenize, sent_tokenize
sents = sent_tokenize(text)
print(sents)

words =[word_tokenize(sent) for sent in sents]
print(words)