class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to hold the "open" container characters as they are found.
        balance = []

        # Iterate through each character in the string. Add it to the stack 
        # if it is an open character, otherwise check if the stack is empty 
        # (meaning that the first character is closing --> not valid). Then, 
        # check that the corresponding character at the top of the stack 
        # mirrors the closing character; if so, pop it off the stack, 
        # otherwise return false.
        for i in s:
            if (i == '(') or (i == '{') or (i == '['):
                balance.append(i)
            elif len(balance) == 0:
                return False
            else:
                len_b = len(balance)
                if (i == ')') and (balance[len_b - 1] == '('):
                    balance.pop(len_b - 1)
                elif (i == '}') and (balance[len_b - 1] == '{'):
                    balance.pop(len_b - 1)
                elif (i == ']') and (balance[len_b - 1] == '['):
                    balance.pop(len_b - 1)
                else:
                    return False

        # If the stack is empty at the end, return true, otherwise return 
        # false. 
        if len(balance) == 0:
            return True
        else:
            return False 