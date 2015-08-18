class SN:

    def __init__(self, string):
        self.string = string

    def normalize(self):
        rework = self.string.lower()
        words = [word for word in rework.split()]
        print words
        temp = ''
        new_words = []
        for word in words:
            temp += word[0].upper()
            temp += word[1:]
            new_words.append(temp)
            temp = ''
        print ' '.join(new_words)


def main():
    string = input()
    s = SN(string)
    s.normalize()

if __name__ == '__main__':
    main()
