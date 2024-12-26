class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'

        str_list = list(s)

        i = 0
        j = len(s)-1

        while i < j:
            if str_list[i] in vowels:
                while j > i:
                    if str_list[j] in vowels:

                        temp = str_list[j]
                        str_list[j] = str_list[i]
                        str_list[i] = temp

                        j -= 1
                        break
                    else:
                        j -= 1
            i += 1

        return ''.join(str_list)