class EarleyParser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar
        self.input_string = input_string
        self.chart = []

    def predict(self, state):
        for production in self.grammar[state.next_symbol()]:
            self.chart.append(State(state.next_symbol(), production, 0, state.origin))

    def scan(self, state):
        if self.input_string[state.origin] == state.next_symbol():
            self.chart.append(State(state.symbol, state.production, state.dot + 1, state.origin))

    def complete(self, state):
        for st in self.chart[state.origin]:
            if st.next_symbol() == state.symbol and st.dot < len(st.production):
                self.chart.append(State(st.symbol, st.production, st.dot + 1, st.origin))

    def parse(self):
        start_production = list(self.grammar.keys())[0]
        start_state = State('S', start_production, 0, 0)
        self.chart.append(start_state)

        for i in range(len(self.input_string) + 1):
            for state in self.chart:
                if state.is_complete():
                    self.complete(state)
                elif state.next_symbol() in self.grammar:
                    self.predict(state)
                elif state.origin < len(self.input_string):
                    self.scan(state)

        accepted = any(state.is_accept() for state in self.chart)
        if accepted:
            print("Parsing successful.")
        else:
            print("Parsing error: Invalid input.")

class State:
    def __init__(self, symbol, production, dot, origin):
        self.symbol = symbol
        self.production = production
        self.dot = dot
        self.origin = origin

    def next_symbol(self):
        if self.dot < len(self.production):
            return self.production[self.dot]
        return None

    def is_complete(self):
        return self.dot == len(self.production)

    def is_accept(self):
        return self.symbol == 'S' and self.is_complete() and self.origin == 0

# Example usage:
grammar = {
    'S': [['E']],
    'E': [['E', '+', 'T'], ['T']],
    'T': [['T', '*', 'F'], ['F']],
    'F': [['(', 'E', ')'], ['num']]
}

input_string = "num + num * num"
earley_parser = EarleyParser(grammar, input_string)
earley_parser.parse()
