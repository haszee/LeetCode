class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        if s[0] == ']' or s[0] == ')' or s[0] == '}':
            return False

        for bracket in s:
            if bracket == '[' or bracket == '(' or bracket == '{':
                brackets.append(bracket)
            elif bracket == ']':
                if len(brackets) == 0:
                    return False
                elif brackets[-1] != '[':
                    return False
                else:
                    brackets.pop()
            elif bracket == ')':
                if len(brackets) == 0:
                    return False
                elif brackets[-1] != '(' or len(brackets) == 0:
                    return False
                else:
                    brackets.pop()
            elif bracket == '}':
                if len(brackets) == 0:
                    return False
                elif brackets[-1] != '{' or len(brackets) == 0:
                    return False
                else:
                    brackets.pop()
        if len(brackets) == 0:
            return True
        else:
            return False