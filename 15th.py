import nltk
from nltk import PCFG, ChartParser
from nltk.tree import Tree

pcfg_grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.4] | NP PP [0.3] | 'John' [0.3]
    Det -> 'the' [0.6] | 'my' [0.4]
    N -> 'cat' [0.7] | 'dog' [0.3]
    VP -> V NP [0.5] | VP PP [0.5]
    V -> 'chased' [0.9] | 'saw' [0.1]
    PP -> P NP [1.0]
    P -> 'in' [0.6] | 'with' [0.4]
""")

parser = ChartParser(pcfg_grammar)


tokens = nltk.word_tokenize(sentence)

parsed_trees = parser.parse(tokens)
most_probable_tree = max(parsed_trees, key=lambda t: t.prob())

print("Most Probable Parse Tree:")
print(most_probable_tree)

most_probable_tree.draw()
