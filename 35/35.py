class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = -1
        l_t = 0
        r_t = len(nums)
        flag = False

        # Halve the sample bounds until the target is found or we can't divide it anymore. Adjust the bounds on each iteration.
        while flag != True:
            len_a = r_t - l_t

            if len_a == 1:
                if nums[l_t] == target:
                    return l_t
                elif nums[l_t] < target:
                    return r_t
                else:
                    return l_t

            int_div = len_a // 2
            rem = len_a % 2
            
            if nums[l_t + int_div] == target:
                return l_t + int_div
            elif nums[r_t - int_div - rem] == target:
                return r_t - int_div - rem
            elif nums[l_t + int_div] < target:
                l_t = r_t - int_div - rem
            else:
                r_t = l_t + int_div