import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download NLTK data for part-of-speech tagging
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tagging(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)

    return tagged_words

# Example usage
text_to_tag = "NLTK is a powerful library for natural language processing in Python."

tagged_text = pos_tagging(text_to_tag)

print("Original Text:")
print(text_to_tag)
print("\nPart-of-Speech Tagging:")
print(tagged_text)
