class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []

        # Take the "Cartesian product" of the possible values provided by a number.
        for num in digits:
            temp = []
            if num == "2":
                vals = ["a", "b", "c"]
            if num == "3":
                vals = ["d", "e", "f"]
            if num == "4":
                vals = ["g", "h", "i"]
            if num == "5":
                vals = ["j", "k", "l"]
            if num == "6":
                vals = ["m", "n", "o"]
            if num == "7":
                vals = ["p", "q", "r", "s"]
            if num == "8":
                vals = ["t", "u", "v"]
            if num == "9":
                vals = ["w", "x", "y", "z"]
            
            if len(out) == 0:
                out = vals
                continue

            for i in vals:
                for j in out:
                    temp.append(j + i)
            
            out = temp

        return out