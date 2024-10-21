class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        max_splits = self.backtrack_memoize(s, len(s), set(), 0, 0)
        return max_splits

    # Use memoization with backtracking to iterate through all possible sub strings.
    def backtrack_memoize(self, s: str, len_s: int, subset: Set[str], start: int, c_max: int) -> int:
        # Update the current max number of unique substrings if needed.
        if len(subset) > c_max:
            c_max = len(subset)
        
        # Verify that, even if all remaining terms were singular, it's worth traversing the rest of the string.
        if c_max >= len(subset) + (len_s - start):
            return c_max

        for i in range(start + 1, len_s + 1):
            temp = s[start:i]

            # Only add the substring if it's unique.
            if temp not in subset:
                subset.add(temp)
                c_max = self.backtrack_memoize(s, len_s, subset, i, c_max)
                subset.discard(temp)

        return c_max