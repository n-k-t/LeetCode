class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Convert the ASCII characters to decimal and create a tracking 
        # variable greater than the maximum difference in character 
        # values (this makes the assumption that the characters are 
        # always lower case.)
        letters = list(map(ord, letters))
        target = ord(target)
        min_char = 26

        # Iterate through the list finding the next smallest character.
        for i in letters:
            if (i - target > 0) and (i - target < min_char):
                min_char = i - target
        
        # If no character is smaller, then return the first character in 
        # the list. Otherwise, return the smallest character.
        if min_char == 26:
            return chr(letters[0])
        else:
            return chr(target + min_char)