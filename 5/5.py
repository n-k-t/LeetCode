class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        
        # Start by considering the entire string then progressivel shrinking the view.
        for i in range(len_s, 0, -1):
            for l_t in range((len_s + 1) - i):
                if self.is_palindrome(s, l_t, l_t + i, len_s):
                    return s[l_t:l_t + i]
    
    # Split the string in two and compare. If the length is odd, the middle term does not matter.
    def is_palindrome(self, s: str, l_t: int, r_t: int, len_s: int) -> bool:
        half_len = (r_t - l_t) // 2

        str_slice = s[l_t:r_t]

        for i in range(half_len):
            if str_slice[i] != str_slice[-(i + 1)]:
                return False
        
        return True