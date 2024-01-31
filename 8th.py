import random

# Sample corpus for training
training_corpus = [
    ("The", "DT"),
    ("quick", "JJ"),
    ("brown", "JJ"),
    ("fox", "NN"),
    ("jumps", "VBZ"),
    ("over", "IN"),
    ("the", "DT"),
    ("lazy", "JJ"),
    ("dog", "NN"),
]

def train_pos_tagger(corpus):
    # Create a basic probability distribution for each word and its corresponding POS tag
    pos_distribution = {}
    for word, pos_tag in corpus:
        if word in pos_distribution:
            pos_distribution[word].append(pos_tag)
        else:
            pos_distribution[word] = [pos_tag]

    return pos_distribution

def stochastic_pos_tagger(pos_distribution, words):
    # Assign POS tags based on the probability distribution
    tagged_words = []
    for word in words:
        if word in pos_distribution:
            pos_tag = random.choice(pos_distribution[word])
        else:
            # If the word is not in the training corpus, assign a default POS tag
            pos_tag = "NN"  # Default to noun for unknown words
        tagged_words.append((word, pos_tag))

    return tagged_words

# Example usage
text_to_tag = "The quick brown fox jumps over the lazy dog."

# Train the POS tagger using the provided training corpus
pos_distribution = train_pos_tagger(training_corpus)

# Tokenize the input text into words
words_to_tag = text_to_tag.split()

# Perform stochastic POS tagging
tagged_text = stochastic_pos_tagger(pos_distribution, words_to_tag)

# Display the original text and the tagged text
print("Original Text:")
print(text_to_tag)
print("\nStochastic Part-of-Speech Tagging:")
print(tagged_text)
