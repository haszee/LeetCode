class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        # if s[0] == ']' or s[0] == ')' or s[0] == '}':
        #     return False

        for bracket in s:
            if bracket == '[' or bracket == '(' or bracket == '{':
                brackets.append(bracket)
            elif len(brackets) == 0 and (bracket == ']' or bracket == ')' or bracket == '}'):
                return False
            elif bracket == ']':
                # if len(brackets) == 0:
                #     return False
                if brackets[-1] != '[':
                    return False
                else:
                    brackets.pop()
            elif bracket == ')':
                # if len(brackets) == 0:
                #     return False
                if brackets[-1] != '(' or len(brackets) == 0:
                    return False
                else:
                    brackets.pop()
            elif bracket == '}':
                # if len(brackets) == 0:
                #     return False
                if brackets[-1] != '{' or len(brackets) == 0:
                    return False
                else:
                    brackets.pop()
        if len(brackets) == 0:
            return True
        else:
            return False