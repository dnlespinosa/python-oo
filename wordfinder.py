"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    def __init__(self, file):
        self.file = file
        open_file = open('words.txt', 'r')
        self.open_file = open_file
        lst = []
        for word in self.open_file:
            lst.append(word)
        self.list = lst
        self.len = len(lst)
        print(len(lst), 'words read')
    
    def random(self):
        num = randint(0, self.len)
        wrd = self.list.pop(num)
        [*letters] = wrd
        letters.pop((len(letters)-1))
        strin = ''
        for letter in letters:
            strin = strin + letter
        return strin
        
class SpecialWordFinder(WordFinder):
    def __init__(self, file):
        super().__init__(file)
        no_blanks = []
        for item in self.list:
            if item == ' ':
                self.list.pop(self.list.index(item))
            elif item.startswith('#'):
                self.list.pop(self.list.index(item))

        