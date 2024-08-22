class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        reverse_num = ''

        for num in bin_num:
            if num == '0':
                reverse_num += '1'
            else:
                reverse_num += '0'

        return int(reverse_num,2)