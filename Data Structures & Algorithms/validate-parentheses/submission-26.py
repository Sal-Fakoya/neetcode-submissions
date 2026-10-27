# from collections import Counter

class Solution:

    def remover(self, stack:bool):
        self.stack.pop()

    def isValid(self, s: str) -> bool:
        length = len(s)
        
        half_length = length//2

        lookup = {"{":"}", "(":")", "[":"]"}
        # count = dict(Counter(s))

        stack = [""]     
        
        # s is not valid if its length is not even
        if length == 0:
            return False
        if length % 2 != 0:
            return False

        if s[0] in lookup.keys() and s[-1] in lookup.values():
            stack.append(s[0])
            index = 1

            while index <= length-1:
                stack.append(s[index])

                if stack[-2] in lookup.keys() and lookup[stack[-2]] == stack[-1]:
                    stack.pop()
                    stack.pop()
                index += 1

            if len(stack) == 1:
                return True
            else:
                return False
        else:
            return False

            

        

                        



