import random

def generate_bigram_model(text):
    # Tokenize the text into words
    words = text.split()

    # Create a dictionary to store bigram frequencies
    bigram_model = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word in bigram_model:
            bigram_model[current_word].append(next_word)
        else:
            bigram_model[current_word] = [next_word]

    return bigram_model

def generate_text(bigram_model, seed_word, length=10):
    generated_text = [seed_word]

    for _ in range(length - 1):
        if seed_word in bigram_model:
            next_word_options = bigram_model[seed_word]
            next_word = random.choice(next_word_options)
            generated_text.append(next_word)
            seed_word = next_word
        else:
            break

    return ' '.join(generated_text)

# Example usage
corpus = "This is a sample text for the bigram model. The bigram model should generate text based on previous words."

bigram_model = generate_bigram_model(corpus)
generated_text = generate_text(bigram_model, seed_word="sample", length=10)

print("Generated Text:")
print(generated_text)
