import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')

text = "The cats are playing in the garden. They are very playful."

words = nltk.word_tokenize(text)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed words:", stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized words:", lemmatized_words)

for word in words:

    pos_tag = nltk.pos_tag([word])[0][1]
    print(f"{word}: {pos_tag}")

    if pos_tag.startswith("VB"):
        for form in lemmatizer.lemmatize(word, pos="v"):
            print(f"  - Verb form: {form}")
