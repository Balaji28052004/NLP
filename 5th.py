import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

def perform_stemming(words):

    porter_stemmer = PorterStemmer()

    stemmed_words = [porter_stemmer.stem(word) for word in words]
    
    return stemmed_words

word_list = ["running", "jumps", "swimming", "happily", "easily", "books"]

stemmed_list = perform_stemming(word_list)

for original, stemmed in zip(word_list, stemmed_list):
    print(f"{original} -> {stemmed}")
