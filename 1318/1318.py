#### Attempt 1 ####

'''
Make every binary operator the same length and iterate through the strings, counting 
the number of flips required for a OR b to match c.
'''

# class Solution:
#     def minFlips(self, a: int, b: int, c: int) -> int:

#         a_b = bin(a)[2:]
#         b_b = bin(b)[2:]
#         c_b = bin(c)[2:]

#         len_a = len(a_b)
#         len_b = len(b_b)
#         len_c = len(c_b)

#         max_l = max(len_a, len_b, len_c)

#         a_b = ('0' * (max_l - len_a)) + a_b
#         b_b = ('0' * (max_l - len_b)) + b_b
#         c_b = ('0' * (max_l - len_c)) + c_b

#         flip_count = 0

#         for i in range(max_l):
#             if c_b[i] == '1':
#                 if a_b[i] == '1' or b_b[i] == '1':
#                     continue
#                 else:
#                     flip_count += 1
#             else:
#                 flip_count += int(a_b[i]) + int(b_b[i])

#         return flip_count


#### Attempt 2 ####

'''
A more condensed approach to above, incorporating the same logic with bitwise operators. 
The left expression represents single flips that are necessary while the right allows us 
to account for situations when two flips are required.
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        return bin((a | b) ^ c).count('1') + bin((a & b) & ~c).count('1')