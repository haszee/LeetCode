class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter.lower() in sentence or letter.upper() in sentence:
                continue
            else:
                return False

        return True