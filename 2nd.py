class State:
    def __init__(self, is_final):
        self.is_final = is_final
        self.transitions = {}
    def add_transition(self, char, next_state):
        self.transitions[char] = next_state
start_state = State(False)
intermediate_state = State(False)
final_state = State(True)
start_state.add_transition("a", intermediate_state)
intermediate_state.add_transition("b", final_state)
def is_accepted(string):
    current_state = start_state
    for char in string:
        if char not in current_state.transitions:
            return False
        current_state = current_state.transitions[char]
    return current_state.is_final
strings = ["ab", "abc", "abab", "ba"]
for string in strings:
    print(f"String: {string}, Accepted: {is_accepted(string)}")
