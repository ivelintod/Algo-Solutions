class SN:

    def __init__(self, string):
        self.string = string

    def normalize(self):
        rework = self.string.lower()
        words = [word for word in rework.split()]
        temp = ''
        for word in words:
            temp += word[0].upper()
            temp += word[1:] + ' '
        print(temp.strip())



def main():
    string = 'HAAACkaAA      MAaika!'
    s = SN(string)
    s.normalize()

if __name__ == '__main__':
    main()
