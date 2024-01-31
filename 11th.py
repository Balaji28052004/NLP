class SimpleParser:
    def __init__(self, input_string):
        self.tokens = iter(input_string)
        self.current_token = None

    def consume_token(self):
        self.current_token = next(self.tokens, None)

    def match(self, expected_token):
        if self.current_token == expected_token:
            self.consume_token()
        else:
            raise ValueError(f"Expected '{expected_token}', but found '{self.current_token}'")

    def parse(self):
        self.consume_token()
        self.expr()

        if self.current_token is None:
            print("Parsing successful.")
        else:
            raise ValueError("Parsing error: Unexpected tokens at the end.")

    def expr(self):
        self.term()
        while self.current_token in ['+', '-']:
            self.match(self.current_token)
            self.term()

    def term(self):
        self.factor()m 1
        while self.current_token in ['*', '/']:
            self.match(self.current_token)
            self.factor()

    def factor(self):
        if self.current_token.isdigit():
            self.match(self.current_token)
        elif self.current_token == '(':
            self.match('(')
            self.expr()
            self.match(')')
        else:
            raise ValueError(f"Unexpected token: {self.current_token}")


# Example usage:
input_expression = "3 + 4 * (2 - 1)"
parser = SimpleParser(input_expression)
parser.parse()
