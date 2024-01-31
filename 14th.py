class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar
        self.subjects = set()
        self.verbs = set()

    def parse_sentence(self, sentence):
        words = sentence.split()
        for word in words:
            if word in self.grammar['Subject']:
                self.subjects.add(word)
            elif word in self.grammar['Verb']:
                self.verbs.add(word)

    def check_agreement(self):
        if self.subjects and self.verbs:
            for subject in self.subjects:
                for verb in self.verbs:
                    if (subject, verb) in self.grammar['Agreement']:
                        print(f"Agreement found: '{subject}' agrees with '{verb}' in the given context.")
                        return
            print("No agreement found.")
        else:
            print("Please provide a valid sentence with subjects and verbs.")

# Example usage:
agreement_grammar = {
    'Subject': ['He', 'She', 'They', 'I', 'You'],
    'Verb': ['is', 'are', 'am'],
    'Agreement': [('He', 'is'), ('She', 'is'), ('They', 'are'), ('I', 'am'), ('You', 'are')]
}

checker = AgreementChecker(agreement_grammar)

sentence1 = "He is happy"
sentence2 = "They am running"
sentence3 = "You are amazing"

checker.parse_sentence(sentence1)
checker.check_agreement()

checker = AgreementChecker(agreement_grammar)
checker.parse_sentence(sentence2)
checker.check_agreement()

checker = AgreementChecker(agreement_grammar)
checker.parse_sentence(sentence3)
checker.check_agreement()
