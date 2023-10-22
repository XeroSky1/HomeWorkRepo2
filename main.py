class Alphabet:
    def __init__(self, lang, letters):
        self.language = lang
        self.letters = letters
    def print(self):    
        for i in self.letters:
            print(i)
    def letters_num(self):
        return len(self.letters)