class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Return if the number of rows is 1.
        if numRows == 1:
            return s

        len_s = len(s)
        
        store = []

        # Iterate over a row and calculate the stride on the fly (storing the character at the index) until you hit the end of 
        # the string, then move onto the next row.
        for i in range(numRows):
            prev = i % (numRows - 1)

            ind = i
            

            while ind < len_s:
                store.append(s[ind])

                temp = ((numRows - 1) - prev)

                ind += 2 * ((numRows - 1) - prev)
                prev = temp % (numRows - 1)
        
        return "".join(store)