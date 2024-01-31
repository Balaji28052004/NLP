import re

def transformation_based_pos_tagger(words, rules):
    tagged_words = []

    for word in words:
        # Apply rules iteratively
        for pattern, replacement, pos_tag in rules:
            if re.search(pattern, word, flags=re.IGNORECASE):
                word = re.sub(pattern, replacement, word, flags=re.IGNORECASE)
                tagged_words.append((word, pos_tag))
                break
        else:
            # Default to a noun if no rule is applied
            tagged_words.append((word, 'NN'))

    return tagged_words

# Example usage
text_to_tag = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words_to_tag = re.findall(r'\b\w+\b', text_to_tag)

# Define transformation rules (pattern, replacement, POS tag)
transformation_rules = [
    (r'\b(?:is|am|are)\b', 'VB', 'VB'),     # Verbs
    (r'\b(?:the|a|an)\b', 'DT', 'DT'),       # Determiners
    (r'\b(?:quick|brown|lazy)\b', 'JJ', 'JJ'),  # Adjectives
    (r'\b(?:fox|dog)\b', 'NN', 'NN'),        # Nouns
    (r'\b(?:jumps)\b', 'VBZ', 'VBZ'),         # Verbs (3rd person singular)
    (r'\b(?:over)\b', 'IN', 'IN'),           # Preposition
]

# Perform transformation-based POS tagging
tagged_text = transformation_based_pos_tagger(words_to_tag, transformation_rules)

# Display the original text and the tagged text
print("Original Text:")
print(text_to_tag)
print("\nTransformation-Based Part-of-Speech Tagging:")
print(tagged_text)
