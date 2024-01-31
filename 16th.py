import spacy

nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities

text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976. The company is known for its innovative products like the iPhone."

named_entities = perform_ner(text)

for entity, label in named_entities:
    print(f"{entity} - {label}")
