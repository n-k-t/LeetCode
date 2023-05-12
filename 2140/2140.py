#### Attempt 1 ####

'''
Uses depth-first search to solve for the best possible score on the exam. It checks whether or not 
the end of the question set has been reached, and if so it returns zero. If not, it returns the 
maximum points of either the next question (skipping and recursively calling the next index) or 
the current question's points and the next answerable question. The @cache decorator incorporates 
memoization (storing results in cache for fast re-access).

NOTE: this does not work without the decorator, LeetCode times out the process.
'''

# class Solution:
#     def mostPoints(self, questions: List[List[int]]) -> int:
#         len_q = len(questions)
        
#         @cache
#         def dfs(index):
#             if index >= len_q:
#                 return 0
#             return max(dfs(index + 1), questions[index][0] + dfs(questions[index][1] + index + 1))
        
#         return dfs(0)

#### Attempt 2 ####

'''
Iterative dynamic programming approach. The solution depends on states that occur after the 
current index, therefore we iterate downwards. Rather than taking a greedy approach and hoping 
for the best, we have broken it down into a sequence of smaller sub-problems (value functions) 
that are solved for a given state (i) over times 1 to n. Additionally, this is faster than a 
recursive approach and reduces the time complexity from exponential to linear.
'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Store the length so we don't calculate it everytime it's needed.
        len_q = len(questions)
        
        # Storage for the current maximum points that can be scored. The length plus one is a baseline 
        # of zero.
        storage = [0 for _ in range(len_q + 1)]

        # Iterate from the bottom of the array to the top. Take the maximum of the current question's 
        # point value plus whatever points are gained after the required waiting time (indexed overflow 
        # is blocked by choosing the minimum index of the wait or n, where n is always a value of 0) 
        # and the previous value that was chosen (farther ahead in the exam). This allows the algorithm 
        # to decide whether skipping a question or solving it will maximize the amount of points possible.
        for i in range(len_q - 1, -1, -1):
            storage[i] = max(questions[i][0] + storage[min(len_q, i + questions[i][1] + 1)], storage[i + 1])
        
        return storage[0]