class LCS:

    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def longest_cs(self):
        ls = ''
        count = 0
        ls_temp = ''
        count_temp = 0

        ind = 0

        while ind < len(self.str1):
            for i in range(len(self.str2)):
                if self.str1[ind] == self.str2[i]: #if match is found, move forward simultaneously letter by letter in both strings
                    str1_forward = ind
                    str2_forward = i
                    while str1_forward < len(self.str1) and str2_forward < len(self.str2) and self.str1[str1_forward] == self.str2[str2_forward]:
                        ls_temp += self.str1[str1_forward]
                        #print ls_temp
                        count_temp += 1
                        #print (self.str1[str1_forward], self.str2[str2_forward])
                        str1_forward += 1
                        str2_forward += 1
                    if count < count_temp:
                        ls = ls_temp
                        count = count_temp

                    ls_temp = ''
                    count_temp = 0

            ind += 1

        print ls


    def lcs(self):
        ls = ''
        count = 0
        ls_temp = ''
        count_temp = 0

        ind = 0
        i = 0

        while ind < len(self.str1):
            while i < len(self.str2):
                if self.str1[ind] == self.str2[i]: #if match is found, move forward simultaneously letter by letter in both strings
                    str1_forward = ind
                    while str1_forward < len(self.str1) and i < len(self.str2) and self.str1[str1_forward] == self.str2[i]:
                        ls_temp += self.str1[str1_forward]
                        print ls_temp
                        count_temp += 1
                        print (self.str1[str1_forward], self.str2[i])
                        str1_forward += 1
                        i += 1
                    if count < count_temp:
                        ls = ls_temp
                        count = count_temp

                    ls_temp = ''
                    count_temp = 0
                else:
                    i += 1

            ind += 1
            i = 0

        print ls

    def lcs_DP(self):
        matrix = [[None for i in range(len(self.str1) + 1)] for i in range(len(self.str2) + 1)]

        longest_substr = 0
        index1 = None
        index2 = None

        for i in range(len(self.str2)):
            for j in range(len(self.str1)):
                if self.str1[j] == self.str2[i]:
                    matrix[i + 1][j + 1] = 1
                    if matrix[i][j] != None:
                        matrix[i + 1][j + 1] += matrix[i][j]
                        if matrix[i + 1][j + 1] > longest_substr:
                            longest_substr = matrix[i + 1][j + 1]
                            index1 = i
                            index2 = j

        print (longest_substr, index1, index2)

        res = ''
        while matrix[index1 + 1][index2 + 1] >= 1:
            res = self.str2[index1] + res
            index1 -= 1
            index2 -= 1

        print res
        print matrix





def main():
    l = LCS('The quick brown fox jumps over the lazy dog', 'A fox which is quick and brown jumps over the dog which is lazy')
    #l.lcs()
    l.lcs_DP()

if __name__ == '__main__':
    main()
