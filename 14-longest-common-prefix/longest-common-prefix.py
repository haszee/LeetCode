class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(min(strs, key=len))):
            letters = [str[i] for str in strs]

            if len(set(letters)) > 1:
                break
            else:
                prefix += list(set(letters))[0]

        return prefix
