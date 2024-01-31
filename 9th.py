import re

def rule_based_pos_tagger(word):
    # Define regular expression patterns for different POS tags
    patterns = [
        (r'\b(?:is|am|are)\b', 'VB'),     # Verbs
        (r'\b(?:the|a|an)\b', 'DT'),       # Determiners
        (r'\b(?:quick|brown|lazy)\b', 'JJ'),  # Adjectives
        (r'\b(?:fox|dog)\b', 'NN'),        # Nouns
        (r'\b(?:jumps)\b', 'VBZ'),         # Verbs (3rd person singular)
        (r'\b(?:over)\b', 'IN'),           # Preposition
    ]

    # Apply patterns to determine the POS tag
    for pattern, pos_tag in patterns:
        if re.search(pattern, word, flags=re.IGNORECASE):
            return pos_tag

    # Default to a noun if no pattern is matched
    return 'NN'

def rule_based_pos_tagging(text):
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text)

    # Perform rule-based POS tagging
    tagged_words = [(word, rule_based_pos_tagger(word)) for word in words]

    return tagged_words

# Example usage
text_to_tag = "The quick brown fox jumps over the lazy dog."

# Perform rule-based POS tagging
tagged_text = rule_based_pos_tagging(text_to_tag)

# Display the original text and the tagged text
print("Original Text:")
print(text_to_tag)
print("\nRule-Based Part-of-Speech Tagging:")
print(tagged_text)
