class NH:

    def __init__(self, needle, haystack):
        self.needle = needle
        self.haystack = haystack
        self.init_mod = len(self.haystack)
        #self.init_mod = 23

    def get_prime_mod(self):
        if self.init_mod == 1:
            self.init_mod += 1
        for i in range(2, self.init_mod):
            if self.init_mod % i == 0:
                self.init_mod += 1
                self.get_prime_mod()

    def hashfunction(self, number, mod):
        return number % mod

    def num_to_be_hashed(self, lis, length, base):
        result = 0
        power = length
        for i in range(length):
            result += lis[i] * base**(power - 1)
            power -= 1
        return result

    def compare(self):
        occurances = list()
        base = 256
        length = len(self.needle)
        self.get_prime_mod()

        needle_code = list()
        for i in self.needle:
            needle_code.append(ord(i))
        target_num_to_be_hashed = self.num_to_be_hashed(needle_code, length, base)
        target_hash = self.hashfunction(target_num_to_be_hashed, self.init_mod)

        start_code = list()
        for i in self.haystack[:len(self.needle)]:
            start_code.append(ord(i))
        start_num_to_be_hashed = self.num_to_be_hashed(start_code, length, base)
        start_hash = self.hashfunction(start_num_to_be_hashed, self.init_mod)

        if target_hash == start_hash:
            if self.needle == self.haystack[0:length]:
                occurances.append(0)

        previous = start_num_to_be_hashed
        for i in range(length, len(self.haystack)):
            #start_code.pop(0)
            #start_code.append(ord(self.haystack[i]))
            new_candidate = (previous - (base**(length - 1) * start_code[0])) * base + ord(self.haystack[i])
            start_code.pop(0)
            start_code.append(ord(self.haystack[i]))
            #candidate = self.num_to_be_hashed(start_code, length, base)
            previous = new_candidate
            if target_hash == self.hashfunction(new_candidate, self.init_mod): #was candidate instead of new_candidate if used commented lines
                if self.needle == self.haystack[i - (length - 1):i + 1]:
                    occurances.append(i - (length - 1))

        return occurances


def main():
    n = NH('dog', 'thequickbrownfoxjumpsoverthelazydogthedogwasnotamused')

    print(n.compare())

if __name__ == '__main__':
    main()
