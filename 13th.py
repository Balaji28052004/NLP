class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children else []

    def __str__(self, level=0):
        result = "\t" * level + self.label + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

def parse_tree(grammar, input_string):
    words = input_string.split()
    chart = [[None for _ in range(len(words) + 1)] for _ in range(len(words) + 1)]
    for i in range(len(words) + 1):
        for symbol in grammar:
            if words[i-1] in grammar[symbol]:
                chart[i-1][i] = Node(symbol, [Node(words[i-1])])

    for width in range(2, len(words) + 1):
        for i in range(len(words) - width + 1):
            j = i + width
            for k in range(i + 1, j):
                for symbol in grammar:
                    if len(grammar[symbol]) == 2 and (chart[i][k] and chart[k][j]) and (chart[i][k].label == grammar[symbol][0] and chart[k][j].label == grammar[symbol][1]):
                        chart[i][j] = Node(symbol, [chart[i][k], chart[k][j]])

    return chart[0][len(words)]

# Example usage:
arithmetic_grammar = {
    'Expr': [['Expr', '+', 'Term'], ['Term']],
    'Term': [['Term', '*', 'Factor'], ['Factor']],
    'Factor': [['(', 'Expr', ')'], ['num']]
}

input_sentence = "( 3 + 4 ) * 2"
result_tree = parse_tree(arithmetic_grammar, input_sentence)

print(result_tree)
