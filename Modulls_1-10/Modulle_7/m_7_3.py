class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        punctuation = ".,=!?:;-"
        translation_table = str.maketrans('', '', punctuation)
        words = {}
        for i in self.file_names:
            with open(i, 'r+', encoding='utf-8') as file:
                words[i] = file.read().translate(translation_table).lower().split()
        return words

    def count(self, word):
        dict_ = self.get_all_words()
        words = {}
        for key in dict_:
            number_word = 0
            tmp_vol = dict_.get(key)
            for wrd in tmp_vol:
                if word.lower() == wrd:
                    number_word += 1
            words[key] = number_word
        return words

    def find(self, word):
        dict_ = self.get_all_words()
        words = {}
        for key in dict_:
            count = 1
            tmp_vol = dict_.get(key)
            for wrd in tmp_vol:
                if word.lower() == wrd:
                    words[key] = count
                    break
                else:
                    count += 1
        return words


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
