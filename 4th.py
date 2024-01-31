class PluralStateMachine:
    def __init__(self):

        self.states = {
            'start': self.start_state,
            'singular': self.singular_state,
            'regular_plural': self.regular_plural_state,
            'irregular_plural': self.irregular_plural_state,
        }

        self.current_state = 'start'

    def start_state(self, word):
        if word.endswith('s') or word.endswith('x') or word.endswith('z') or word.endswith('ch') or word.endswith('sh'):
            self.current_state = 'irregular_plural'
        else:
            self.current_state = 'singular'

    def singular_state(self, word):
        if word.endswith('y') and len(word) > 1 and word[-2] not in 'aeiou':
            self.current_state = 'regular_plural'
        elif word.endswith('s') or word.endswith('x') or word.endswith('z') or word.endswith('ch') or word.endswith('sh'):
            self.current_state = 'irregular_plural'

    def regular_plural_state(self, word):
        if word.endswith('y'):
            return word[:-1] + 'ies'
        elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return word + 'es'
        else:
            return word + 's'

    def irregular_plural_state(self, word):
  
        if word.endswith('s'):
            return word + 'es'
        else:
            return word + 's'

    def generate_plural(self, word):
        self.current_state = 'start'
        self.states[self.current_state](word)
        return self.states[self.current_state](word)


# Example usage:
plural_fsm = PluralStateMachine()

nouns = ['cat', 'dog', 'city', 'baby', 'box', 'bus']
for noun in nouns:
    plural_form = plural_fsm.generate_plural(noun)
    print(f"{noun} -> {plural_form}")
